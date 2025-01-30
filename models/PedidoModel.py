from database.db_connection import DB
from contextlib import closing
from uuid import UUID
from models.entities import Pedido

class PedidoModel():
    @classmethod
    def get_pedido(self, id_pedido: UUID):
        pass
    @classmethod
    def get_pedidos_free(self, next:int):
        pass
    @classmethod
    def search_pedidos(self, search:str):
        pass
    @classmethod
    def cancelar_pedido(self, id_pedido: UUID):
        pass
    @classmethod
    def add_pedido(self, pedido:Pedido):
        pass