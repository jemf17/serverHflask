from database.db_connection import db_connection
from contextlib import closing
from .entities.Tag import Tag

class TagModel():
    @classmethod
    def get_tag_name(self, id_obra):
        try:
            conection = db_connection()
            tags = []
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"SELECT (SELECT name FROM Tags WHERE Tags.id = Obra_Tag.id) FROM Obra_Tag WHERE Obra_Tag.id_obra = {id_obra}") 
                resultset = cursor.fetchall()
                for row in resultset:
                    tag = Tag(row[0])
                    tags.append(tag.to_JSON_view())
                return tags
        except Exception as ex:
            raise Exception(ex)