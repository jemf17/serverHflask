class Obra():

    def __init__(self,id, titulo,titulosecu,  portada, oneshot ,madure,vistas = 0, likes = 0, guardados = 0, capitulo = [], tag = [] ,comentario = [], artista =[]) -> None:
        self.id = id
        self.titulo = titulo
        self.titulosecu = titulosecu
        self.portada = portada
        self.oneshot = oneshot
        self.madure = madure
        self.guardados = guardados
        self.vistas = vistas
        self.likes = likes
        self.tag = tag
        self.capitulo = capitulo
        self.artista = artista
        self.comentario = comentario
    
    def to_JSON(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'titulo_sec': self.titulosecu,
            'portada': self.portada,
            'oneshot': self.oneshot,
            'vistas': self.vistas,
            'likes': self.likes,
            'guardados': self.guardados,
            'capitulos': self.capitulo,
            'comentarios': self.comentario,
            'arts': self.artista,
            'tags': self.tag #no creo que haga falta hacerlo una clase ya que con simplemente una consulta SQL, basta para dar todos los nombres de los Tags
                #'tags': self.to_JSON_tag() 
        }
    def to_JSON_view(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'portada': self.portada,
            'oneshot': self.oneshot,
            'vistas' : self.vistas,
            'likes' : self.likes,
            'guardados': self.guardados
        } #considero si es importante en poner el numero de likes, comentarios y favoritos, consultar con el equipo