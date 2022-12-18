from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, RadioField
from wtforms.validators import  DataRequired, Length, Email, EqualTo, uuid


db: SQLAlchemy = SQLAlchemy()



"""
from extensions import db
from models.post import Post
db.create_all()
"""
