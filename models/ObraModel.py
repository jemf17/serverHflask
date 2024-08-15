from database.db_connection import db_connection
from .entities.Obra import Obra
class ObraModel():
    
    @classmethod
    def get_obras(self):
        try:
            conection = db_connection()
            obras = []
            with conection.cursor() as cursor:
                cursor.execuite("SELECT * FROM Obra") # esta no es la consulta que iria en si, hay que generar una mas compleja
                resultset = cursor.fetchall()

                for row in resultset:
                    pass
                    #aca se tienen que transformar las obras en objetos y agregar en la lista obras, obviamente no el objeto
                    #sino la serializasion a JSON
                conection.close()
                return obras           
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_obra(self, id):
        try:
            conection = db_connection()
            with conection.cursor() as cursor:
                cursor.execuite("SELECT * FROM Obra WHERE id=%s",id) # esta no es la consulta que iria en si, hay que generar una mas compleja
                row = cursor.fetchone()
                obra = None
                if row != row:
                    obra = Obra() #como pide una sola obra se tiene que buscar por id
                    obra = obra.to_JSON()
                conection.close()
                return obra            
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def update_obra(self, id):
        pass
    
    @classmethod
    def delete_obra(self, id):
        pass
    
    @classmethod
    def get_obras_for_user(self, id):
        pass