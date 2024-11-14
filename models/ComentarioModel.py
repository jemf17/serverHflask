from database.db_connection import DB
from .entities.Comentario import *
from contextlib import closing
from concurrent.futures import ThreadPoolExecutor

class ComentarioModel():

    @classmethod
    def get_all_coments_by_obra(self, id_obra):
        try:
            coments = list()
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT fecha, comentario, id_user FROM comentarios c WHERE id_obra = '{id_obra}'""")
                result = cursor.fetchall()
                with ThreadPoolExecutor() as tx:
                    for row in result:
                        coment = ContextComentario(ComentUser(row[0],row[1],row[2]))
                        coments.append(coment.someone_strategy_json_coment())
            return coments
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def add_coment(self, coment):
        try:
            pass
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def delete_coment(self, id_coment):
        try:
            pass
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_all_coments_by_user(self, id_user):
        try:
            coments = list()
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT fecha, comentario, id_obra FROM comentarios c WHERE id_user = '{id_user}'""")
                result = cursor.fetchall()
                with ThreadPoolExecutor() as tx:
                    for row in result:
                        coment = ContextComentario(ComentObra(row[0],row[1],row[2]))
                        coments.append(coment.someone_strategy_json_coment())
            return coments
        except Exception as ex:
            raise Exception(ex)
