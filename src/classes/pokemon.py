import random

class Pokemon:
    def __init__(self, id, name, type, sex = None):
        self.__id = int(id)
        self.__name = str(name)
        self.__type = str(type)
        self.__sex = str(sex)
        
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def type(self):
        return self.__type
    
    @property
    def sex(self):
        return self.__sex
    
    @sex.setter
    def sex(self, sex):
        self.__sex = sex
    
    
    #def definedSex(self):
        #numero = random.randint(1, 2)
        #if numero == 1:
            #print(1)
            #self.__sex = 'Macho'
            #return self.__sex
        #else: 
            #print(2)
            #self.__sex = 'Femea'
            #return self.__sex
        
