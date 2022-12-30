from Models.Students import Students
from Repositories.StudentRep import StudentRep
class StudentController():
    def __init__(self):
        self.studentRep = StudentRep()
   
    def index(self):
        return self.studentRep.findAll()
        

    def create(self,studentInfo):
        newStudent=Students(studentInfo)
        return self.studentRep.save(newStudent)

    def show(self,id):
        theStudent =Students(self.studentRep.findById(id))
        return theStudent.__dict__

    def update(self,id,studentInfo):
        currentStudent = Students(self.studentRep.findById(id))
        currentStudent.cedula = studentInfo["cedula"]
        currentStudent.nombre = studentInfo["nombre"]
        currentStudent.apellido = studentInfo["apellido"]
        return self.studentRep.save(currentStudent)

    def delete(self,id):
        return self.studentRep.delete(id)