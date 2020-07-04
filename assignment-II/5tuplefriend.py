mytuple = ('Binay','Thapa',25)
people = []

people.append(mytuple)
print(people)

bikalTuple = ('Bikal','Thapa',26)
neerajTuple = ('Neeraj','Neupane',26)
people.append(bikalTuple)
people.append(neerajTuple)

print(people)
print()
#sort
print('sort by name')
print(sorted(people,key=lambda tup: tup[0]))
print()
print('sort by sur name')
print(sorted(people,key=lambda tup: tup[1]))
print()
print('sort by age')
print(sorted(people,key=lambda tup: tup[2]))
