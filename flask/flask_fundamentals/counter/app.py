from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'super'

@app.route('/')
def index():
  
  if not 'visited' in session:
    session['visited'] = 0
    session['clicked'] = 0
  else:
    session['visited'] += 1

  return render_template('index.html')



@app.route('/clicked')
def show():
  if not 'clicked' in session:
    session['clicked'] = 0
    session['visited'] -=1
  else:
    session['clicked'] += 2
    session['visited'] -=1
  return redirect('/')

@app.route('/reset')
def delete():
  session.clear()
  return redirect('/')

@app.route('/add_input', methods=['POST'])
def addInput():
 
  var = request.form.get('number')
  if var:
    session['clicked'] += int(var) + 1
    session['clicked'] -= 1
    session['visited'] -= 1 
  else:
    session['visited'] -= 1

  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)