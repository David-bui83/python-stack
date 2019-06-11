from flask import Flask, render_template, redirect, request, session
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():
  mysql = connectToMySQL('pets')
  pets = mysql.query_db('SELECT * FROM pets')
  print(pets)
  return render_template('index.html', pets=pets)

@app.route('/add', methods=['POST'])
def add_pet():
  mysql = connectToMySQL('pets')
  print('hello from add')
  print(request.form['name'])
  print(request.form['type'])
  query = f"INSERT INTO pets (name, type, created_at, updated_at) VALUES ('{request.form['name']}', '{request.form['type']}', NOW(), NOW()) "
  
  mysql.query_db(query)
  # query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW()) "
  # data = {
  #   'name': request.form['name'],
  #   'type': request.form['type']
  # }
  # mysql.query_db(query, data)
  
  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)