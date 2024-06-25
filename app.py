from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import my_view

# new instance of the Flask class
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

app.register_blueprint(my_view)

if __name__=="__main__":
	with app.app_context():
		db.create_all()
	app.run(debug=True, port=8000)