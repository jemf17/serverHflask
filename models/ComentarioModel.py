from database.db_connection import db_connection
from .entities.Comentario import Comentario
from contextlib import closing

class ComentarioModel():

    @classmethod
    def get_all_coments_by_obra(self, id_obra):
        try:
            pass
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
            pass
        except Exception as ex:
            raise Exception(ex)