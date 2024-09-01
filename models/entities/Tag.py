class Tag():
    
    def __init__(self, nombre, descripcion = "") -> None:
        self.nombre = nombre
        self.descripcion = descripcion

    def to_JSON(self):
        return {
            'nombre': self.nombre,
            'descripcion': self.descripcion
        }
    def to_JSON_view(self):
        return self.nombre