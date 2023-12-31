# pylint: disable=too-few-public-methods
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()


class SecretKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    secret_key = db.Column(db.String(50), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    inactive_since = db.Column(db.DateTime, nullable=True)


class RunTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(), unique=True, nullable=False)
    value = db.Column(JSON, nullable=False)
