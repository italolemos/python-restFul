"""
GET /tasks - display all tasks
POST /tasks - create a new task
PUT /tasks/(id) - update a task by ID
DELETE /tasks/(id) - delete a task by ID
"""
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

# Connectung to SQLite3

e = create_engine('sqlite:///salaries.db')

app = Flask(__name__)
api = Api(app)


class Departments_Meta(Resource):
    def get(self):
        # connect to database
        conn = e.connect()
        # query and return JSON data
        query = conn.execute("select distinct DEPARTMENT from salaries")
        print(query.cursor.fetchall())
        return {'departmets': [i[0] for i in query.cursor.fetchall()]}


class Departamental_Salary(Resource):
    def get(self, department_name):
        conn = e.connect()
        query = conn.execute("select * from salaries where Department='%s'" % department_name.upper())
        # query the result and get cursos.Dumping that data to a JSON
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return result

api.add_resource(Departamental_Salary, '/dept/<string:department_name>')
api.add_resource(Departments_Meta, '/departments')

if __name__ == '__main__':
    app.run()
