def manupulate(words):
               
        for i in range(len(words)):
            if i < (len(words)-1) and words[i] == words[i+1] :
                del words[i]
        return words
    
print(manupulate([1,2,3,3,3,3,4,5]))