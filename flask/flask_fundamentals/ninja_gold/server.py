from flask import Flask, render_template, request, session, redirect
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
  if not 'gold' in session:
    session['gold'] = 0
    
    
  total_gold = session['gold']
  return render_template('index.html', total_gold=total_gold)

@app.route('/gold', methods=['POST'])
def gold():
  if not 'messages' in session:
    session['messages'] = []

  building = {
    'farm': (10,20),
    'cave': (5,10),
    'house': (2,5),
    'casino':(-50,50)
  }
 
  gold_amount = random.randint(building[request.form['name']][0], building[request.form['name']][1])
  now = datetime.time(datetime.now())
  
  if gold_amount < 0:
    str_out = f"<p class='red'>Entered a {request.form['name']} and lost {gold_amount}! ({now})</p>"
    # session['color'] = 'red'
    session['gold'] -= gold_amount
  else:
    str_out = f"<p class='green'>Earned {gold_amount} golds from the {request.form['name']}! ({now}) </p>"
    # session['color'] = 'green'
    session['gold'] += gold_amount

  session['messages'].append(str_out)


  print(gold_amount)
  print(session['messages'])
  return redirect('/')

@app.route('/clear')
def clearSession():
  session.clear()
  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)