from flask import Flask, render_template, request, redirect
# from cs50 import SQL

app = Flask(__name__)

REGISTRANTS = {}
# db = SQL("sqlite:///froshims.db")

SPORTS = [
  'Baseball',
  'Frisbee',
  'Soccer'
]

# @app.route('/', methods=['GET', 'POST'])
# def greet():
#     if request.method == 'POST':
#       name = request.form.get('name')
#       return render_template('greet.html', name=name)
    
#     return render_template('index.html')

@app.route('/')
def index():
  return render_template('index.html', sports=SPORTS)

@app.route('/register', methods=['POST'])
def register():
  if not request.form.get('name'):
    return render_template('failure.html')
  if not request.form.get('sport') or request.form.get('sport') not in SPORTS:
    return render_template('failure.html')
    
  REGISTRANTS[request.form.get('name')] = request.form.get('sport')
  
  # use db 
  # db.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", name=request.form.get('name'), sport=request.form.get('sport'))
  
  return redirect('/registrants')

@app.route('/registrants')
def registrants():
  # registrants = db.execute("SELECT * FROM registrants")

  return render_template('registrants.html', registrants=REGISTRANTS)