class Solution:
    
    def solve(self,number_list):
        
        for nums in range(len(number_list)-1):
            for i in range(nums):
               if number_list[i] > number_list[i+1]:
                    temp = number_list[i]
                    number_list[i] = number_list[i+1]
                    number_list[i+1] = temp
                    
        return number_list

if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([1,4,2,3,8,6,5]))