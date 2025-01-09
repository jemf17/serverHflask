class Tag():
    
    def __init__(self, nombre, descripcion = "", namej = None) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
        self.namej = namej

    def to_JSON(self):
        return {
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'namej': self.namej
        }
    def to_JSON_view(self):
        return self.nombre