num = [1,2,3,4]
print('even number')
print(list(filter(lambda x: x%2 == 0, num)))
print('odd number')
print(list(filter(lambda x: x%2 != 0, num)))