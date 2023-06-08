from flask import Flask
from config import Config
from app.extensions import db, migrate

def create_app(config_class=Config):
    # Konfigurasi APP
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initilizae database & migration
    db.init_app(app)
    migrate.init_app(app, db)

    # initilize blueprint
    from app.tweet import tweetBp
    app.register_blueprint(tweetBp, url_prefix='/tweets')

    return app