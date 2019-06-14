from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re

# Creating Flask app
app = Flask(__name__)
# Creating secret key
app.secret_key = 'asdf'
bcrypt = Bcrypt(app)

# Regex for valid email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# Regex for valid password 
PW_REGEX = re.compile(r'^[a-zA-Z0-9]{8,}')

# Root route
@app.route('/')
def index():
  return render_template('index.html')

# Process registration data from index html
@app.route('/registration', methods=["POST"])
def process():

  is_valid = True # Var for successful checks

  # Checking for valid first name length
  if len(request.form['first_name'])  < 2 or not request.form['first_name'].isalpha():
    is_valid = False
    flash('Invalid First Name', 'first_name')

  #Checking for valid last name length
  if len(request.form['last_name']) < 2 or not request.form['last_name'].isalpha():
    is_valid = False
    flash('Invalid Last Name', 'last_name')

  # Checking for valid email pattern
  if not EMAIL_REGEX.match(request.form['email']):
    is_valid = False
    flash('Invalid email','email')

  # Checking for unique email 
  sql = connectToMySQL('dojo')
  emails = sql.query_db('SELECT email FROM d_users')
  if len(emails) > 0:
    data = {
      'email': request.form['email']
    }
    sql = connectToMySQL('dojo')
    query = 'SELECT email from d_users where emial=%(email)s'
    user_email = sql.query_db(query,data)
    if not user_email:
      is_valid = False
      flash('Email is already in used', 'email')

  # Checking for valid email pattern
  if not PW_REGEX.match(request.form['password']):
      is_valid = False
      flash('Password must be at least 8 characters long', 'password')

  # Checking email confirmation
  if request.form['password'] != request.form['confirm_pw']:
    is_valid = False
    flash('Passowrd does not match', 'confirm_pw')

  # Checking for is_valid True/False
  if not is_valid:
    # Redirecting to Root
    return redirect('/')
  else:

    # Hashing password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    # Saving information into dictionary
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'password': pw_hash
    }

    # Connect to database
    sql = connectToMySQL('dojo')
    # Query statement to insert information into database
    query = "INSERT INTO d_users(first_name, last_name, email, password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
    # Inserting information into database
    user_id = sql.query_db(query, data)
    print(user_id)
    # saving user id into session
    session['user_id'] = user_id
    print(data)
  # Redirecting to success page
  return redirect('/success')

# Check for login 
@app.route('/login/check', methods=['POST'])
def log_in():

  data = {
    'email': request.form['lge'],
    'password': request.form['login-pw']
  }
  
  # Connect to database
  sql = connectToMySQL('dojo')
  query = 'SELECT email FROM d_users WHERE email=%(email)s;'
  user_email = sql.query_db(query, data)

  print(user_email)

  if not user_email:
    flash('Invalid email', 'login-email')
    return redirect('/')
  else:
    sql = connectToMySQL('dojo')
    query = 'SELECT password FROM d_users WHERE email=%(email)s;'
    user_pw = sql.query_db(query, data)
    print('user password below')
    print(user_pw)

    if not bcrypt.check_password_hash(user_pw[0]['password'], data['password']):
      flash('Invalid password', 'login_pw')
      return redirect('/')
    else:
      sql = connectToMySQL('dojo')
      query ='SELECT id FROM d_users WHERE email=%(email)s;'
      user_id = sql.query_db(query, data)
      session['user_id'] = user_id[0]['id']

  return redirect('/success')

@app.route('/success')
def success():
  # Check if session session is false
  if not session:
    # Redirect back to root
    return redirect('/')
  
  # Connect to database
  sql = connectToMySQL('dojo')
  # Storing id in dictionary
  data = {
    'id': session['user_id']
  }
  # Query Statement to get user information
  query = "SELECT * FROM d_users WHERE id=%(id)s"
  # Getting user information from database
  user = sql.query_db(query, data)
  
  # Rendering success.html and returning user information 
  return render_template('success.html',user=user[0])

# Delete route
@app.route('/delete')
def delete():

  # Clear session
  session.clear()
  
  # Redirect to root
  return redirect('/')

# Checking name
if __name__ == '__main__':
  # Running app
  app.run(debug=True)