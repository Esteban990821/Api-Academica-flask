from flask import jsonify
from flask import request
from flask import Blueprint
from Controllers.CourseController import CourseController

myControllerCourse = CourseController()

routeGetCourses=Blueprint("routeGetCourses",__name__)
routeCreateCourse=Blueprint("routeCreateCourse",__name__)
routeGetCourse=Blueprint("routeGetCourse",__name__)
routeUpdateCourse=Blueprint("routeUpdateCourse",__name__)
routeDeleteCourse=Blueprint("routeDeleteCourse",__name__)
routeAssignDepartmentToCourse=Blueprint("routeAssignDepartmentToCourse",__name__)


@routeGetCourses.route("/course",methods=['GET'])
def getCourses():
    json = myControllerCourse.index()
    return jsonify(json)

@routeCreateCourse.route("/course",methods=['POST'])
def createCourse():
    data = request.get_json()
    json = myControllerCourse.create(data)
    return jsonify(json)

@routeGetCourse.route("/course/<string:id>",methods=['GET'])
def getCourse(id):
    json=myControllerCourse.show(id)
    return jsonify(json)

@routeUpdateCourse.route("/course/<string:id>",methods=['PUT'])
def updateCourse(id):
    data = request.get_json()
    json=myControllerCourse.update(id,data)
    return jsonify(json)

@routeDeleteCourse.route("/course/<string:id>",methods=['DELETE'])
def deleteCourse(id):
    json=myControllerCourse.delete(id)
    return jsonify(json)

############################# Rutas Departamentos-Materias [1:n] #################################
@routeAssignDepartmentToCourse.route("/course/<string:id>/departamento/<string:idDepartment>",methods=['PUT'])
def assignDepartmentToCourse(id,idDepartment):
    json = myControllerCourse.assignmentDepartment(id,idDepartment)
    return jsonify(json)