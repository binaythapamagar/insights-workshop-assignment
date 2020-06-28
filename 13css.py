class Solution:
    
    def manupulate(self, words):
        words =words.split(',')
        words.sort()
        
        for i in range(len(words)):
            if i < (len(words)-1) and words[i] == words[i+1] :
                del words[i]
        return words
    
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate('red,white,black,red,green,black')
    print(f"{result}")