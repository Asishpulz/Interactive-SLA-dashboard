from flask import Flask,render_template
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def hello_world():
   return render_template("home.html")
@app.route('/line')
def line_data():
   return render_template("linegraph.html")

if __name__ == '__main__':
   app.run(debug=True)