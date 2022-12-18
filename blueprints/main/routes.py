from blueprints.main import bp
from flask import render_template, redirect, flash, url_for, request
from models.message import MessageDB, MessageForm
from extensions import db

from ua_parser import user_agent_parser

def extract_info_from_user_agent(user_agent):
	parsed_ua = user_agent_parser.Parse(user_agent)
	device_type = parsed_ua['device']['family']
	os = parsed_ua['os']['family']
	browser = parsed_ua['user_agent']['family']
	return device_type, os, browser


@bp.route('/', methods=['POST', 'GET'])
def index():
	form = MessageForm()

	if form.validate_on_submit():
		first_name = form.first_name.data.capitalize()
		last_name = form.last_name.data.capitalize()
		email = form.email.data
		message = form.message.data

		# Collect the technical information
		ip_address = request.remote_addr
		user_agent = request.headers.get('User-Agent')
		device_type, os, browser = extract_info_from_user_agent(user_agent)
		screen_resolution = request.headers.get('Screen-Resolution')
		accept_language = request.headers.get('Accept-Language')
		mode_preference = request.headers.get('Mode-Preference')

		data = MessageDB.query.filter_by(email=email).first()
		if not data:
			# Create a new MessageDB instance with the collected information
			data = MessageDB(
				name=f"{first_name} {last_name}",
				email=email,
				message=message,
				ip_address=ip_address,
				device_type=device_type,
				os=os,
				browser=browser,
				screen_resolution=screen_resolution,
				accept_language=accept_language,
				mode_preference=mode_preference
			)
			db.session.add(data)
			db.session.commit()
		else:
			# Update the existing MessageDB instance with the collected information
			data.name = f"{first_name} {last_name}"
			data.message = message
			data.ip_address = ip_address
			data.device_type = device_type
			data.os = os
			data.browser = browser
			data.screen_resolution = screen_resolution
			data.accept_language = accept_language
			data.mode_preference = mode_preference
			db.session.commit()
		flash('Your message has been successfully submitted and updated in the system!')

		# Reset the form
		form.reset()

		# Query the database for all messages
		messages = MessageDB.query.all()
		print(f"The table has : {len(messages)} entries")

		# Render the index template and pass in the messages as an argument
		return render_template('index.html', messages=messages, form=form, title='Merry Christmas!')

	if not form.validate_on_submit():
		flash("An entry with the given email address already exists. Please contact the administrator.")
		return render_template('index.html', form=form, title='Merry Christmas!')


