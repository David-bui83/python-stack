from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', n_row=8, n_col=8)

@app.route('/<num>')
def index2(num):
  return render_template('index.html', n_row=8, n_col=int(num))

@app.route('/<num1>/<num2>')
def index3(num1,num2):
  return render_template('index.html', n_row=int(num1),n_col=int(num2))

@app.route('/<num1>/<num2>/<cc1>/<cc2>')
def index4(num1,num2,cc1,cc2):
  return render_template('index.html', n_row=int(num1), n_col=int(num2), c1=cc1, c2=cc2)

@app.errorhandler(404)
def something_is_worng(e):
  return 'Page not found'

if __name__ == '__main__':
  app.run(debug=True)