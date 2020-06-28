class Solution:
    
    def manupulate(self, list, anotherlist):
        list[-1:] = anotherlist
        return list
    
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate([1,2,3,4],[5,6,7])
    print(f"result is :{result}")