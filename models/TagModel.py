from database.db_connection import DB
from contextlib import closing
from .entities.Tag import Tag
from .entities.Obra import Obra

class TagModel():
    @classmethod
    def get_tag_name(self, id_obra):
        try:
            conection = DB().db_connection()
            tags = []
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT tag FROM obras_tags WHERE obras_tags.id_obra ='{id_obra}'""") 
                resultset = cursor.fetchall()
                for row in resultset:
                    tag = Tag(row[0])
                    tags.append(tag.to_JSON_view())
                return tags
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_obras_by_tag_order_time(self, tag: str, next: int):
        try:
            conection = DB().db_connection()
            obras = []
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""
                        SELECT id, titulo, titulo_secundario, portada, oneshot, madure, v.visualizacion, v.favoritos, v.guardados, MAX(c.fecha) as ultimafecha 
                        FROM obras o 
                        inner join vistas v on v.id_obra = o.id 
                        inner join obras_tags ot on ot.id_obra = o.id 
                        inner join capitulos c on c.id_obra = o.id 
                        where ot.tag = '{tag}'
                        group by id, titulo, titulo_secundario, portada, oneshot, madure, 
                        v.visualizacion, v.favoritos, v.guardados 
                        order by ultimafecha LIMIT 20 OFFSET {next*20}""") 
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
    def get_all_tags(self, next: int):
        try:
            conection = DB().db_connection()
            tags = []
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""select t.nombre, t.descripcion, t.name_japanese FROM tags t order by t.nombre LIMIT 60 offset {next*60}""") 
                resultset = cursor.fetchall()
                for row in resultset:
                    tag = Tag(row[0], row[1], row[2])
                    tags.append(tag.to_JSON())
                return tags
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_obras_by_tag_order_popular(self, tag:str, next:int):
        try:
            conection = DB().db_connection()
            obras = []
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""
                        SELECT id, titulo, titulo_secundario, portada, oneshot, madure, v.visualizacion, v.favoritos, v.guardados, MAX(c.fecha) as ultimafecha 
                        FROM obras o 
                        inner join vistas v on v.id_obra = o.id 
                        inner join obras_tags ot on ot.id_obra = o.id 
                        inner join capitulos c on c.id_obra = o.id 
                        where ot.tag = '{tag}'
                        group by id, titulo, titulo_secundario, portada, oneshot, madure, 
                        v.visualizacion, v.favoritos, v.guardados
                        order by v.visualizacion LIMIT 20 OFFSET {next*20}""") 
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