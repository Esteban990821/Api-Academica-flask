from flask import jsonify
from flask import request
from flask import Blueprint
from Controllers.StudentController import StudentController

myControllerStudents = StudentController()

routeGetStudents=Blueprint("routeGetStudents",__name__)
routeCreateStudent=Blueprint("routeCreateStudent",__name__)
routeGetStudent=Blueprint("routeGetStudent",__name__)
routeUpdateStudent=Blueprint("routeUpdateStudent",__name__)
routeDeleteStudent=Blueprint("routeDeleteStudent",__name__)


@routeGetStudents.route("/students",methods=['GET'])
def getEstudiantes():
    json = myControllerStudents.index()
    return jsonify(json)

@routeCreateStudent.route("/students",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json = myControllerStudents.create(data)
    return jsonify(json)

@routeGetStudent.route("/students/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=myControllerStudents.show(id)
    return jsonify(json)

@routeUpdateStudent.route("/students/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json=myControllerStudents.update(id,data)
    return jsonify(json)

@routeDeleteStudent.route("/students/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json=myControllerStudents.delete(id)
    return jsonify(json)