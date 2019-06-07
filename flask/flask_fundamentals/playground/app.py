from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/play')
def play():
  return render_template('play.html',num_boxes=3)

@app.route('/play/<num>')
def play1(num):
  return render_template('play.html', num_boxes=int(num))
@app.route('/play/<num>/<color>')
def play2(num, color):
  return render_template('play.html', num_boxes=int(num), box_color=color)

@app.errorhandler(404)
def page_not_found(e):
  return 'Page not found'

if __name__ == "__main__":
    app.run(debug=True)