from abc import ABCMeta
#se crea el constructor
class AbstractModel(metaclass=ABCMeta):
    def __init__(self,data):
        for llave, valor in data.items():
            setattr(self, llave, valor)
