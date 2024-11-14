from __future__ import annotations
from abc import ABC, abstractmethod

class ContextComentario():
    def __init__(self, strategy: StrategyComentario):
        self._strategy = strategy
    
    @property
    def strategy(self) -> StrategyComentario:
        return self._strategy
    @strategy.setter
    def strategy(self, strategy: StrategyComentario) -> None:
        self._strategy = strategy
    def someone_strategy_json_coment(self):
        return self._strategy.to_JSON()
class StrategyComentario(ABC):
    @abstractmethod
    def to_JSON(self):
        pass
class ComentUser(StrategyComentario):
    def __init__(self, fecha, descripcion, usuario) -> None:
        self.fecha = fecha
        self.descripcion = descripcion
        self.usuario = usuario
    def to_JSON(self):
        return {
            'fecha': self.fecha,
            'descripcion': self.descripcion,
            #'usuario': self.usuario.to_JSON_view()
            'usuario': self.usuario
        }
class ComentObra(StrategyComentario):
    def __init__(self, fecha, descripcion,obra) -> None:
        self.fecha = fecha
        self.descripcion = descripcion
        self.obra = obra
    
    def to_JSON(self):
        return {
            'fecha': self.fecha,
            'descripcion': self.descripcion,
            #'usuario': self.obra.to_JSON_view()
            'obra': self.obra
        }