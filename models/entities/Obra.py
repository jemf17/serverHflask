class Obra():

    def __init__(self, id, titulo, portada, oneshot, capitulo, artista, tag = [], vistas = 0, likes = 0, idioma = [], guardados = 0, comentario = []) -> None:
        self.id = id
        self.titulo = titulo
        self.portada = portada
        self.oneshot = oneshot
        self.capitulo = capitulo
        self.artista = artista
        self.tag = tag
        self.vistas = vistas
        self.likes = likes
        self.idioma = idioma
        self.guardados = guardados
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
    def to_JSON_capitulos(self): 
#esto se puede mejorar haciendo una funcion que en vez de poner los JSON en un array y listo, hacer una funcion que me los almacene
#en diferentes diccionarios dependiendo el idioma ej: {'ingles':[...], 'espaniol':[...], etc} y que los arrays esten ordenados por numero de caps
#por ahora voy a hacer que la consulta este mas o menos ordenada con un orden by idioma and numero
        caps = []
        for cap in self.capitulo:
            caps.append(cap.to_JSON_view())
        return caps
    def to_JSON_comentario(self):
        if self.comentario != []:
            comens = []
            for com in self.comentario:
                comens.append(com.to_JSON())
            return comens
        return []
    def to_JSON_artist(self):
        arts = []
        for art in self.tag:
            arts.append(art.to_JSON())
        return arts
    """def to_JSON_tag(self):
        tags = []
        for tag in self.tag:
            tags.append(tag.to_JSON())
        return tags """      
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
            'idiomas' : self.idioma,
            'capitulos': self.to_JSON_capitulos(),
            'comentarios': self.to_JSON_comentario(),
            'arts': self.to_JSON_artist(),
            'tags': self.tag #no creo que haga falta hacerlo una clase ya que con simplemente una consulta SQL, basta para dar todos los nombres de los Tags
            #'tags': self.to_JSON_tag() 
        }
    def to_JSON_view(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'idiomas' : self.idioma,
            'portada': self.portada
        } #considero si es importante en poner el numero de likes, comentarios y favoritos, consultar con el equipo