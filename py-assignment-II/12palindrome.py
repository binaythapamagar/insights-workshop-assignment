class Solution:
           
    def is_Palindrom(self,word):
        reverseWord = word[::-1]
        
        if word == reverseWord:
            return True
        else:
            return False
        
if __name__ == "__main__":
    solution = Solution()
    word = input('Enter a word to check palindrom :')
    print(f"The word {word} is Palindrom : {solution.is_Palindrom(word)}")