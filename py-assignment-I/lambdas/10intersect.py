list1 = [1,2,3]
list2 = [3,4,5]

expression  = lambda x: x in list1

print(list(filter(expression,list2)))