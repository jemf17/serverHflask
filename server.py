from fastapi import FastAPI
from routes import Capitulo, Comentario, Obra, Page
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

# FastAPI middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

#routes
app.include_router(Capitulo.mainCapi)
app.include_router(Comentario.mainComent)
app.include_router(Obra.mainObra)
app.include_router(Page.mainPage)

"""from flask import Flask
from routes import Obra, Capitulo, Comentario

app = Flask(__name__)

def error_page(error):
    return "<h1>Not Found Page<h1>", 404

if __name__ == '__main__':

    # Blueprint
    #agregar un name cada vez que se registre un blueprint nuevo uwu
    app.register_blueprint(Capitulo.mainCapi, url_prefix='/capi', name='Capi')
    app.register_blueprint(Obra.mainObra, url_prefix='/obra', name='Obra')
    app.register_blueprint(Comentario.mainComent, url_prefix='/coment', name='Coment')
    # Error handlers
    app.register_error_handler(404, error_page)
    app.run(debug=True, threaded=True, port=5070) """