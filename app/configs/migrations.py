from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    from app.models.vacina_model import VaccineModel

    Migrate(app, app.db)
