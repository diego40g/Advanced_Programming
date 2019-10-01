##Asignacion iterativa 
squared_nums = [num**2 for num in range(10)]
print (squared_nums)

##Los diccionarios se asignan como tipos de datos JSON

student = {
    "name": "Diego",
    "age": "21"
}
##print(student.get)
a=20 if squared_nums[0]==0 else 10 ##devuelve 20
a=20 if squared_nums[1]==0 else 10 ##devuelve 10
##TERNARIAS ANIDADAS

a=20 if squared_nums[1]==0 else 10 if squared_nums[0]==0 else 5

##funcion orden superior
def printer(print_func, input_list):
    print_func(input_list)

##IMPORT
print("ULTIMA PARTE")
from funtions import pretty_print_list
pretty_print_list(['1','2'])

names = ['Diego','Richard','Lucia']

printer(pretty_print_list, names)
printer(print, names)