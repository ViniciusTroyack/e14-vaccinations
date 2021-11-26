from app.routes.vacina_blueprint import bp_vaccine
from flask import Flask

def init_app(app: Flask):
    app.register_blueprint(bp_vaccine)
