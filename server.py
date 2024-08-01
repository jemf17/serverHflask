from flask import Flask
from routes import Obra

app = Flask(__name__)

def error_page(error):
    return "<h1>Not Found Page<h1>", 404

if __name__ == '__main__':

    # Blueprint
    app.register_blueprint(Obra.main, url_prefix='/api/obra')

    # Error handlers
    app.register_error_handler(404, error_page)
    app.run(debug=True, threaded=True, port=5070)