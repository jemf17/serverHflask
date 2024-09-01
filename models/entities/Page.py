class Page():
    def __init__(self, id, numero, image) -> None:
        self.id = id
        self.numero = numero
        self.image = image
    def to_JSON(self):
        return {
            "id": self.id,
            "numero": self.numero,
            "image": self.image
        }