from flask import Blueprint,render_template,request,redirect,url_for
from datetime import datetime
from models import db,Todo

view = Blueprint('view', __name__)

@view.route("/")
def home():
	todo_list = Todo.query.all()
	return render_template("index.html", todo_list=todo_list)

@view.route("/add", methods=['POST'])
def add():
	new_todo = Todo(task=request.form.get('task'))
	db.session.add(new_todo)
	db.session.commit()
	return redirect(url_for('view.home'))

@view.route("/update/<todo_id>")
def update(todo_id):
	todo = Todo.query.filter_by(id=todo_id).first()
	todo.complete = not todo.complete
	todo.date_modified = datetime.now()

	# print(f"{todo.date_created} --- {todo.date_created.timestamp()}")
	# print(f"{todo.date_modified} --- {todo.date_modified.timestamp()}")
	# if todo.date_modified > todo.date_created:
	# 	print("> True!")
	# else:
	# 	print("> False")

	db.session.commit()
	return redirect(url_for('view.home'))

@view.route("/delete/<todo_id>")
def delete(todo_id):
	todo = Todo.query.filter_by(id=todo_id).first()
	db.session.delete(todo)
	db.session.commit()
	return redirect(url_for('view.home'))

@view.route("/page2")
def page():
	return render_template('page2.html')

