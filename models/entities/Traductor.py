from .Usuario import Usuario

class Traductor(Usuario):
    def __init__(self, calificacion, capitulosTraducidos = [], trabajosP=[], idiomas = [] ,*args, **kwargs) -> None:
        super.__init__(*args, **kwargs)
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
