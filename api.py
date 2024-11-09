from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restx import Api, Resource, fields  # Используем Flask-RESTX
from models import db, Employee
from database import create_app

app = create_app()
CORS(app) 

api = Api(app, version='1.0', title='Employee API',
          description='An API to manage employees in an IT company')

ns = api.namespace('employees', description='Operations related to employees')

employee_model = ...

@ns.route('/')
class EmployeeList(Resource):
    @ns.doc('list_employees')
    @ns.marshal_list_with(employee_model)
    def get(self):
        """Получить всех сотрудников"""
        employees = Employee.query.all()
        return employees
....

@ns.route('/<int:id>')
@ns.response(404, 'Employee not found')
@ns.param('id', 'The employee identifier')
class EmployeeResource(Resource):
    @ns.doc('get_employee')
    @ns.marshal_with(employee_model)
    def get(self, id):
        """Получить сотрудника по ID"""
        employee = Employee.query.get_or_404(id)
        return employee
....

if __name__ == '__main__':
    app.run(port="5001", debug=True)
