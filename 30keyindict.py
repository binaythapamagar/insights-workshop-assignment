class Solution:
    
    def manupulate(self, dict,key):
        if key in dict:
            return "Key is present in dict"
        else:
            return "key is not present in dict"
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate({0: 10, 1: 20},4)
    print(f"result is :{result}")