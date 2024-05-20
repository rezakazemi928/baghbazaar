from os import getenv

from dotenv import load_dotenv
from flask import Flask

from config import Development, Production
from extensions import cors, db, ma, migrate

load_dotenv()

def create_app():
    """Create the flask app with related configs"""

    app = Flask(__name__)
    app_env = getenv("FLASK_ENV", "production")
    config = {
        "production": Production,
        "development": Development,
    }
    app.config.from_object(config[app_env])
    db.init_app(app)
    cors.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    return app