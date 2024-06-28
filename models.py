from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	task = db.Column(db.String(80), unique = True)
	complete = db.Column(db.Boolean, default=False)
	date_created = db.Column(db.DateTime, default=datetime.now())
	date_modified = db.Column(db.DateTime, default=datetime.now())