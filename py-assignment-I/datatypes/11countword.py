class Solution:
    
    def manupulate(self, words):
        words = words.split()
        result = {}
        
        for word in words:
            if word in result:
                result[word] += 1 
            else:
                result[word] = 1
        return result
    
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate('Hello from insights workshop academy. This is awesome assignment from insights workshop.')
    print(f"{result}")