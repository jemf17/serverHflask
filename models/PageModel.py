from database.db_connection import db_connection
from .entities.Page import Page
from contextlib import closing

class PageModel():
    @classmethod
    def get_pages_by_capitulo(self, obra_id, numero):
        try:
            conection = db_connection()
            pages = []
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"SELECT id_page AS id, (SELECT orden FROM Pages WHERE Pages.id = Capitulos_Pages.id_page) AS orden, (SELECT imagen FROM Pages WHERE Pages.id = Capitulos_Pages.id_page) AS imagen FROM Capitulos_Pages WHERE Capitulos_Pages.id_capitulo IN (SELECT id FROM Capitulos WHERE Capitulos.id_obra = {obra_id} AND Capitulos.numero = {numero})") 
                resultset = cursor.fetchall()
                print(resultset)
                for row in resultset:
                    page = Page(row[0], row[1], row[2])
                    print(page.to_JSON())
                    pages.append(page.to_JSON())
            return pages    
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def count_pages_by_capitulo(self, id_capitulo):
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
    def add_page(self, page, capNumero, obraName):
        try:
            """
            datos para agregar: imagen:bytea, orden: int => para hacer subconsultas: CapNumero: Int, ObraName: varchar
            """
            conection = db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"INSERT INTO Pages (imagen, orden, id_capitulo) VALUES ({page.imagen}, {page.orden},SELECT id FROM Capitulos WHERE Capitulos.numero = {capNumero} AND Capitulos.id_obra = (SELECT obras.id FROM Obras WHERE Obras.titulo = {obraName}) )")
                conection.commit()
        except Exception as ex:
            raise Exception(ex)