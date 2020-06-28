class Solution:
    
    def manupulate(self):
        dict = {}
        for x in range(1,16):
            dict[x] = x*x
        return dict
    
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate()
    print(f'resut is : {result}')