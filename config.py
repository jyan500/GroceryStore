from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_wtf.csrf import CSRFError
from datetime import datetime
import os
from dotenv import load_dotenv
import sys

## configurations
# config = yaml.load(open('config.yaml'))

## load env file
load_dotenv(verbose = True)
app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

#### global variables ####
mysql = MySQL()

mysql.init_app(app)

## register csrf protection
csrf = CSRFProtect(app)

from home import home_controller

app.register_blueprint(home_controller)

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('404.html')