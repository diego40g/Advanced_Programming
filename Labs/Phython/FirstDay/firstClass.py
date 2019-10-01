class Student:
    color = 'Red'
    
    class Meta:
        name = 'This is a metaClass'

    def __init__(self, _id, _name, _age,_cell_number):
    ##def __init__(self, _id, _name, _age):
        self.id = _id
        self.name = _name
        self.age = _age
        ##genera modificadores de estado 2 guion bajo
        ##self __private_age = 1000
        class Cellphone:
            def __init__(self, number):
                self.number = number
        self.phone = Cellphone(_cell_number)


## similar a toString sobre escribe el comportamiento del objeto, cuando se lo llama por consola
    def __repr__(self):
        return 'Student({})'.format(self.__dict__)

##print(Student('L00368708', 'Diego', 22))
##GET AGE
##print(Student('L00368708', 'Diego', 22).age)

##print(Student('L00368708', 'Diego', 22).color)
##print(Student.color)
print(Student('L00368708', 'Diego', 22, '0980491964').phone)


