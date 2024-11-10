from .Usuario import Usuario

class Artista(Usuario):
    #tengo que ver como generar las instancias de invitaciones en el diagrama de clases
    def __init__(self, obras = [], pedidos = [], solicitudes = [],*args, **kwargs) -> None:
        super.__init__(*args, **kwargs)
        self.obras = obras
        self.pedidos = pedidos
        self.solicitudes = solicitudes

    def to_JSON(self):
        return {
            "userName": self.userName,
            "email": self.email,
            "perfilF" : self.perfil,
            "fechaDeCreacion": self.fechadeCreacion,
            "obras": self.obras,
            "pedidos": self.pedidos,
            "solicitudes": self.solicitudes
        }
    def to_JSON_view_name(self):
        return {
            "userName" : self.userName
        }
    def to_JSON_view(self):
        return {
            "userName": self.userName,
            "email": self.email,
            "perfilF" : self.perfil,
            "descripcion": self.descripcion,
            "fechaDeCreacion": self.fechadeCreacion,
            "obras": self.obras,
            "pedidos": self.pedidos,
            "solicitudes": self.solicitudes
        }