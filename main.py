from flask import Flask, render_template

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page (now using the index.html file)
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/Names')
def lijst_template():
  Names = ['Heinrich', 'Bock', 'Jos', 'Manstein']
  return render_template('Usernames.html', Names=Names)

@app.route('/Login')
def login():
  return render_template('Login.html')

@app.route('/Schutzstaffel')
def Schutzstaffel():
  return render_template('Schutzstaffel.html')

@app.route('/Signup')
def Signup():
  return render_template('Signup.html')

@app.route('/Start')
def Start():
  return render_template('Start.html')

if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )