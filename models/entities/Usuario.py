class Usuario():
    def __init__(self, id, userName, email, fechadecreacion, rechazo, descripcion, perfil="https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fimages%2Fdefault-profile-picture%2F64676383&psig=AOvVaw1Pj6fj_WKiVuyvrpaQw_i0&ust=1726677697844000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNCO4vK1yogDFQAAAAAdAAAAABAE" ) -> None:
        self.id = id
        self.userName = userName
        self.email = email
        self.fechadeCreacion = fechadecreacion
        self.rechazo = rechazo
        self.descripcion = descripcion
        self.perfil = perfil

    def to_JSON(self):
        return {
            "userName": self.userName,
            "email": self.email,
            "descripcion": self.descripcion,
            "perfilF" : self.perfil,
            "fechaDeCreacion": self.fechadeCreacion
        }
    def to_JSON_view(self):
        return {
            "userName": self.userName,
            "perfilF": self.perfil
        }