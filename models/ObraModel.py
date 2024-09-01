from database.db_connection import db_connection
from .entities.Obra import Obra
from contextlib import closing
class ObraModel():    
    @classmethod
    def get_obras(self):
        try:
            conection = db_connection()
            obras = []
            print("no entre al with")
            with closing(conection.cursor()) as cursor:
                cursor.execute("SELECT id, titulo, portada, oneshot, (SELECT count(*) FROM Historial WHERE Historial.id_obra = Obra.id) as views, (SELECT count(*) FROM Historial WHERE Historial.id_obra = Obra.id AND Historial.favorito != 0) as like, (SELECT count(*) FROM Historial WHERE Historial.id_obra = Obra.id AND Historial.guardado != 0) as guardado FROM Obra") # esta no es la consulta que iria en si, hay que generar una mas compleja
                resultset = cursor.fetchall()
                print("OwO entre al with")
                for row in resultset:
                    obra = Obra(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    obras.append(obra.to_JSON_view())
                    #aca se tienen que transformar las obras en objetos y agregar en la lista obras, obviamente no el objeto
                    #sino la serializasion a JSON
                #conection.close()
                print("estas son las obras:",obras)
                return obras           
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_obra(self, id):
        try:
            conection = db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute("SELECT id, titulo, portada, oneshot, (SELECT count(*) FROM Historial WHERE Historial.id_obra = Obra.id) as views, (SELECT count(*) FROM Historial WHERE Historial.id_obra = Obra.id AND Historial.favorito != 0) as like, (SELECT count(*) FROM Historial WHERE Historial.id_obra = Obra.id AND Historial.guardado != 0) as guardado FROM Obra WHERE id=%s",id) # esta no es la consulta que iria en si, hay que generar una mas compleja
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
    def get_obras_for_arts(self, id):
        pass        
    @classmethod
    def update_obra(self, id):
        pass
    
    @classmethod
    def delete_obra(self, id):
        pass
    @classmethod
    def post_obra(self, obra):
        pass
    @classmethod
    def get_obras_for_user(self, id):
        pass