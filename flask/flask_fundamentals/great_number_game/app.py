from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secret key'


@app.route('/')
def index():
  session['randNum']= random.randint(1,100)
  session['visible'] = 'none'
  session['attempts'] = 0
  return render_template('index.html')

@app.route('/greater')
def greater():
  session['visible'] = 'block'
  session['bg'] = 'red'
  session['wrong'] = 'Too High'
  session['can_see'] = 'none'
  session['attempt-msg'] = 'You have taken ' + str(session['attempts']) + ' out of 5.'
  print('greater')
  return render_template('index.html')

@app.route('/less')
def less():
  session['visible'] = 'block'
  session['bg'] = 'red'
  session['wrong'] = 'Too Low'
  session['can_see'] = 'none'
  session['attempt-msg'] = 'You have taken ' + str(session['attempts']) + ' out of 5.'
  print('less')
  return render_template('index.html')

@app.route('/winner')
def winner():
  session['visible'] = 'block'
  session['bg'] = 'green'
  session['wrong'] = 'Winner'
  session['attempt-msg'] = 'You took ' + str(session['attempts']) + ' out of 5 attempts.'
  session['can_see'] = 'inline'
  print('winner')
  return render_template('index.html')

@app.route('/loss')
def loss():
  print('loss')
  session['bg'] = '#333'
  session['wrong'] = 'Game Over'
  session['attempt-msg'] = 'You have taken ' + str(session['attempts']) + ' out of 5.'
  session['can_see'] = 'inline'
  return render_template('index.html')

@app.route('/again')
def again():
  session.clear()
  return redirect('/')

@app.route('/guess', methods=['POST'])
def guess():
  session['user_guess'] = request.form.get('user_guess')
  session['attempts'] += 1
  if session['attempts'] < 5:
    if int(session['user_guess']) > session['randNum']:  
      return redirect('/greater')
    elif int(session['user_guess']) < session['randNum']:
      return redirect('/less')
    else:
      return redirect('/winner')
  else:
    return redirect('/loss')

  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)