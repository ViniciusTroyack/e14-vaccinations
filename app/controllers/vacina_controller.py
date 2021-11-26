from flask import request, current_app, jsonify
from app.models.vacina_model import VaccineModel
from sqlalchemy.exc import IntegrityError
import psycopg2.errorcodes


def create_vaccine_card():
    data = request.get_json()
    card_valid_keys = ["cpf", "name", "vaccine_name", "health_unit_name"]
    
    invalid_keys = [key for key in data.keys() if key not in card_valid_keys]
    for key in invalid_keys:
        data.pop(key, None)

    if not data['cpf'].isnumeric() or not len(data["cpf"]) == 11:
        return {"msg": "CPF invalido"}, 400

    try:
        vaccine_card = VaccineModel(**data)
        current_app.db.session.add(vaccine_card)
        current_app.db.session.commit()
    except IntegrityError as e:
        if e.orig.pgcode == psycopg2.errorcodes.NOT_NULL_VIOLATION:
            return {"msg": f'Chaves não encontradas {[key for key in card_valid_keys if key not in data.keys()]}'}, 400
        if e.orig.pgcode == psycopg2.errorcodes.UNIQUE_VIOLATION:
            return {"msg": "Cartão ja registrado"}, 409
    except TypeError:
            return {"msg": "Chave invalida"}, 400

    return jsonify(vaccine_card), 201


def get_all():
    cards = VaccineModel.query.all()

    return jsonify(cards)
