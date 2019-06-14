from flask import Flask, session, redirect, render_template, flash, request
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = 'asdfas'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
  if not EMAIL_REGEX.match(request.form["email"]):
    flash("<h1 class='bg-danger text-center text-light'>Email is not valid!</h1>")
    return redirect('/')
  sql = connectToMySQL('email_validation')
  emails = sql.query_db('SELECT email FROM emails')

  # check is database is empty
  if len(emails) < 1:
    data = {
      'email': request.form['email']
    }

    sql = connectToMySQL('email_validation')
    query = 'INSERT INTO emails(email) VALUES(%(email)s);'
    email_id = sql.query_db(query,data)
    session['email_id'] = email_id
  # check if email exist
  else: 
    for email in emails:
      if request.form['email'] == email['email']:
        flash("<h1 class='bg-danger text-center text-light'>Email already in use!</h1>")
        return redirect('/')

    data = {
      'email': request.form['email']
    }

    sql = connectToMySQL('email_validation')
    query = 'INSERT INTO emails(email) VALUES(%(email)s);'
    email_id = sql.query_db(query,data)
    session['email_id'] = email_id

  return redirect('/success')

@app.route('/success')
def success():
  # getting singl email
  sql = connectToMySQL('email_validation')
  email_address = sql.query_db(f"SELECT email FROM emails where id={session['email_id']}")

  # check if email is in database
  if email_address:
    flash(f"The email address you entered {email_address[0]['email']} is a VALID email address! Thank you!")

  # getting all emails
  sql = connectToMySQL('email_validation')
  emails = sql.query_db('SELECT * FROM emails')

  return render_template('success.html',emails=emails)

@app.route('/delete/<email_id>')
def delete_email(email_id):
  print('from delete' + str(email_id))
  data = {
    'id': email_id
  }
  query = 'DELETE FROM emails where id=%(id)s'
  sql = connectToMySQL('email_validation')
  sql.query_db(query, data)

  return redirect('/success')

if __name__ == '__main__':
  app.run(debug=True)
