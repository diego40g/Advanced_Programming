name='diego1'

if name == 'diego':
    print(True)
else:
    print(False)

if name == 'diego':
    print(True)
elif name == 'diego1':
    print('Your name is {}'.format(name))
else:
    print(False)

##bucle for normal
for i in range(10): 
    print(i)

##bucle for each
names = ['Diego','Richard','Lucia']
ages = [18, 50 ,15]
for name in names:
    print(name)
##ZIP emparejar dos listas
for name_age in zip(names,ages):
    print(name_age)

##print('{} ->{} ->{}'.format(ages1,ages2,ages3)

##
##for name_age in zip(names,ages):
##    print('{} -> {}' .format(name,ages))

while names:
    print(names.pop())