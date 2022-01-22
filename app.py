from flask import Flask,jsonify,request
import pymysql 

def db_connector():
    db = pymysql.connect(host='127.0.0.1', user='root', password='12345678', charset='utf8',db='demo')
    cursor = db.cursor()
    sql = '''SELECT * FROM visits;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return str(result)




app = Flask(__name__)


@app.route('/')
def index():
    return db_connector()

if __name__ == '__main__':
    app.run(debug=True)