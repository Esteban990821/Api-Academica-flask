from flask import Flask
from flask import jsonify
from flask import request
#Cors para hacer comunicacion cruzada entre diferentes herramientas 
from flask_cors import CORS
import json
from waitress import serve
from Controllers.StudentController import StudentController
from Controllers.CourseController import CourseController
from Controllers.DepartmentController import DepartmentController
from Controllers.InscriptionController import InscriptionController

app = Flask(__name__)
cors = CORS(app)

myControllerStudents = StudentController()
myControllerCourse = CourseController()
myControllerDepartment = DepartmentController()
myControllerInscription = InscriptionController()

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

#################################### Rutas Estudiantes #####################################
@app.route("/students",methods=['GET'])
def getEstudiantes():
    json = myControllerStudents.index()
    return jsonify(json)

@app.route("/students",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json = myControllerStudents.create(data)
    return jsonify(json)

@app.route("/students/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=myControllerStudents.show(id)
    return jsonify(json)
#leer configuracion del puerto y url

@app.route("/students/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json=myControllerStudents.update(id,data)
    return jsonify(json)

@app.route("/students/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json=myControllerStudents.delete(id)
    return jsonify(json)
############################################################################################

############################# Rutas Departamentos ##########################################
@app.route("/department",methods=['GET'])
def getDepartments():
    json = myControllerDepartment.index()
    return jsonify(json)

@app.route("/department",methods=['POST'])
def createDepartment():
    data = request.get_json()
    json = myControllerDepartment.create(data)
    return jsonify(json)

@app.route("/department/<string:id>",methods=['GET'])
def getDepartment(id):
    json=myControllerDepartment.show(id)
    return jsonify(json)

@app.route("/department/<string:id>",methods=['PUT'])
def updateDepartment(id):
    data = request.get_json()
    json=myControllerDepartment.update(id,data)
    return jsonify(json)

@app.route("/department/<string:id>",methods=['DELETE'])
def deleteDepartment(id):
    json=myControllerDepartment.delete(id)
    return jsonify(json)
############################################################################################

####################################### Rutas Materias #####################################
@app.route("/course",methods=['GET'])
def getCourses():
    json = myControllerCourse.index()
    return jsonify(json)

@app.route("/course",methods=['POST'])
def createCourse():
    data = request.get_json()
    json = myControllerCourse.create(data)
    return jsonify(json)

@app.route("/course/<string:id>",methods=['GET'])
def getCourse(id):
    json=myControllerCourse.show(id)
    return jsonify(json)

@app.route("/course/<string:id>",methods=['PUT'])
def updateCourse(id):
    data = request.get_json()
    json=myControllerCourse.update(id,data)
    return jsonify(json)

@app.route("/course/<string:id>",methods=['DELETE'])
def deleteCourse(id):
    json=myControllerCourse.delete(id)
    return jsonify(json)
############################################################################################

############################# Rutas Departamentos-Materias #################################
@app.route("/course/<string:id>/departamento/<string:idDepartment>",methods=['PUT'])
def asignarDepartamentoAMateria(id,idDepartment):
    json = myControllerCourse.assignmentDepartment(id,idDepartment)
    return jsonify(json)
############################################################################################

############################# Rutas Inscripciones relacion [n:n] #################################
@app.route("/inscripciones",methods=['GET'])
def getInscriptions():
    json=myControllerInscription.index()
    return jsonify(json)

@app.route("/inscripcion/<string:id>",methods=['GET'])
def getInscription(id):
    json=myControllerInscription.show(id)
    return jsonify(json)

@app.route("/inscripcion/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['POST'])
def createInscription(id_estudiante,id_materia):
    data = request.get_json()
    json=myControllerInscription.create(data,id_estudiante,id_materia)
    return jsonify(json)

@app.route("/inscripciones/<string:id_inscripcion>/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['PUT'])
def updateInscripcion(id_inscripcion,id_estudiante,id_materia):
    data = request.get_json()
    json=myControllerInscription.update(id_inscripcion,data,id_estudiante,id_materia)
    return jsonify(json)

@app.route("/inscripcion/<string:id>",methods=['DELETE'])
def deleteInscription(id):
    json=myControllerInscription.delete(id)
    return jsonify(json)
############################################################################################

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data 

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])