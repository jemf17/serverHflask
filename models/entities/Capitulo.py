class Capitulo():
    

    def __init__(self, numero, idioma, fecha , pages = []) -> None:
        self.numero = numero
        self.idioma = idioma
        self.fecha = fecha
        self.pages = pages
    
    def to_JSON_view(self):
    #ver comentario de Obra.py para entender el por que de dos funciones
        return {
            'numero': self.numero,
            'idioma': self.idioma,
            'fecha': self.fecha
        }
    def to_JSON(self):
        return {
            'numero': self.numero,
            'idioma': self.idioma,
            'fecha': self.fecha,
            'pages': self.pages
        }
        