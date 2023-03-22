from app import app
from app.models import import_models
from scripts import import_scripts
# from flask_seeder import FlaskSeeder
from routes import register_blueprints
from flask import request, jsonify


@app.route('/', methods=['GET'])
def index():
    return "THIS!! IS!! SPARTAAAAA!! charottt!! <3"


# configuration settings
def configure():
    import_models()
    import_scripts()
    register_blueprints()


# run configuration settings
configure()

if __name__ == "__main__":
    debug = True
    app.run(debug=True, host="0.0.0.0", port=5000)
    # socket.run(app, debug=debug, host='0.0.0.0', port=5000)
