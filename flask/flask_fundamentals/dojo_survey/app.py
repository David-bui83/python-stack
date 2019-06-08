from flask import Flask, render_template, request
from sub.checkinput import checkForEmpty
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
  
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
  users = [in_dic]

  f_name = request.form.get('first_name')
  in_dic['first_name'] = checkForEmpty(f_name)

  l_name = request.form.get('last_name')
  in_dic['last_name'] = checkForEmpty(l_name)
  # if f_name:
  #   in_dic['last_name'] = l_name
  # else:
  #   in_dic['last_name'] = False

  email = request.form.get('email')
  in_dic['email'] = checkForEmpty(email)
  # if f_name:
  #   in_dic['email'] = email
  # else:
  #   in_dic['email'] = False

  check1 = request.form.get('check1')
  in_dic['check1'] = checkForEmpty(check1)
  # if check1:
  #   in_dic['check1'] = check1
  # else: 
  #   in_dic['check1'] = False

  check2 = request.form.get('check2')
  in_dic['check2'] = checkForEmpty(check2)
  # if check2:
  #   in_dic['check2'] = check2
  # else: 
  #   in_dic['check2'] = False

  check3 = request.form.get('check3')
  in_dic['check3'] = checkForEmpty(check3)
  # if check3:
  #   in_dic['check3'] = check3
  # else: 
  #   in_dic['check3'] = False

  check4 = request.form.get('check4')
  in_dic['check4'] = checkForEmpty(check4)
  # if check4:
  #   in_dic['check4'] = check4
  # else: 
  #   in_dic['check4'] = False

  online = request.form.get('online')
  in_dic['online'] = checkForEmpty(online)
  # if online:
  #   in_dic['online'] = online
  # else: 
  #   in_dic['online'] = False

  # if in_person:
  #   in_dic['in_person'] = in_person
  # else: 
  #   in_dic['in_person'] = False

  comments = request.form.get('comments')
  in_dic['comments'] = checkForEmpty(comments)
  # if comments:
  #   in_dic['comments'] = comments
  # else: 
  #   in_dic['comments'] = False

  return render_template('result.html', users = users)

@app.errorhandler(404)
def something_is_worng(e):
  return 'Page not found'

if __name__ == '__main__':
  app.run(debug=True)
