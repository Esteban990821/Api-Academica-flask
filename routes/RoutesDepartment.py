from flask import jsonify
from flask import request
from flask import Blueprint
from Controllers.DepartmentController import DepartmentController

myControllerDepartment = DepartmentController()

routeGetDepartments=Blueprint("routeGetDepartments",__name__)
routeCreateDepartment=Blueprint("routeCreateDepartment",__name__)
routeGetDepartment=Blueprint("routeGetDepartment",__name__)
routeUpdateDepartment=Blueprint("routeUpdateDepartment",__name__)
routeDeleteDepartment=Blueprint("routeDeleteDepartment",__name__)


@routeGetDepartments.route("/department",methods=['GET'])
def getDepartments():
    json = myControllerDepartment.index()
    return jsonify(json)

@routeCreateDepartment.route("/department",methods=['POST'])
def createDepartment():
    data = request.get_json()
    json = myControllerDepartment.create(data)
    return jsonify(json)

@routeGetDepartment.route("/department/<string:id>",methods=['GET'])
def getDepartment(id):
    json=myControllerDepartment.show(id)
    return jsonify(json)

@routeUpdateDepartment.route("/department/<string:id>",methods=['PUT'])
def updateDepartment(id):
    data = request.get_json()
    json=myControllerDepartment.update(id,data)
    return jsonify(json)

@routeDeleteDepartment.route("/department/<string:id>",methods=['DELETE'])
def deleteDepartment(id):
    json=myControllerDepartment.delete(id)
    return jsonify(json)