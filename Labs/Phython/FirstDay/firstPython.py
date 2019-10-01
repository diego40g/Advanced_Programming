print("Hello World")

##CREAR LISTAS
names = ['Diego','Richard','Lucia']
ages = [18, 50 ,15]
##imprimir lista
print(ages)
##concatenar lista
print('I have this names: {} whit this ages: {}'.format(names,ages))
##agregar elemento a la lista
names.append('Damian')
print(names)
##concatener listas
names.extend(['Juan','Fanny'])
print(names)
##pop remueve el ultimo elemento de la lista y lo muestra
ivan=names.pop()
print(names)
print(ivan)
##Insertar dato con indice
names.insert(1,'Ivan')
print(names)