from __future__ import annotations
from database.db_connection import DB
from .entities.Page import Page
from contextlib import closing
from abc import ABC, abstractmethod
from uuid import UUID

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
    def get_pages_by_capitulo(self, obra_id:UUID, numero:int):
        try:
            conection = DB().db_connection()
            pages = []
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT id_obra, numero_cap, imagen, orden FROM pages p WHERE p.id_obra = '{obra_id}' AND p.numero_cap = {numero} order by orden""") 
                resultset = cursor.fetchall()
                for row in resultset:
                    page = Page(row[0], row[1], row[2], row[3])
                    #print(page.to_JSON())
                    pages.append(page.to_JSON())
            return pages    
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_pages_by_capitulo_scan(self, obra_id:UUID, numero:int, id_scan:UUID):
        try:
            conection = DB().db_connection()
            pages = []
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT id_obra, numero, imagen, orden FROM pages_scans ps WHERE ps.id_obra = '{obra_id}' AND ps.numero = {numero} AND ps.id_scan = '{id_scan}' order by orden""") 
                resultset = cursor.fetchall()
                print(resultset)
                for row in resultset:
                    page = Page(row[0], row[1], row[2], row[3])
                    pages.append(page.to_JSON())
            return pages
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def update_page(self, id_obra:UUID, numero:int, orden:int,*args, **kwargs):
        try:
            pass
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def add_page(self, page:Page):
        try:
            return self._strategy.add_page(page)
        except Exception as ex:
            raise Exception(ex)
class PageStrategy(ABC):
    @abstractmethod
    def add_page(self, page:Page):
        pass
    @abstractmethod
    def update_page(self, id_obra, numero, orden, *args, **kwargs):
        pass
class StrategyPageArts(PageStrategy):
    @classmethod
    def add_page(self, page:Page):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""INSERT INTO Pages (imagen, orden, numero_cap, id_obra) 
                               VALUES ('{page.image}', {page.orden},{page.numero},'{page.id}')""")
                conection.commit()
                afect_rows = cursor.rowcount
            return afect_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def update_page(self, id_obra, numero, orden, *args, **kwargs):
        pass
class StrategyPageScan(PageStrategy):
    @classmethod
    def add_page(self, page:Page):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""INSERT INTO pages_scans (imagen, orden, numero, id_obra, id_scan) 
                               VALUES ('{page.image}', {page.orden},{page.numero},'{page.id}', '{page.id_scan}')""")
                conection.commit()
                afect_rows = cursor.rowcount
            return afect_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def update_page(self, id_obra, numero, orden, *args, **kwargs):
        pass