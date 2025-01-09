from __future__ import annotations
from database.db_connection import DB
from .entities.Capitulo import Capitulo
from contextlib import closing
from models.PageModel import PageModel
from concurrent.futures import ThreadPoolExecutor
from abc import ABC, abstractmethod
from models.entities.Page import Page
from uuid import UUID

class CapituloModel():
    def __init__(self, strategy: CapituloStrategy) -> None:
        self._strategy = strategy
    @property
    def strategy(self) -> CapituloStrategy:
        return self._strategy
    @strategy.setter
    def strategy(self, strategy: CapituloStrategy) -> None:
        self._strategy = strategy
    @classmethod
    def delete_capi(self, numero:int, id_obra: UUID, id_user:UUID) -> None:
        try:
            return self._strategy.delete_capi(numero, id_obra, id_user)
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_capitulos_by_obra(self,id_obra):
        try:
            conection = DB().db_connection()
            caps = []
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT numero, fecha, (SELECT nombre FROM idiomas WHERE Capitulos.id_idioma = idiomas.nombre ) as idioma FROM Capitulos WHERE Capitulos.id_obra = '{id_obra}' ORDER BY idioma, numero""") 
                resultset = cursor.fetchall()
                for row in resultset:
                    cap = Capitulo(row[0], row[1], row[2])
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
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT numero, fecha, (SELECT nombre FROM Idiomas WHERE Capitulos.id_idioma = Idiomas.nombre) FROM Capitulos WHERE numero = {numero} AND Capitulos.id_obra = '{id_obra}'""")
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
    def add_capitulo(self, cap, obraid):
        try:
            """
            datos para agregar: numero:int, fecha:date, idioma: id_idioma, id_obra: titulo de obra, pages: [pages]
            """
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""INSERT INTO Capitulos (numero, id_obra, fecha, id_idioma, pay) VALUES ({cap.numero},'{obraid}','{cap.fecha}','{cap.idioma}', false)""")
                conection.commit()
                afect_rows = cursor.rowcount
                with ThreadPoolExecutor() as tx:
                    for page in range(len(cap.pages)):
                        print(cap.pages[page])
                        pag = Page(obraid, cap.numero, cap.pages[page], page+1)
                        afect_rows += 1
                        tx.submit(PageModel.add_page(pag, cap.numero, obraid))
                
            return afect_rows
        except Exception as ex:
            raise Exception(ex)

        
class CapituloStrategy(ABC):

    @abstractmethod
    def add_capi_free(self, cap, obraid):
        pass
    @abstractmethod
    def add_capi_pay(self, *args, **kwargs):
        pass
    @abstractmethod
    def delete_capi(self, numero: int, obraid: UUID,*args, **kwargs):
        pass
class StrategyCapituloArts(CapituloStrategy):
    @classmethod
    def add_capitulo_free(self, cap, obraid):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""INSERT INTO capitulos (numero, id_obra, fecha, id_idioma, pay) VALUES ({cap.numero},{obraid},{cap.fecha},{cap.id_idioma}, false)""")
                conection.commit()
                afect_rows = cursor.rowcount
                with ThreadPoolExecutor as tx:
                    for page in cap.pages:
                        afect_rows += tx.submit(PageModel.add_page(page, cap.numero, obraid))
                
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
    def add_capitulo_free(self, cap, obraid):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""INSERT INTO capitulos_scans (numero, id_obra, fecha, id_idioma, pay) VALUES ({cap.numero},{obraid},{cap.fecha},{cap.id_idioma}, false)""")
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
    