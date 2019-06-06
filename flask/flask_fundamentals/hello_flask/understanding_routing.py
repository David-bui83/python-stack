from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello world'

@app.route('/dojo')
def dojo():
  return 'Dojo!'

@app.route('/say/<name>')
def say(name):
  print(name)
  return f'Hello {name}!'

@app.route('/repeat/<num>/<name>')
def repeat(num, name):
  return f'{name}' * int(num)


@app.errorhandler(404)
def page_not_found(e):
  return 'Sorry! No response. Try again later'

if __name__ == '__main__':
  app.run(debug=True)