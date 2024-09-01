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