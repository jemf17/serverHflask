class Obra():

    def __init__(self, id, titulo, portada, vistas, likes, guardados, tag, capitulo, comentario, artista) -> None:
        self.id = id
        self.titulo = titulo
        self.portada = portada
        self.vistas = vistas
        self.likes = likes
        self.guardados = guardados
        self.tag = tag
        self.capitulo = capitulo
        self.comentario = comentario
        self.artista = artista
    def getId(self):
        return self.id
    def getTitulo(self):
        return self.titulo
    def getPortada(self):
        return self.portada
    def getVistas(self):
        return self.vistas
    def getLikes(self):
        return self.likes
    def to_JSON_capitulos(self):
        caps = []
        for cap in self.capitulo:
            caps.append(cap.to_JSON())
        return caps
    def to_JSON_comentario(self):
        comens = []
        for com in self.comentario:
            comens.append(com.to_JSON())
        return comens
    def to_JSON_artist(self):
        arts = []
        for art in self.tag:
            arts.append(art.to_JSON())
        return arts
    def to_JSON_tag(self):
        tags = []
        for tag in self.tag:
            tags.append(tag.to_JSON())
        return tags      
    def to_JSON_all(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'portada': self.portada,
            'vistas': self.vistas,
            'likes': self.likes,
            'guardados': self.guardados,
            'capitulos': self.to_JSON_capitulos(),
            'comentarios': self.to_JSON_comentario(),
            'arts': self.to_JSON_artist(),
            'tags': self.to_JSON_tag() 
        }
    def to_JSON_view(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'portada': self.portada
        }