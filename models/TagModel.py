from database.db_connection import DB
from contextlib import closing
from .entities.Tag import Tag

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