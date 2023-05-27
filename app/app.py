import mysql
from flask import Flask, jsonify
from mysql import connector

app = Flask(__name__)

config = {
        'user': 'root',
        'password': '1201',
        'host': '172.26.28.185',
        'port': '3306',
        'database': 'database'
    }
connection = mysql.connector.connect(**config)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk.Chess,Pizza,Fruit,Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['get'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == "__main__":
    app.run(debug=True,host='http://172.26.28.185',port=5000)