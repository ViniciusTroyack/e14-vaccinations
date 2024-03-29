from datetime import datetime, timedelta
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql.expression import false
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class VaccineModel(db.Model):
    cpf: str
    name: str
    first_shot_date: str
    second_shot_date: str
    vaccine_name: str
    health_unit_name: str

    __tablename__ = "vaccine_cards"

    cpf = Column(String(11), primary_key=True)
    name = Column(String(60), nullable=False)
    first_shot_date = Column(DateTime, default=datetime.utcnow)
    second_shot_date = Column(DateTime, default=datetime.utcnow() + timedelta(days=90))
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String, nullable=False)
