from Repositories.DepartmentsRep import DepartmentsRep
from Models.Departments import Departments

class DepartmentController():
    def __init__(self):
        self.departmentRep = DepartmentsRep()
   
    def index(self):
        return self.departmentRep.findAll()
        

    def create(self,departmentInfo):
        newDepartment=Departments(departmentInfo)
        return self.departmentRep.save(newDepartment)

    def show(self,id):
        theDepartment =Departments(self.departmentRep.findById(id))
        return theDepartment.__dict__

    def update(self,id,departmentInfo):
        currentDepartment = Departments(self.departmentRep.findById(id))
        currentDepartment.nombre = departmentInfo["nombre"]
        currentDepartment.descripcion = departmentInfo["descripcion"]
        return self.departmentRep.save(currentDepartment)

    def delete(self,id):
        return self.departmentRep.delete(id)  