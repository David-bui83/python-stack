from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/users')
def users():
  mysql = connectToMySQL('users')
  users = mysql.query_db('SELECT * FROM users;')
  print(users)
  return render_template('users.html',users=users)

@app.route('/users/new')
def users_new():
  
  return render_template('create.html')

@app.route('/users/create', methods=['POST'])
def users_create():
  mysql = connectToMySQL('users')
  data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
  }
  query = "INSERT INTO users(first_name, last_name, email) VALUES(%(first_name)s,%(last_name)s,%(email)s);"

  user_id = mysql.query_db(query, data)
  print(user_id)

  return redirect('/users/'+ str(user_id))

@app.route('/users/<user_id>')
def user_id(user_id):
  print(user_id)

  data ={
    'id': user_id
  }

  mysql = connectToMySQL('users')
  query = "SELECT * FROM users where id=%(id)s;"
  user = mysql.query_db(query, data)
  return render_template('read_one.html', user=user[0])

@app.route('/users/<user_id>/edit')
def users_id_edit(user_id):
  print(user_id)

  data = {
    'id': user_id
  }

  mysql = connectToMySQL('users')
  query = "SELECT * FROM users where id=%(id)s;"
  user = mysql.query_db(query, data)
  print(user)

  return render_template('update.html', user=user[0])

@app.route('/users/<user_id>/update', methods=['POST'])
def users_id_update(user_id):
  print(user_id)

  data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'id': user_id
  }

  print(data)

  mysql = connectToMySQL('users')
  query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
  user = mysql.query_db(query, data)
  print(user)

  return redirect('/users/' + str(user_id))

@app.route('/delete/<user_id>')
def delete(user_id):
  print('user_id: ' +str(user_id))
  mysql = connectToMySQL('users') 
  mysql.query_db(f'DELETE FROM users WHERE id ={user_id}')
  
  return redirect('/users')

if __name__ == '__main__':
  app.run(debug=True)