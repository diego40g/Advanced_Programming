names = ['Diego','Richard','Lucia']
ages = [18, 50 ,15]

str_ages = list(map(str,ages))

print(ages)
print(str_ages)

##PARA QUE SUGUIERA LOS METODOS DE UNA LISTA
##NO PASA NADA HASTA LLAMARLA
def pretty_print_list(input_list: list):
    pass

##def pretty_print_list(input_list: list):
##    print('->'.join(input_list)) ##interpretar el string como un separador

##Procedimiento de ciudano de primera clase COSA EXTRAÑA
proc_list = [pretty_print_list, print]
proc_list[0](names)
proc_list[0](str_ages)
proc_list[1](names)
proc_list[1](str_ages)


pretty_print_list(names)
pretty_print_list(str_ages)