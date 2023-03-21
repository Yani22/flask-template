from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import dotenv_values
from flask_migrate import Migrate


# load environment variables
# load_dotenv()
ENV_VARIABLES = dotenv_values('.env')

# NOTE: this will only work if tzdata package is installed
app_timezone = 'Asia/Manila'

app = Flask(__name__)
# app = Flask(__name__, static_folder='../../aimhi-frontend/build/static', template_folder='../../aimhi-frontend/build')
app.config.from_object(ENV_VARIABLES['SERVER_CONFIGURATION'])
app.config['CORS_HEADERS'] = 'Content-Type'


cors = CORS(app)

# app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024 #50MB file limit
db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db, compare_type=True)