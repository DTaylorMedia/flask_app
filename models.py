from app import db

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	task = db.Column(db.String(80), unique = True)
	complete = db.Column(db.Boolean, default=False)