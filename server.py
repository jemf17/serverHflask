from flask import Flask
from routes import Obra, Capitulo

app = Flask(__name__)

def error_page(error):
    return "<h1>Not Found Page<h1>", 404

if __name__ == '__main__':

    # Blueprint
    #agregar un name cada vez que se registre un blueprint nuevo uwu
    app.register_blueprint(Capitulo.mainCapi, url_prefix='/capi', name='Capi')
    app.register_blueprint(Obra.mainObra, url_prefix='/obra', name='Obra')
    
    # Error handlers
    app.register_error_handler(404, error_page)
    app.run(debug=True, threaded=True, port=5070)