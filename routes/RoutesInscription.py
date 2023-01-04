from flask import jsonify
from flask import request
from flask import Blueprint
from Controllers.InscriptionController import InscriptionController

myControllerInscription = InscriptionController()

routeGetInscriptions=Blueprint("routeGetInscriptions",__name__)
routeGetInscription=Blueprint("routeGetInscription",__name__)
routeCreateInscription=Blueprint("routeCreateInscription",__name__)
routeUpdateInscripcion=Blueprint("routeUpdateInscripcion",__name__)
routeDeleteInscription=Blueprint("routeDeleteInscription",__name__)
routeGetListInscribedInCourse=Blueprint("routeGetListInscribedInCourse",__name__)
routeGetGreaterValue=Blueprint("routeGetGreaterValue",__name__)
routeGetAVGCourse=Blueprint("routeGetAVGCourse",__name__)

@routeGetInscriptions.route("/inscripciones",methods=['GET'])
def getInscriptions():
    json=myControllerInscription.index()
    return jsonify(json)

@routeGetInscription.route("/inscripcion/<string:id>",methods=['GET'])
def getInscription(id):
    json=myControllerInscription.show(id)
    return jsonify(json)

@routeCreateInscription.route("/inscripcion/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['POST'])
def createInscription(id_estudiante,id_materia):
    data = request.get_json()
    json=myControllerInscription.create(data,id_estudiante,id_materia)
    return jsonify(json)

@routeUpdateInscripcion.route("/inscripciones/<string:id_inscripcion>/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['PUT'])
def updateInscripcion(id_inscripcion,id_estudiante,id_materia):
    data = request.get_json()
    json=myControllerInscription.update(id_inscripcion,data,id_estudiante,id_materia)
    return jsonify(json)

@routeDeleteInscription.route("/inscripcion/<string:id>",methods=['DELETE'])
def deleteInscription(id):
    json=myControllerInscription.delete(id)
    return jsonify(json)

@routeGetListInscribedInCourse.route("/inscripcion/materias/<string:idMaterias>",methods=['GET'])
def getListInscribedInCourse(idMaterias):
    json=myControllerInscription.listInscribedInCourse(idMaterias)
    return jsonify(json)

@routeGetGreaterValue.route("/inscripcion/nota_mayor_por_curso",methods=['GET'])
def getGreaterValue():
    json=myControllerInscription.greaterValueForCourse()
    return jsonify(json)

@routeGetAVGCourse.route("/inscripcion/promedio_por_materia/<string:idMaterias>",methods=['GET'])
def getAVGCourse(idMaterias):
    json=myControllerInscription.AvgCourse(idMaterias)
    return jsonify(json)