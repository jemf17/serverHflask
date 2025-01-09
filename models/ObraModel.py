from database.db_connection import DB
from .entities.Obra import Obra
from contextlib import closing
from models.CapituloModel import CapituloModel
from models.TagModel import TagModel
from models.ArtistModel import ArtistModel
from models.ComentarioModel import ComentarioModel
import pandas as pd
import numpy as np
#from helper.img_save import save_img

class ObraModel():    
    @classmethod
    def get_obras(self):
        try:
            conection = DB().db_connection()
            obras = []
            with closing(conection.cursor()) as cursor:
                cursor.execute("""SELECT id, titulo, titulo_secundario, portada, oneshot, madure, v.visualizacion, v.favoritos, v.guardados  FROM obras o inner join vistas v on v.id_obra = o.id""") 
                resultset = cursor.fetchall()
                for row in resultset:
                    obra = Obra(row[0], row[1],row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
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
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT id, titulo, portada, oneshot, v.visualizacion , v.favoritos , v.guardados , titulo_secundario,madure FROM Obras o inner join vistas v on v.id_obra = o.id WHERE id='{id}'""")
                row = cursor.fetchone()
                obra = None
                if row != None:
                    capitulos = CapituloModel.get_capitulos_by_obra(id)
                    tags = TagModel.get_tag_name(id)
                    arts = ArtistModel.get_artists_by_obra(id)
                    coment = ComentarioModel.get_all_coments_by_obra(id)
                    obra = Obra(row[0], row[1],row[7], row[2], row[3],row[8],row[4], row[5], row[6], capitulos, tags, coment, arts)
                    obra = obra.to_JSON()
                
                return obra            
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_obras_for_arts(self, id_arts):
        try:
            obras = []
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT id, titulo, titulo_secundario, portada, oneshot, madure, v.visualizacion, v.favoritos, v.guardados  FROM obras o inner join vistas v on v.id_obra = o.id where exists (select oa.id_obra from obras_artistas oa where oa.id_arts = '{id_arts}' and oa.id_obra = o.id )""")
                resultset = cursor.fetchall()
                for row in resultset:
                    obra = Obra(row[0], row[1],row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    obras.append(obra.to_JSON_view())
            return obras
        except Exception as ex:
            raise Exception(ex)        
    @classmethod
    def update_obra(self, obra):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""UPDATE obras SET portada ='{obra.portada}', titulo ='{obra.titulo}', oneshot={obra.oneshot}, madure={obra.madure}, titulo_secundario='{obra.titulosecu}' WHERE id = '{obra.id}'""")
                conection.commit()
                afect_rows = cursor.rowcount
                return afect_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_obra(self, id):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""DELETE FROM obras WHERE id = {id}""")
                conection.commit()
                afect_rows = cursor.rowcount
                return afect_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def exist_obra(self, title):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT obra_titulo_unico('{title}')""")
                return cursor.fetchone()[0]
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def add_obra(self, obra, tags, arts, cap):
        try:
            """
            datos para agregar: titulo:varchar, portada:bytea, oneshot:bool, tags:[id], id_artista
            """
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""INSERT INTO Obras (id, titulo, portada, oneshot, madure, titulo_secundario, romance) VALUES ('{obra.id}','{obra.titulo}','{obra.portada}',{obra.oneshot}, {obra.madure}, '{obra.titulosecu}', {obra.reg})""")
                conection.commit()
                #registra primero el artista que posteo la obra, el resto vendra atravez de las invitaciones
                #tendre que ver si es mejor llamar la funcion aca o con solo esta consulta basta
                cursor.execute(f"""INSERT INTO Obras_artistas (id_obra, id_arts, push) VALUES ('{obra.id}', '{arts}', true)""")
                conection.commit()
                for tag in tags:
                    cursor.execute(f"""INSERT INTO Obras_Tags (id_obra, tag) VALUES('{obra.id}','{tag}')""")
                    conection.commit()
                afect_rows = cursor.rowcount
                afect_rows += CapituloModel.add_capitulo(cap, obra.id)
                #agregar un metodo en CapituloModel donde agrege los capitulos, en el front se tiene que ejecutar despues de agregar la obra
            return afect_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_obras_for_user(self, id):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                #cursor.execute(f"""select tag1, tag2, tag3, tag4, tag5, tag6, v1, v2, v3, v4, v5, v6 from preferencias p where p.id_user = {id}""")
                #row_user =  cursor.fetchone()
                #user_np = np.array(row_user[0:5], row_user[6:12])
                #user_pd = pd.DataFrame([row_user[0:5], row_user[6:12]], columns=['tag1, tag2, tag3, tag4, tag5, tag6'], index=['tags', 'value'])
                #cursor.execute(f"""""")
                pass
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def push_historial(self, historial):
        pass
    
    @classmethod
    def get_f_g_obras_for_user(self, user):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT id_obra FROM favoritos WHERE id_user = {user}""")
                rowF = cursor.fetchone()
                cursor.execute(f"""SELECT id_obra FROM guardados WHERE id_user = {user}""")
                rowG = cursor.fetchone()
                if rowG != None and rowG != None:
                    return {
                        "favorito": rowF[0],
                        "guardado": rowG[0]
                    }
                return {
                        "favorito": False,
                        "guardado": False
                    }
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def create_uuid(self):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute("""select generar_uuid_unico()""")
                result = cursor.fetchone()[0]
                return result
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def like_obra(self, id_obra, id_user):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT fav_obra('{id_obra}', '{id_user}') """)
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def save_obra(self, id_obra, id_user):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT save_obra('{id_obra}', '{id_user}')""")
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def search_obra(self, search, next):
        try:
            obras = []
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""select distinct o.id,o.titulo,o.titulo_secundario, o.portada, v.visualizacion,v.favoritos,v.guardados , o.fechacreate from obras o inner join obras_tags ot on o.id = ot.id_obra inner join vistas v on v.id_obra = o.id  where '{search}' LIKE CONCAT('%', ot.tag, '%') or o.titulo like '%{search}%' or o.titulo_secundario like '%{search}%' order by o.fechacreate LIMIT 20 OFFSET {next*20}""")
                resultset = cursor.fetchall()
                resultset = cursor.fetchall()
                for row in resultset:
                    obra = Obra(row[0], row[1],row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    obras.append(obra.to_JSON_view())
            return obras
        except Exception as ex:
            raise Exception(ex)