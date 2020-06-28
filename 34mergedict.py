class Solution:
    
    def manupulate(self, dict1,dict2):
       dict = {}
       for d in (dict1,dict2):
           dict.update(d)
       return dict
    
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate({1:10, 2:20},{3:30, 4:40})
    print(f"result is :{result}")