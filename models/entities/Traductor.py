from entities import Usuario

class Traductor(Usuario):
    def __init__(self,id, userName, email, fechadecreacion, descripcion, calificacion, capitulosTraducidos = [], trabajosP=[], idiomas = [] ,perfil="https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fimages%2Fdefault-profile-picture%2F64676383&psig=AOvVaw1Pj6fj_WKiVuyvrpaQw_i0&ust=1726677697844000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNCO4vK1yogDFQAAAAAdAAAAABAE") -> None:
        super.__init__(id, userName, email, fechadecreacion, descripcion, perfil)
        self.calificacion = calificacion
        self.traducciones = capitulosTraducidos
        self.trabajosP = trabajosP
        self.idiomas = idiomas
    def to_JSON(self):
        return {
            "userName": self.userName,
            "email": self.email,
            "descripcion": self.descripcion,
            "perfilF" : self.perfil,
            "fechaDeCreacion": self.fechadeCreacion,
            "calificacion": self.calificacion,
            "traducciones": self.traducciones,
            "trabajosP" : self.trabajosP,
            "idiomas": self.idiomas
        }
