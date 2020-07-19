class Solution:
    
    def solve(self,year):
        
        if year % 400 == 0:
            return f'{year} is a leap year.'

        elif year % 100 == 0:
            return f'{year} is not a leap year.'
        
        elif year % 4 == 0:
            return f'{year} is a leap year.'
        else:
            return f'{year} is not a leap year.'
        
if __name__ == "__main__":
    solution = Solution()
    year = int (input('Enter any year : '))
    print(solution.solve(year))