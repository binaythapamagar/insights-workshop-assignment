class Solution:
    
    def manupulate(self, word):
        result = ""
        for i in range(len(word)):
            if i % 2 == 0 :
                result = result + word[i]
        return result
        
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate('hihellotaxi')
    print(f"{result}")