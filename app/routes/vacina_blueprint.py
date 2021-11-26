from flask import Blueprint
from app.controllers.vacina_controller import get_all, create_vaccine_card

bp_vaccine = Blueprint("bp_vaccine", __name__, url_prefix="/vaccinations")

bp_vaccine.get("")(get_all)
bp_vaccine.post("")(create_vaccine_card)
