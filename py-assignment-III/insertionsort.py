class Solution:
    
    def solve(self,nlist):
       for index in range(1,len(nlist)):
            currentvalue = nlist[index]
            position = index
            while position>0 and nlist[position-1]>currentvalue:
                nlist[position]=nlist[position-1]
                position = position-1
            nlist[position]=currentvalue
                        
       return nlist
   
if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([1,4,2,3,8,6,5]))