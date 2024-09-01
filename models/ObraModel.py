from database.db_connection import db_connection
from .entities.Obra import Obra
from contextlib import closing
from models.CapituloModel import CapituloModel
from models.TagModel import TagModel
class ObraModel():    
    @classmethod
    def get_obras(self):
        try:
            conection = db_connection()
            obras = []
            with closing(conection.cursor()) as cursor:
                cursor.execute("SELECT id, titulo, portada, oneshot, (SELECT count(*) FROM Historiales WHERE Historiales.id_obra = Obras.id) as views, (SELECT count(*) FROM Historiales WHERE Historiales.id_obra = Obras.id AND Historiales.favorito != 0) as like, (SELECT count(*) FROM Historiales WHERE Historiales.id_obra = Obras.id AND Historiales.guardado != 0) as guardado FROM Obras") 
                resultset = cursor.fetchall()
                for row in resultset:
                    obra = Obra(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    obras.append(obra.to_JSON_view())
                    #aca se tienen que transformar las obras en objetos y agregar en la lista obras, obviamente no el objeto
                    #sino la serializasion a JSON
                #conection.close()
                return obras           
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_obra(self, id):
        try:
            conection = db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"SELECT id, titulo, portada, oneshot, (SELECT count(*) FROM Historiales WHERE Historiales.id_obra = Obras.id) as views, (SELECT count(*) FROM Historiales WHERE Historiales.id_obra = Obras.id AND Historiales.favorito != 0) as like, (SELECT count(*) FROM Historiales WHERE Historiales.id_obra = Obras.id AND Historiales.guardado != 0) as guardado FROM Obras WHERE id={id}")
                row = cursor.fetchone()
                obra = None
                if row == row:
                    capitulos = CapituloModel.get_capitulos_by_obra(id)
                    tags = TagModel.get_tag_name(id)
                    obra = Obra(row[0], row[1], row[2], row[3],row[4], row[5], row[6], capitulos, tags)
                    obra = obra.to_JSON()
                
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