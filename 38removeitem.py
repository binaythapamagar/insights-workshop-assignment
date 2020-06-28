class Solution:
    
    def manupulate(self, dict,key):
        if key in dict:
            del dict[key]
        
        return dict
        
        
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate({0: 10, 1: 20},1)
    print(f'result is : {result}')