from Models.Students import Students

class StudentController():
    def __init__(self):
        print("Creando Controlador de estudiante")
   
    def index(self):
        print("Listar todos los estudiantes")
        oneStudent = {
            "_id":"1",
            "cedula":"123456",
            "nombre":"Esteban",
            "apellido":"Rodriquez"
        }
        return [oneStudent]

    def create(self,studentInfo):
        print("Crear un estudiante")
        theStudent = Students(studentInfo)
        return theStudent.__dict__

    def show(self,id):
        print("Mostrando un estudiante con id ",id)
        theStudent = {
            "_id":id,
            "cedula":"123456",
            "nombre":"Esteban",
            "apellido":"Rodriquez"
        }
        return theStudent

    def update(self,id,studentInfo):
        print("Actualizando estudiante con id ",id)
        theStudent = Students(studentInfo)
        return theStudent.__dict__

    def delete(self,id):
        print("Elimiando estudiante con id ",id)
        return{"deleted_count":id}