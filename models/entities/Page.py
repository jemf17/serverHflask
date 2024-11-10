class Page():
    def __init__(self, id, numero, image, orden) -> None:
        self.id = id
        self.numero = numero
        self.image = image
        self.orden = orden
    def to_JSON(self):
        return {
            "image": self.image,
            "orden": self.orden
        }