class Solution:
    
    def manupulate(self, list):
    
        if len(list) == 0:
            return 'list is empty'
        
        min = list[0]
        
        for item in list:
            if(min > item):
                min = item
        return min

if __name__ == "__main__":
    s = Solution();
    result = s.manupulate([1,2,4,5])
    print(f"min is :{result}")