from database.db_connection import DB
from .entities.Artista import Artista
from contextlib import closing

class ArtistModel():
    @classmethod
    def get_all_artists(self):
        try:
            pass
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_artist(self, id):
        try:
            pass
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_artists_by_obra(self, id_obra):
        try:
            arts = list()
            conection = DB().db_connection()
            with closing(conection.cursor()) as cursor:
                cursor.execute(f"""SELECT id_arts FROM obras_artistas oa WHERE oa.id_obra = '{id_obra}' """)
                arts = cursor.fetchall()
            #conection = DB().supabase_connection()
            #with conection as cursor:
            #    pass
            return arts
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def add_artist_obra(self, id_obra):
        try:
            pass
        except Exception as ex:
            raise Exception(ex)