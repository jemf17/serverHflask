from database.db_connection import DB
from .entities.Obra import Obra
from contextlib import closing
from models.CapituloModel import CapituloModel, StrategyCapituloArts, StrategyCapituloScan
from models.TagModel import TagModel
from models.ArtistModel import ArtistModel
from models.ComentarioModel import ComentarioModel
import pandas as pd
import numpy as np
from uuid import UUID
#from helper.img_save import save_img

class ObraModel():    
    @classmethod
    def get_obras(self, next:int):
        #recomienda obras basado en la popularidad de las mismas
        try:
            conection = DB().db_connection()
            obras = []
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT id, titulo, titulo_secundario, portada, oneshot, madure, v.visualizacion, v.favoritos, v.guardados, 
                               (v.favoritos::numeric * 2 + (v.visualizacion * EXTRACT(EPOCH FROM v.retencion)) * 0.5 + v.guardados::numeric * 3 - (EXTRACT(EPOCH FROM (NOW() - cs.ultimapubli)) / 9000000)) AS popularidad                               
                               from obras o inner join vistas v on o.id = v.id_obra 
                               inner join  (SELECT c.id_obra AS id_obra, MAX(c.fecha) AS ultimapubli FROM capitulos c GROUP BY c.id_obra) cs ON cs.id_obra = o.id
                               order by popularidad 
                               LIMIT 20 OFFSET {next*20}
                               """)
                resultset = cursor.fetchall()
                for row in resultset:
                    obra = Obra(row[0], row[1],row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    obras.append(obra.to_JSON_view())
                return obras           
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_obra(self, id: UUID):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT id, titulo, portada, oneshot, v.visualizacion , v.favoritos , v.guardados , titulo_secundario,madure, artista FROM Obras o inner join vistas v on v.id_obra = o.id WHERE id='{id}'""")
                row = cursor.fetchone()
                obra = None
                if row != None:
                    capitulos = CapituloModel.get_capitulos_by_obra(id, row[3])
                    tags = TagModel.get_tag_name(id)
                    arts = ArtistModel.get_colaboladores(id)
                    arts.append(row[9])
                    #coment = ComentarioModel.get_all_coments_by_obra(id)
                    obra = Obra(row[0], row[1],row[7], row[2], row[3],row[8],row[4], row[5], row[6], capitulos, tags,arts)
                    print(obra.to_JSON())
                return obra.to_JSON()       
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_obras_for_arts(self, id_arts:UUID):
        try:
            obras = []
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT id, titulo, titulo_secundario, portada, oneshot, madure, v.visualizacion, v.favoritos, v.guardados  FROM obras o inner join vistas v on v.id_obra = o.id where o.artista = '{id_arts}' or exists (select oa.id_obra from obras_artistas oa where oa.id_artist = '{id_arts}' and oa.id_obra = o.id )""")
                resultset = cursor.fetchall()
                for row in resultset:
                    obra = Obra(row[0], row[1],row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    obras.append(obra.to_JSON_view())
            return obras
        except Exception as ex:
            raise Exception(ex)        
    @classmethod
    def update_obra(self, obra: Obra):
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
    def delete_obra(self, id: UUID):
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
    def exist_obra(self, title: str):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT obra_titulo_unico('{title}')""")
                return cursor.fetchone()[0]
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def exist_obra_by_id(self, id_obra: UUID):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""select exists (select 1 from obras o where o.id = '{id_obra}')""")
                return cursor.fetchone()[0]
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_obra(self, obra: Obra, tags, arts, cap):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""INSERT INTO Obras (id, titulo, portada, oneshot, madure, titulo_secundario, artista) VALUES ('{obra.id}','{obra.titulo}','{obra.portada}',{obra.oneshot}, {obra.madure}, '{obra.titulosecu}', '{arts}')""")
                conection.commit()
                for tag in tags:
                    cursor.execute(f"""INSERT INTO Obras_Tags (id_obra, tag) VALUES('{obra.id}','{tag}')""")
                    conection.commit()
                afect_rows = cursor.rowcount
                capi = StrategyCapituloArts()
                afect_rows += capi.add_capitulo(cap, obra.id)
                #agregar un metodo en CapituloModel donde agrege los capitulos, en el front se tiene que ejecutar despues de agregar la obra
            return afect_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_obras_for_user(self, id:UUID, next:int):
        try:
            obras = []
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                 cursor.execute(
                "SELECT * FROM get_obras_for_user(%s, %s);",
                (id, next)
            )
            result = cursor.fetchall()
            obras = []
            for row in result:
                obra = Obra(
                    row[0], row[1], row[2], row[3], row[4], 
                    row[5], row[6], row[7], row[8]
                )
                obras.append(obra.to_JSON_view())
            return obras
                #consigue los tags de preferencia del usuario
                #cursor.execute(f"""select p.tag1, p.tag2, p.tag3,p.tag4,p.tag5,p.tag6 from 
                #               preferencias p where p.id_user = '{id}'""")
                #tags_pref = cursor.fetchone()
                #toma todas las obras habidas y por haber que contengan esos tags
                #cursor.execute(f"""select distinct ot.id_obra from obras_tags ot 
                #               WHERE EXISTS (SELECT 1 FROM unnest(ARRAY{tags_pref[0]}) AS valor WHERE valor = ot.tag)""")
                #id_obras =  cursor.fetchall()
                #ordena las obras segun el historial y retencion de esas mismas obras en los ultimos 30 dias
                #cursor.execute(f"""select h.id_obra, avg(tiempo) as tiempo from historiales h 
                #               WHERE fecha >= NOW() - INTERVAL '30 days' group by h.id_obra order by tiempo AND 
                #               EXISTS (SELECT 1 FROM unnest(ARRAY{id_obras}) AS valor WHERE valor = h.id_obra 
                #               LIMIT 20 OFFSET {next*20}""")
                #row_obras = cursor.fetchall()
                #obtiene toda la info sobre la lista de row_obras
                #cursor.execute(f"""SELECT id, titulo, titulo_secundario, portada, oneshot, madure, v.visualizacion, 
                #               v.favoritos, v.guardados from obras o inner join vistas v on o.id = v.id_obra 
                #               WHERE EXISTS (SELECT 1 FROM unnest(ARRAY{row_obras}) AS valor WHERE valor = o.id) """)
                #resultset = cursor.fetchall()
                #for row in resultset:
                #    obra = Obra(row[0], row[1],row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                #    obras.append(obra.to_JSON_view())
                #return obras           
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_f_g_obras_for_user(self, user:UUID):
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
    def like_obra(self, id_obra:UUID, id_user:UUID):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT fav_obra('{id_obra}', '{id_user}') """)
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def save_obra(self, id_obra:UUID, id_user:UUID):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT save_obra('{id_obra}', '{id_user}')""")
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def search_obra(self, search:str, next:int):
        try:
            obras = []
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""select distinct o.id,o.titulo,o.titulo_secundario, o.portada,o.oneshot, o.madure, v.visualizacion,v.favoritos,v.guardados , 
                                    cf.ultimafecha from obras o inner join obras_tags ot on o.id = ot.id_obra 
                                    inner join vistas v on v.id_obra = o.id
                                    inner join 
                                    (select c.id_obra as id_obra ,MAX(c.fecha) as ultimafecha from capitulos c group by c.id_obra) cf 
                                    on cf.id_obra = o.id 
                                    where 
                                    '{search}' LIKE CONCAT('%', ot.tag, '%') or o.titulo like '%{search}%' or 
                                    o.titulo_secundario like '%{search}%' 
                                    order by cf.ultimafecha LIMIT 20 OFFSET {next*20}""")
                resultset = cursor.fetchall()
                print(resultset)
                for row in resultset:
                    obra = Obra(row[0], row[1],row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    obras.append(obra.to_JSON_view())
            return obras
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def history(self, id_user:UUID, id_obra:UUID, tiempo:str, fecha:str, numero:int, id_scan:UUID = None):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                id_scan_value = f"'{id_scan}'" if id_scan is not None else "NULL"
                cursor.execute(f"""insert into historiales (id_user, id_obra, tiempo, fecha, numero, id_scan) 
                               values ('{id_user}', '{id_obra}', '{tiempo}', '{fecha}', {numero}, {id_scan_value})""")
                conection.commit()
                afect_rows = cursor.rowcount
            return afect_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def f_s_user(self, id_user:UUID, id_obra: UUID):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT 
                                    EXISTS (
                                        SELECT 1 
                                        FROM favoritos 
                                        WHERE id_user = '{id_user}' AND id_obra = '{id_obra}'
                                    ) AS favoritos,
                                    EXISTS (
                                        SELECT 1 
                                        FROM guardados 
                                        WHERE id_user = '{id_user}' AND id_obra = '{id_obra}'
                                    ) AS guardados
                                    """)
                resultset = cursor.fetchone()
            return {'favorito': resultset[0],'saved': resultset[1]}
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def oneshot_bool(self, id_obra: UUID):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""select exists (select 1 
                                    from obras o where o.id = '{id_obra}' 
                                    and o.oneshot = true ) as oneshot""")
                result = cursor.fetchone()
            return result[0]
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def count_search(search:str):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""
                                select distinct count(o.id)
                                from obras o inner join obras_tags ot on o.id = ot.id_obra 
                                inner join vistas v on v.id_obra = o.id
                                inner join 
                                (select c.id_obra as id_obra ,MAX(c.fecha) as ultimafecha from capitulos c group by c.id_obra) cf 
                                on cf.id_obra = o.id where 
                                '{search}' LIKE CONCAT('%', ot.tag, '%') or o.titulo like '%{search}%' or 
                                o.titulo_secundario like '%{search}%' 
                                """)
                result = cursor.fetchone()
            return result[0]
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def artis_permition(id_art:UUID, id_obra:UUID):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT 
                                    EXISTS (
                                        SELECT 1 
                                        FROM obras 
                                        WHERE artista = '{id_art}' AND id = '{id_obra}'
                                    ) AS permiso
                                    """)
                resultset = cursor.fetchone()
            return resultset[0]
        except Exception as ex:
            raise Exception(ex)