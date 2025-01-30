from database.db_connection import DB
from contextlib import closing
from uuid import UUID

class SolicitudModel():
    @classmethod
    def get_solicitudes_by_obra(cls, id_user: UUID):
        pass
    @classmethod
    def delete_solicitud(self, id_user: UUID):
        pass
    @classmethod
    def aceptar_solicitud(self, id_user: UUID, id_solicitud: UUID):
        pass
    @classmethod
    def rechazar_solicitud(self, id_user: UUID, id_solicitud: UUID):
        pass
    @classmethod
    def solicitar_pedido(self, id_user: UUID, id_obra: UUID):
        pass