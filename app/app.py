from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('clock-in.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
      # Process the form data
      return redirect('/')
  return render_template('register.html')

@app.route('/registrar_ponto', methods=['POST'])
def clock_in():
  pass