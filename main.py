from flask import Flask
from flask import jsonify
from flask import request
#Cors para hacer comunicacion cruzada entre diferentes herramientas 
from flask_cors import CORS
import json
from waitress import serve
from Controllers.StudentController import StudentController

app = Flask(__name__)
cors = CORS(app)

myControllerStudents = StudentController()

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

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

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data 

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])