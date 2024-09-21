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
                cursor.execute("SELECT id, titulo, portada, oneshot, (SELECT count(*) FROM Historiales WHERE Historiales.id_obra = Obras.id) as views, (SELECT count(*) FROM Favoritos_Guardados WHERE guardado = 1 AND Favoritos_Guardados.id_obra = Obras.id) as like, (SELECT count(*) FROM Favoritos_Guardados WHERE guardado = 1 AND Favoritos_Guardados.id_obra = Obras.id) as guardado FROM Obras") 
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
            #las subconsultas de fav y guardados tienen que ser asi, por un tema de que se pueden generar conflictos si los
            #registramos en el historial
            #SELECT count(*) FROM Favoritos_Guardados WHERE guardado = 1 AND id_obra = 2
            conection = db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"SELECT id, titulo, portada, oneshot, (SELECT count(*) FROM Historiales WHERE Historiales.id_obra = Obras.id) as views, (SELECT count(*) FROM Favoritos_Guardados WHERE favorito = 1 AND Favoritos_Guardados.id_obra = {id}) as like, (SELECT count(*) FROM Favoritos_Guardados WHERE guardado = 1 AND Favoritos_Guardados.id_obra = {id}) as guardado FROM Obras WHERE id={id}")
                row = cursor.fetchone()
                obra = None
                if row != None:
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
    def add_obra(self, obra):
        try:
            """
            datos para agregar: titulo:varchar, portada:bytea, oneshot:bool, tags:[id], id_artista
            """
            conection = db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"INSERT INTO Obras (titulo, portada, oneshot) VALUES ({obra.titulo}, {obra.portada},{obra.oneshot})")
                conection.commit()
                #registra primero el artista que posteo la obra, el resto vendra atravez de las invitaciones
                #tendre que ver si es mejor llamar la funcion aca o con solo esta consulta basta
                cursor.execute(f"INSERT INTO Obras_Arts (id_obra, id_artist) VALUES ((SELECT id FROM Obras WHERE titulo = {obra.titulo}), {obra.artist})")
                conection.commit()
                for tag in obra.tag:
                    cursor.execute(f"INSERT INTO Obra_Tag (id_obra, id_tag) VALUES((SELECT id FROM Obras WHERE titulo = {obra.titulo}),{tag})")
                    conection.commit()
                afect_rows = cursor.rowcount
                #agregar un metodo en CapituloModel donde agrege los capitulos, en el front se tiene que ejecutar despues de agregar la obra
            return afect_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_obras_for_user(self, id):
        pass
    @classmethod
    def push_historial(self, historial):
        pass
    
    @classmethod
    def get_f_g_obra_for_user(self, user, obra):
        try:
            conection = db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f'SELECT favorito, guardado FROM Favoritos_Guardados WHERE id_user = {user} AND id_obra = {obra}')
                row = cursor.fetchone()
                if row != None:
                    return {
                        "favorito": row[0],
                        "guardado": row[1]
                    }
                return {
                        "favorito": False,
                        "guardado": False
                    }
        except Exception as ex:
            raise Exception(ex)