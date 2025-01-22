from database.db_connection import DB
from .entities.Comentario import *
from contextlib import closing
from concurrent.futures import ThreadPoolExecutor
from uuid import UUID

class ComentarioModel():

    @classmethod
    def get_all_coments_by_obra(self, id_obra: UUID):
        try:
            coments = list()
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT fecha, comentario, id_user FROM comentarios c WHERE id_obra = '{id_obra}'""")
                result = cursor.fetchall()
                with ThreadPoolExecutor() as tx:
                    for row in result:
                        coment = ComentUser(row[0],row[1],row[2])
                        coments.append(coment.to_JSON())
            return coments
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_all_coments_by_capi(self, id_obra: UUID, numero:int):
        try:
            coments = list()
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT fecha, comentario, id_user FROM comentarios c WHERE id_obra = '{id_obra}' and capitulo = {numero}""")
                result = cursor.fetchall()
                with ThreadPoolExecutor() as tx:
                    for row in result:
                        coment = ComentUser(row[0],row[1],row[2])
                        coments.append(coment.to_JSON())
            return coments
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def add_coment(self, id_obra:UUID ,coment, numero:int):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""insert into comentarios (id_user, id_obra, fecha, comentario, capitulo) values ('{coment.usuario}','{id_obra}', '{coment.fecha}', '{coment.descripcion}', {numero})""")
                conection.commit()
                afect_rows = cursor.rowcount
                return afect_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def delete_coment(self, id_coment):
        try:
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""delete from comentarios where id = '{id_coment}'""")
                conection.commit()
                afect_rows = cursor.rowcount
                return afect_rows
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
    @classmethod
    def get_coment_by_capitulo(self, id_obra: UUID, capitulo: int):
        try:
            coments = []
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT fecha, comentario, id_user FROM comentarios c WHERE id_obra = '{id_obra}' AND capitulo = {capitulo}""")
                result = cursor.fetchall()
                with ThreadPoolExecutor() as tx:
                    for row in result:
                        coment = ContextComentario(ComentUser(row[0].isoformat(),row[1],row[2]))
                        coments.append(coment.someone_strategy_json_coment())
            return coments
        except Exception as ex:
            raise Exception(ex)
