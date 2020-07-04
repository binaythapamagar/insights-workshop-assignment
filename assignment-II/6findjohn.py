class Solution:
           
    def solve(self,friendlist):
       found = False 
       for friend in friendlist:
           if friend == 'John':
               found = True
           else:
               found = False
       
       if found:
           print('John is found') 
       else:
           print('John not found') 
        
        
if __name__ == "__main__":
    friendlist = ['Ram','Shyam','Hari','Getta','John']
    solution = Solution()
    solution.solve(friendlist)