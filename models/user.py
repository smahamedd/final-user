from db import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)
    email = db.Column(String(100), nullable=False, unique=True)
    phone_number = db.Column(String(20), nullable=False)
    added_date = db.Column(DateTime, default=datetime.utcnow)
