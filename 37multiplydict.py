class Solution:
    
    def manupulate(self, dict):
        result = 1
        for key,value in dict.items():
            result *= value
        
        return result
        
        
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate({0: 10, 1: 20})
    print(f'result is : {result}')