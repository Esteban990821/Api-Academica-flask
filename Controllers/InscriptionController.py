from Repositories.InscriptionRep import InscriptionRep
from Repositories.StudentRep import StudentRep
from Repositories.CourseRep import CourseRep
from Models.Course import Course
from Models.Students import Students
from Models.Inscription import Inscription

class InscriptionController():
    def __init__(self):
        self.studentRep = StudentRep()
        self.courseRep = CourseRep()
        self.inscriptionRep = InscriptionRep()
    def index(self):
        return self.inscriptionRep.findAll()

    #Asignacion estudiante y materia a inscripción
    def create(self,inscriptionInfo,idStudent,idCourse):
        newInscription = Inscription(inscriptionInfo)
        theStudent = Students(self.studentRep.findById(idStudent))
        theCourse = Course(self.courseRep.findById(idCourse))
        newInscription.estudiante = theStudent
        newInscription.materia = theCourse
        return self.inscriptionRep.save(newInscription)
    
    def show(self,id):
        theInscription = Inscription(self.inscriptionRep.findById(id))
        return theInscription.__dict__
    
    #Modificación de inscripción (estudiante y materia)
    def update(self,id,inscriptionInfo,idStudent,idCourse):
        theInscription = Inscription(self.inscriptionRep.findById(id))
        theInscription.year = inscriptionInfo["year"]
        theInscription.semestre = inscriptionInfo["semestre"]
        theInscription.nota_final = inscriptionInfo["nota_final"]
        theStudent = Students(self.studentRep.findById(idStudent))
        theCourse = Course(self.courseRep.findById(idCourse))
        theInscription.estudiante = theStudent
        theInscription.materia = theCourse
        return self.inscriptionRep.save(theInscription)
    
    def delete(self,id):
        return self.inscriptionRep.delete(id)




    
