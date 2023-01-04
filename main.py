from flask import Flask
from flask import jsonify
from flask import request
#Cors para hacer comunicacion cruzada entre diferentes herramientas 
from flask_cors import CORS
import json
from waitress import serve
#Se importan los controladores si las rutas se encuentran en el archivo main 
#from Controllers.CourseController import CourseController
#from Controllers.DepartmentController import DepartmentController
#from Controllers.InscriptionController import InscriptionController
#from Controllers.StudentController import StudentController


#importar los archivos de rutas
from routes.RoutesStudent import *
from routes.RoutesDepartment import *
from routes.RoutesCourse import *
from routes.RoutesInscription import *


app = Flask(__name__)
cors = CORS(app)

#se crea una instancia de los controladores
#myControllerCourse = CourseController()
#myControllerDepartment = DepartmentController()
#myControllerInscription = InscriptionController()
#myControllerStudents = StudentController()


@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

#################################### Rutas Estudiantes #####################################
app.register_blueprint(routeGetStudents)#libreria Blueprint para comunicar rutas de un archivo a otro
app.register_blueprint(routeCreateStudent)
app.register_blueprint(routeGetStudent)
app.register_blueprint(routeUpdateStudent)
app.register_blueprint(routeDeleteStudent)
############################################################################################

############################# Rutas Departamentos ##########################################
app.register_blueprint(routeGetDepartments)
app.register_blueprint(routeCreateDepartment)
app.register_blueprint(routeGetDepartment)
app.register_blueprint(routeUpdateDepartment)
app.register_blueprint(routeDeleteDepartment)
############################################################################################

####################################### Rutas Materias #####################################
app.register_blueprint(routeGetCourses)
app.register_blueprint(routeCreateCourse)
app.register_blueprint(routeGetCourse)
app.register_blueprint(routeUpdateCourse)
app.register_blueprint(routeDeleteCourse)
############################################################################################

############################# Rutas Departamentos-Materias [1:n] ###########################
app.register_blueprint(routeAssignDepartmentToCourse)
############################################################################################

############################# Rutas Inscripciones relacion [n:n] ###########################
app.register_blueprint(routeGetInscriptions)
app.register_blueprint(routeGetInscription)
app.register_blueprint(routeCreateInscription)
app.register_blueprint(routeUpdateInscripcion)
app.register_blueprint(routeDeleteInscription)
app.register_blueprint(routeGetListInscribedInCourse)
app.register_blueprint(routeGetGreaterValue)
app.register_blueprint(routeGetAVGCourse)
############################################################################################

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data 

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])