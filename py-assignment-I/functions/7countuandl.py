def count(word):
    counter = {'upper':0,'lower':0}
    
    for x in word:
        if x.isupper():
            counter['upper'] +=1
        else:
            counter['lower'] +=1
    return counter

print(count('hello World'))