people = [('Prem','Pun',29)]

mytuple = ('Binay','Thapa',25)
bikalTuple = ('Bikal','Thapa',26)
neerajTuple = ('Neeraj','Neupane',None)
people.append(bikalTuple)
people.append(neerajTuple)
people.append(mytuple)

#lambda expression
makedigit = lambda x: x if x != None else 0
counter = lambda x: 1 if x != None else 0
difference = lambda x: f'{x[0]} is {average-x[2]} younger than average' if x[2] < average else f'{x[0]} is {x[2]-average} older than average'

#average
average = int(sum([ makedigit(i[2]) for i in people]) / sum([ counter(i[2]) for i in people]))

print(f'The list of people are {people}')
print(f'Average age is {average}')

for person in people:
    if person[2] == None:
        continue
    else:
        print(difference(person))
