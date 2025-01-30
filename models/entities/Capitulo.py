from uuid import UUID
class Capitulo():
    def __init__(self, numero, fecha, idioma,price = 0, pages = [], comentario = []) -> None:
        #self.id = id
        self.numero = numero
        self.idioma = idioma
        self.fecha = fecha
        self.pages = pages
        self.comentario = comentario
        self.price = price
    def to_JSON_view(self):
    #ver comentario de Obra.py para entender el por que de dos funciones
        return {
            #'id': self.id,
            'numero': self.numero,
            'idioma': self.idioma,
            'fecha': self.fecha,
            'price': self.price
        }
    def to_JSON(self):
        return {
            #'id': self.id,
            'numero': self.numero,
            'idioma': self.idioma,
            'fecha': self.fecha,
            'pages': self.pages,
            'comentario': self.comentario,
        }
    def to_JSON_scan(self, id_scan:UUID):
        return {
            'id_scan': id_scan,
            'numero': self.numero,
            'idioma': self.idioma,
            'fecha': self.fecha,
            'pages': self.pages,
            'comentario': self.comentario
        }
        