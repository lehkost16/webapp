import pymysql
from flask import Flask, jsonify, abort

app = Flask(__name__)

conn =pymysql.connect(host='flask_mysql',port=3306,database='t_d',user='root',password='1201',charset='utf8')
cursor =conn.cursor()


@app.route('/kingdom/api/v1.0/person', methods=['get'])
def get_persons():
    cursor.execute('select * from person')
    for person in cursor.fetchall():
        return person
    return

@app.route('/todo/api/v1.0/tasks/<int:person_id>', methods=['POST'])
def get_task(person_id):
    return

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)