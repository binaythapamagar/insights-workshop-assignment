class Solution:
    
    def search (self,first,last,lists,num):
        
        if last >= first : 
            
            mid = ( last + first ) // 2
            if lists[mid] == num:
                 print(f'Index of the number is {mid}')
            
            elif lists[mid] > num:
                self.search(first,mid-1,lists,num)
            else:
                self.search(mid+1,last,lists,num)
     
        else:
            return -1
       
       
if __name__ == "__main__":
    number_list = [1,3,5,6,9,10] 
    solution = Solution()
    num = int (input('Enter number to find the position in {} using binary search : '.format(number_list)))
    index = solution.search(0,len(number_list)-1,number_list,num)
    if index == -1:
        print('Number not found')
