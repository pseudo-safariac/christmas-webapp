from extensions import db
from extensions import FlaskForm, StringField, DataRequired, Length, Email, SubmitField, uuid

from datetime import datetime
import uuid


class MessageDB(db.Model):
	__tablename__ = 'messages'
	  
	id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime, default=datetime.now)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	message = db.Column(db.String, nullable=False)
	uuid = db.Column(db.String, nullable=False)
	ip_address = db.Column(db.String)
	device_type = db.Column(db.String)
	os = db.Column(db.String)
	browser = db.Column(db.String)
	screen_resolution = db.Column(db.String)
	accept_language = db.Column(db.String)
	mode_preference = db.Column(db.String)

	def __init__(self, name:str, email:str, message:str, ip_address:str, device_type:str, os:str, browser:str, screen_resolution:str, accept_language:str, mode_preference:str) -> None:
		self.name = name
		self.email = email
		self.message = message
		self.uuid = str(uuid.uuid1())
		self.ip_address = ip_address
		self.device_type = device_type
		self.os = os
		self.browser = browser
		self.screen_resolution = screen_resolution
		self.accept_language = accept_language
		self.mode_preference = mode_preference
	

class MessageForm(FlaskForm):
	first_name = StringField(label="First Name:", validators=[DataRequired(), Length(max=32)])
	last_name = StringField(label="Last Name:", validators=[DataRequired(), Length(max=32)])
	email = StringField(label="Email Address:", validators=[DataRequired(), Email(), Length(max=32)])
	message = StringField(label="Message:", validators=[DataRequired()])
	submit = SubmitField(label="Submit")

	def reset(self):
		self.first_name.data = ''
		self.last_name.data = ''
		self.email.data = ''
		self.message.data = ''

	





