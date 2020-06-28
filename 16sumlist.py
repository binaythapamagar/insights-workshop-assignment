class Solution:
    
    def manupulate(self, list):
        total = 0
        if len(list) == 0:
            return 'list is empty'
        
        for item in list:
            total += item
        return total

if __name__ == "__main__":
    s = Solution();
    result = s.manupulate([1,2,4,5])
    print(f"total is :{result}")