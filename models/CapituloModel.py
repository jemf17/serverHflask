from database.db_connection import db_connection
from .entities.Capitulo import Capitulo
from contextlib import closing
from models.PageModel import PageModel

class CapituloModel():
    
    @classmethod
    def get_capitulos_by_obra(self,id_obra):
        try:
            conection = db_connection()
            caps = []
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"SELECT Capitulos.id, numero, fecha, (SELECT nombre FROM idiomas WHERE Capitulos.id_idioma = idiomas.id ) as idioma FROM Capitulos WHERE Capitulos.id_obra = {id_obra} ORDER BY idioma, numero") 
                resultset = cursor.fetchall()
                for row in resultset:
                    cap = Capitulo(row[0], row[1], row[2], row[3])
                    caps.append(cap.to_JSON_view())
                return caps  
            #consulta sql para obtener capitulos por id de obra y ordenado por idioma y numeros
            #
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_capitulo_by_obra(self, id_obra, numero):
        try:
            conection = db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"SELECT id, numero, fecha, (SELECT nombre FROM Idiomas WHERE Capitulos.id_idioma == Idiomas.id) FROM Capitulos WHERE numero == {numero} AND Capitulos.id_obra == {id_obra}")
                row = cursor.fetchone()
                cap = None
                if row != None:
                    pages = PageModel.get_pages_by_capitulo(id_obra, numero)
                    cap = Capitulo(row[0],row[1],row[2],row[3],pages)
                    cap = cap.to_JSON()
            return cap

        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def post_capitulo(self, cap):
        try:
            pass
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def delete_capitulo(self, id):
        try:
            pass
        except Exception as ex:
            raise Exception(ex)
    