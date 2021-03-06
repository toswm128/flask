from flask import Flask,jsonify,request
import pymysql 
from flask_cors import CORS

def db_connector():
    db = pymysql.connect(host='127.0.0.1', user='root', password='12345678', charset='utf8',db='demo')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = '''SELECT * FROM visits;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return result

def db_insert(name):
    db = pymysql.connect(host='127.0.0.1', user='root', password='12345678', charset='utf8',db='demo')
    cursor = db.cursor()
    sql = '''INSERT INTO visits VALUES(Null,'%s')'''% name
    cursor.execute(sql)
    result = cursor.fetchall()
    db.commit()
    db.close()
    return result




app = Flask(__name__)

CORS(app)


@app.route('/',methods=["GET","POST"])
def index():
    if request.method == 'GET':
        return jsonify({'result':'success','data': db_connector(),'msg': '이 요청은 GET!'})
    if request.method == "POST":
        value = request.json
        db_insert(value["text"])
        return jsonify({'result':'success','data': value,'msg': '이 요청은 POST'})

if __name__ == '__main__':
    app.run(debug=True)