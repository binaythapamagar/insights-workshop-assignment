class Solution:
    
    def manupulate(self, num):
        dict = {}
        for x in range(1,num+1):
            dict[x] = x*x
        return dict
    
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate(5)
    print(f'resut is : {result}')