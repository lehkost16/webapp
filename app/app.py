from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
    }
connection = pymysql.connect(**config)


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
    app.run(debug=True,host='http://172.26.28.185')
