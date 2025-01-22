from uuid import UUID
class Page():
    def __init__(self, id:UUID, numero:int, image:str, orden:int, id_scan:UUID = None) -> None:
        self.id = id
        self.numero = numero
        self.image = image
        self.orden = orden
        self.id_scan = id_scan
    def to_JSON(self):
        return {
            "image": self.image,
            "orden": self.orden
        }