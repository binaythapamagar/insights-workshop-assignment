class Solution:
    
    def manupulate(self, dict):
       dict.update({2:30})
       return dict
    
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate({0: 10, 1: 20})
    print(f"result is :{result}")