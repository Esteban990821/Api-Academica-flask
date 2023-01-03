from Repositories.CourseRep import CourseRep
from Repositories.DepartmentsRep import DepartmentsRep
from Models.Course import Course
from Models.Departments import Departments

class CourseController():
    def __init__(self):
        self.courseRep = CourseRep()
        self.departmentRep = DepartmentsRep()
   
    def index(self):
        return self.courseRep.findAll()
        

    def create(self,courseInfo):
        newCourse=Course(courseInfo)
        return self.courseRep.save(newCourse)

    def show(self,id):
        theCourse =Course(self.courseRep.findById(id))
        return theCourse.__dict__

    def update(self,id,courseInfo):
        currentCourse = Course(self.courseRep.findById(id))
        currentCourse.nombre = courseInfo["nombre"]
        currentCourse.creditos = courseInfo["creditos"]
        return self.courseRep.save(currentCourse)

    def delete(self,id):
        return self.courseRep.delete(id)

    def assignmentDepartment(self,id,idDepartment):
        currentCourse = Course(self.courseRep.findById(id))
        currentDepartment = Departments(self.departmentRep.findById(idDepartment))
        currentCourse.departamento = currentDepartment
        return self.courseRep.save(currentCourse)
