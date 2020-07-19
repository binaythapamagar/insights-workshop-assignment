class Solution:
        
    def isPrime(self,num):
        if num == 1 or num == 2:
            return False
        else:
            for i in range(2,num):
                if num % i == 0:
                    return False
        return True
       
       
if __name__ == "__main__":
    
    solution = Solution()
    num = int (input('Enter number to check if the number is prime or not : '))
    print('The number is prime : {}'.format(solution.isPrime(num)))