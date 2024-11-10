from __future__ import annotations
from database.db_connection import DB
from .entities.Page import Page
from contextlib import closing
from abc import ABC, abstractmethod

class PageModel():
    def __init__(self, strategy: PageStrategy) -> None:
        self._strategy = strategy
    @property
    def strategy(self) -> PageStrategy:
        return self._strategy
    @strategy.setter
    def strategy(self, strategy: PageStrategy) -> None:
        self._strategy = strategy
    @classmethod
    def get_pages_by_capitulo(self, obra_id, numero):
        try:
            conection = DB().db_connection()
            pages = []
            with closing(conection.cursor()) as cursor:
                print('inicio error')
                cursor.execute(f"""SELECT id_obra, numero_cap, imagen, orden FROM pages p WHERE p.id_obra = '{obra_id}' AND p.numero_cap = {numero} """) 
                print('fin error')
                resultset = cursor.fetchall()
                print(resultset)
                for row in resultset:
                    page = Page(row[0], row[1], row[2], row[3])
                    print(page.to_JSON())
                    pages.append(page.to_JSON())
            return pages    
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def count_pages_by_capitulo(self, id_obra, numero_capi):
        try:
            pass
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def update_page(self, id):
        try:
            pass
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def add_page(self, page, capNumero, obra_id):
        try:
            """
            datos para agregar: imagen:bytea, orden: int => para hacer subconsultas: CapNumero: Int, obra_id: varchar
            """
            conection = DB().db_connection()
            #img_url =  save_img(page.image)
            #if img_url == -1:
            #    return -1
            #creo que es mejor opcion que se guarde directamente las imagenes en el front
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"INSERT INTO Pages (imagen, orden, numero_cap, id_obra) VALUES ('{page.image}', {page.orden},{capNumero},'{obra_id}')")
                conection.commit()
                afect_rows = cursor.rowcount
            return afect_rows
        except Exception as ex:
            raise Exception(ex)
class PageStrategy(ABC):
    @abstractmethod
    def add_page(self, page, capNumero, obra_id):
        pass
class StrategyPageArts(PageStrategy):
    @classmethod
    def add_page(self, page, capNumero, obra_id):
        pass
class StrategyPageScan(PageStrategy):
    @classmethod
    def add_page(self, page, capNumero, obra_id):
        pass