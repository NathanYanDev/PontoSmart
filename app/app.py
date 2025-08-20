from config import Base, engine
from models import User
from models import Attendance
from models import ImageData

from flask import Flask, render_template, request, redirect

Base.metadata.create_all(bind=engine)

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