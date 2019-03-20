from config import mysql
from extensions import *
home_controller = Blueprint('home_controller', __name__)
@home_controller.route("/", methods = ['GET'])
def index():
	return render_template('index.html')