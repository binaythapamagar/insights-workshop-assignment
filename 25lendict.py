class Solution:
    
    def manupulate(self, lists):
        result = False
        for item in lists:
            if len(item) > 0:
                result  = True
        return result
        
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate([{},{},{}])
    print(f"dict. in list is not empty :{result}")