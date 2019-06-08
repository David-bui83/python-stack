from flask import Flask, render_template, request
from sub.checkinput import checkForEmpty
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
  users = []

  in_dic = {
    "first_name": '',
    "last_name": '',
    'email': '',
    'check1': '',
    'check2': '',
    'check3': '',
    'check4': '',
    'online': '', 
    'comments': ''
  }
  
  f_name = request.form.get('first_name')
  in_dic['first_name'] = checkForEmpty(f_name)

  l_name = request.form.get('last_name')
  in_dic['last_name'] = checkForEmpty(l_name)

  email = request.form.get('email')
  in_dic['email'] = checkForEmpty(email)

  check1 = request.form.get('check1')
  in_dic['check1'] = checkForEmpty(check1)

  check2 = request.form.get('check2')
  in_dic['check2'] = checkForEmpty(check2)

  check3 = request.form.get('check3')
  in_dic['check3'] = checkForEmpty(check3)

  check4 = request.form.get('check4')
  in_dic['check4'] = checkForEmpty(check4)

  online = request.form.get('online')
  in_dic['online'] = checkForEmpty(online)

  comments = request.form.get('comments')
  in_dic['comments'] = checkForEmpty(comments)
  
  users.append(in_dic)

  return render_template('result.html', users = users)

@app.route('/return', methods=['GET'])
def backToIndex():
  return render_template('index.html')

@app.errorhandler(404)
def something_is_worng(e):
  return 'Page not found'

if __name__ == '__main__':
  app.run(debug=True)
