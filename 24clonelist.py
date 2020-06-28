class Solution:
    
    def manupulate(self, lists):
        return list(lists)
        
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate([1,1,2,2,3,3,4])
    print(f"clone is :{result}")