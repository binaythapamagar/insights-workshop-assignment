class Solution:
    
    def partition(self,dataList,lb,ub):
        
        pivot = dataList[lb]
        start = lb+1
        end = ub
        
        while start > end:
            
            while start < end and dataList[start] <= pivot:
                start +=1
            
            while start < end and dataList[end] >= pivot:
                end +=1
            
            if(start < end):
                temp = dataList[start]
                dataList[start] = dataList[end]
                dataList[end] = dataList[start]
                
        temp = dataList[ub]
        dataList[ub] = dataList[end]
        dataList[end] = temp
            
            
        return end
        
    def solve(self,number_list,start,end):
        if start < end:
            split = self.partition(number_list,start,end)
            self.solve(number_list,start,split-1)
            self.solve(number_list,split+1,end)
            
        return number_list

if __name__ == '__main__':
    solution = Solution()
    data_list = [1,4,2,3,8,6,5]
    print(solution.solve(data_list,0,len(data_list)-1))