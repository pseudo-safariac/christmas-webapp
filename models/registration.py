from extensions import db


class Staff(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	password = db.Column(db.String, nullable=False)
	first_name = db.Column(db.String, nullable=False)
	last_name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)
	phone_number = db.Column(db.String)
	sex = db.Column(db.String, nullable=False)
	job_category = db.Column(db.String, nullable=False)
	uuid = db.Column(db.String, nullable=False)
	priv_key = db.Column(db.BINARY, nullable=False)
	pub_key = db.Column(db.BINARY, nullable=False)