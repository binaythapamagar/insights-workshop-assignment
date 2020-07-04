class Solution:
           
    def is_Palindrom(self,word):
        reverseWord = word[::-1]
        
        if word == reverseWord:
            return True
        else:
            return False
        
if __name__ == "__main__":
    solution = Solution()
    print(f"The word PAAP is Palindrom : {solution.is_Palindrom('PAAP')}")