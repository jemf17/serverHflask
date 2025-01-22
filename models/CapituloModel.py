from __future__ import annotations
from database.db_connection import DB
from .entities.Capitulo import Capitulo
from contextlib import closing
from models.PageModel import PageModel, StrategyPageArts, StrategyPageScan
from concurrent.futures import ThreadPoolExecutor
from abc import ABC, abstractmethod
from models.entities.Page import Page
from uuid import UUID
from models.ComentarioModel import ComentarioModel

class CapituloModel():
    @classmethod
    def get_capitulos_by_obra(self,id_obra:UUID, oneshot:bool):
        try:
            conection = DB().db_connection()
            caps = []
            if oneshot:
                with closing(conection.cursor()) as cursor:
                    cursor.execute(f"""select c.id_idioma, c.price, c.fecha from capitulos c where c.id_obra = '{id_obra}' and c.numero = {1}""")
                    row = cursor.fetchone()
                    cap = None
                    if row != None:
                        pages = PageModel.get_pages_by_capitulo(id_obra, 1)
                        coment = ComentarioModel.get_coment_by_capitulo(id_obra, 1)
                        fecha = row[2].isoformat()
                        cap = Capitulo(1,fecha,row[0],row[1],pages, coment)
                        caps.append(cap.to_JSON())
                    cursor.execute(f"""select cs.numero, cs.fecha ,cs.id_scan, cs.id_idioma, cs.price from capitulos_scans cs where cs.id_obra = '{id_obra}' and cs.numero  = {1}""")
                    row = cursor.fetchall()
                    for row in row:
                        pages = PageModel.get_pages_by_capitulo_scan(id_obra, 1, row[2])
                        fecha = row[1].isoformat()
                        cap = Capitulo(row[0], fecha,row[3],row[4],pages, None)
                        caps.append(cap.to_JSON_scan(row[2]))
                return caps
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT numero, fecha, id_idioma as idioma FROM Capitulos WHERE Capitulos.id_obra = '{id_obra}' ORDER BY idioma, numero""") 
                resultset = cursor.fetchall()
                for row in resultset:
                    fecha = row[1].isoformat()
                    cap = Capitulo(row[0], fecha, row[2])
                    caps.append(cap.to_JSON_view())
                return caps  
            #consulta sql para obtener capitulos por id de obra y ordenado por idioma y numeros
            #
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_capitulo_by_obra(self, id_obra, numero):
        try:
            conection = DB().db_connection()
            #obra original
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT numero, fecha, (SELECT nombre FROM idiomas WHERE Capitulos.id_idioma = idiomas.nombre ) as idioma FROM Capitulos WHERE Capitulos.id_obra = '{id_obra}' AND Capitulos.numero = {numero} ORDER BY idioma, numero""")
                row = cursor.fetchone()
                cap = None
                if row != None:
                    pages = PageModel.get_pages_by_capitulo(id_obra, numero)
                    cap = Capitulo(row[0],row[1],row[2],pages)
                    cap = cap.to_JSON()
            return cap

        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def exist_cap(self, id_obra, numero):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT cap_exist({id_obra}, {numero})""")
                return cursor.fetchone()[0]
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_max_capitulo(self, id_obra: UUID):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT max(numero) FROM capitulos WHERE id_obra = '{id_obra}'""")
                return cursor.fetchone()[0]
        except Exception as ex:
            raise Exception(ex)
        

        
class CapituloStrategy(ABC):

    @abstractmethod
    def add_capitulo(self, cap: Capitulo, obraid:UUID):
        pass
    @abstractmethod
    def delete_capi(self, numero: int, obraid: UUID,*args, **kwargs):
        pass
class StrategyCapituloArts(CapituloStrategy):
    @classmethod
    def add_capitulo(self, cap: Capitulo, obraid: UUID):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""INSERT INTO Capitulos (numero, id_obra, fecha, id_idioma, price) 
                               VALUES ({cap.numero},'{obraid}','{cap.fecha}','{cap.idioma}', {cap.price})""")
                print("llegue")
                conection.commit()
                afect_rows = cursor.rowcount
                with ThreadPoolExecutor() as tx:
                    for page in range(len(cap.pages)):
                        print(cap.pages[page])
                        pag = Page(obraid, cap.numero, cap.pages[page], page+1)
                        afect_rows += 1
                        tx.submit(StrategyPageArts.add_page(pag))
                
            return afect_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def delete_capi(self, numero: int, id_obra: UUID, id_user: UUID):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""DELETE FROM capitulos WHERE numero = {numero} AND id_obra = '{id_obra}'""")
                conection.commit()
                cursor.execute(f"""DELETE FROM pages WHERE numero_cap = {numero} AND id_obra = '{id_obra}'""")
                conection.commit()
                afect_rows = cursor.rowcount
                return afect_rows
        except Exception as ex:
            raise Exception(ex)
class StrategyCapituloScan(CapituloStrategy):
    @classmethod
    def add_capitulo(self, cap:Capitulo, obraid:UUID):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""INSERT INTO capitulos_scans (numero, id_obra, fecha, id_idioma, price) VALUES ({cap.numero},{obraid},{cap.fecha},{cap.id_idioma}, {cap.price})""")
                conection.commit()
                afect_rows = cursor.rowcount
                with ThreadPoolExecutor as tx:
                    for page in cap.pages:
                        afect_rows += tx.submit(PageModel.add_page(page, cap.numero, obraid))
                
            return afect_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def delete_capi(self, numero: int, id_obra: UUID, id_scan: UUID):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""DELETE FROM capitulos_scans WHERE numero = {numero} AND id_obra = '{id_obra}' AND id_scan = '{id_scan}'""")
                conection.commit()
                cursor.execute(f"""DELETE FROM pages_scans WHERE numero = {numero} AND id_obra = '{id_obra}' AND id_scan = '{id_scan}'""")
                conection.commit()
                afect_rows = cursor.rowcount
                return afect_rows
        except Exception as ex:
            raise Exception(ex)
    