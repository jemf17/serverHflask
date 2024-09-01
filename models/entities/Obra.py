class Obra():

    def __init__(self, id, titulo, portada, oneshot ,vistas = 0, likes = 0, guardados = 0, capitulo = [], tag = [] ,comentario = [], artista =[]) -> None:
        self.id = id
        self.titulo = titulo
        self.portada = portada
        self.oneshot = oneshot
        self.guardados = guardados
        self.vistas = vistas
        self.likes = likes
        self.tag = tag
        self.capitulo = capitulo
        self.artista = artista
        self.comentario = comentario
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
    
    def to_JSON(self):
    #realizo dos funciones que retornan JSONS diferentes por que va a depender de lo que se necesite, para no saturar al front
    #de datos inecesarios que a lo mejor no utiliza, to_JSON_all; para ver la info de la obra al completo y to_JSON_view;
    #para ver lo basico de la obra
        return {
            'id': self.id,
            'titulo': self.titulo,
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
            'portada': self.portada
        } #considero si es importante en poner el numero de likes, comentarios y favoritos, consultar con el equipo