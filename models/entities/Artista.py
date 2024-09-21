from entities import Usuario

class Artista(Usuario):
    #tengo que ver como generar las instancias de invitaciones en el diagrama de clases
    def __init__(self,id, userName, email, fechadecreacion, descripcion, obras = [], pedidos = [], solicitudes = [], perfil="https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fimages%2Fdefault-profile-picture%2F64676383&psig=AOvVaw1Pj6fj_WKiVuyvrpaQw_i0&ust=1726677697844000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNCO4vK1yogDFQAAAAAdAAAAABAE") -> None:
        super.__init__(id, userName, email, fechadecreacion, descripcion, perfil)
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