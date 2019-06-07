from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/success')
def success():
  return 'success'

@app.route('/<name>/<times>')
def hello(name,times):
  return render_template('hello.html', some_name=name,num_times=int(times))

if __name__ == '__main__':
  app.run(debug=True)