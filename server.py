from flask import Flask
from flask import jsonify
from flask import Response
import MySQLdb

app = Flask(__name__)

db = MySQLdb.connect(host="watering.cx44b8lvz89x.eu-central-1.rds.amazonaws.com",    # your host, usually localhost
                     user="frontend",         # your username
                     passwd="pipipipi",  # your password
                     db="watering")  

cur = db.cursor()   


@app.route('/not_much')
def hello_world():
    return 'not much to see here'

@app.route('/', methods=['GET'])
def metrics():  # pragma: no cover
#    content = get_file('index.html')
    content = open("index.html").read()
    return Response(content, mimetype="text/html")

@app.route('/weather')
def weather():
    cur.execute("SELECT * FROM  weather ORDER BY weather.id DESC LIMIT 0 , 100")
    j = jsonify(cur.fetchall())
    return j

@app.route('/weather/<parameter>')
def weather_with_param(parameter="*"):
    cur.execute("SELECT "+ parameter +" FROM  weather ORDER BY weather.id DESC LIMIT 0 , 100")
    j = jsonify(cur.fetchall())
    return j
