def last(n):return n[-1]
    
def manupulate(list):
        return sorted(list,key=last)

print(manupulate([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))