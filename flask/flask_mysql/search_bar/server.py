from flask import Flask, render_template, redirect, request, session, flash 
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = 'asdf'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/username', methods=['POST'])
def username():
  found = False
  sql = connectToMySQL('username')
  
  query = 'SELECT username FROM users WHERE users.username = %(username)s;'
  data = {'username': request.form['username']}
  result = sql.query_db(query, data)
  if result: 
    found = True
  print(found)
  return render_template('/partials/username.html', found=found)

@app.route("/usersearch", methods=['GET','POST'])
def search():
    mysql = connectToMySQL("username")
    query = "SELECT * FROM users WHERE username LIKE %%(name)s;"
    data = {
        "name" : request.args.get('name')  + '%' # get our data from the query string in the url
    }
    results = mysql.query_db(query, data)
    return render_template("/partials/usersearch.html", users = results) # render a template which uses the results

@app.errorhandler(404)
def something_went_worng(e):
  return "Page not found"

if __name__ == '__main__':
  app.run(debug=True)