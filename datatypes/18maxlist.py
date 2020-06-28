class Solution:
    
    def manupulate(self, list):
    
        if len(list) == 0:
            return 'list is empty'
        
        max = list[0]
        
        for item in list:
            if(max < item):
                max = item
        return max

if __name__ == "__main__":
    s = Solution();
    result = s.manupulate([1,2,4,5])
    print(f"max is :{result}")