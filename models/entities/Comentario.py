class Comentario():
    
    def __init__(self, fecha, descripcion, usuario) -> None:
        self.fecha = fecha
        self.descripcion = descripcion
        self.usuario = usuario

    def to_JSON(self):
        return {
            'fecha': self.fecha,
            'descripcion': self.descripcion,
            'usuario': self.usuario.to_JSON_view()
        }