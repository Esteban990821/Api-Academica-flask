from .InterfaceRep import InterfaceRep
from Models.Course import Course
from Models.Students import Students
from Models.Inscription import Inscription
from bson.objectid import ObjectId

class InscriptionRep(InterfaceRep[Inscription]):
    def getListInscribedInCourse(self,idMateria):
        Query = {'materia.$id': ObjectId(idMateria)}
        return self.query(Query)

    def getGreaterValueForCourse(self):
        query = {
            "$group":{
                "_id": "$materia",
                "max": {
                    "$max": "$nota_final"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
                
            }
        }
        pipelino=[query]
        return self.queryAggregation(pipelino)

    def getAvgCourse(self,idMateria):
        query1 = {
            "$match":{"materia.$id":ObjectId(idMateria)}            
        }
        query2 = {
            "$group":{
                "_id": "$materia",
                "promedio": {
                    "$avg": "$nota_final"
                }
                
            }
        }
        pipelino=[query1,query2]
        return self.queryAggregation(pipelino)
    