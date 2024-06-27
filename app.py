from flask import Flask
from models import db
from views import view

# new instance of the Flask class
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)

app.register_blueprint(view)

if __name__=="__main__":
	with app.app_context():
		db.create_all()
	app.run(debug=True, port=8000)