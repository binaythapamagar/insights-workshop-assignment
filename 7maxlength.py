class Solution:
    
    def manupulate(self, words):
       
        max = 0
        for word in words:
           wordMax = len(word)
           if(wordMax > max):
               max = wordMax
        return max
    
if __name__ == "__main__":
    s = Solution();
    max = s.manupulate(['hi','hello','taxi'])
    print(f"The maximum length among the list of string is : {max}")