from flask import Flask, render_template, redirect, request, session, flash 
from mysqlconnection import connectToMySQL

app = Flask(__name__)

app.secret_key = 'abc'

@app.route('/')
def index():

  return render_template('index.html')

@app.route('/result', methods=['POST'])
def add_user():
  is_valid = True

  if len(request.form['name']) < 1:
    is_valid = False
    flash('Please enter your name')
  if len(request.form['location']) < 1:
    is_valid = False
    flash('Please choose a location')
  if len(request.form['language']) < 1:
    is_valid = False
    flash('Please choose a language')
  if len(request.form['comment']) < 1:
    comment = 'N/A'
  else: 
    comment = request.form['comment']
  print('is valid', is_valid)
    
  if not is_valid:
    return redirect('/')
  else:
    data = {
      'name': request.form['name'],
      'location': request.form['location'], 
      'language': request.form['language'],
      'comment': comment
    }

    sql = connectToMySQL('dojo_survey')
    query ='INSERT INTO members(name, location, language, comment) VALUES(%(name)s,%(location)s,%(language)s,%(comment)s);'

    user_id = sql.query_db(query,data)
    print(user_id)
    data = {
      'id': user_id
    }

    sql = connectToMySQL('dojo_survey')
    query = "SELECT * FROM members where id=%(id)s;"
    user = sql.query_db(query,data)
    print('users output below')
    print(user)

  return render_template('result.html',user=user[0])

if __name__ == '__main__':
  app.run(debug=True)