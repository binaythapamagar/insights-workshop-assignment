class Solution:
    
    def solve (self,word,separator='_'):
       result = word[0]
       if separator == '_':
           for character in word[1:]:
               if character.isupper():
                   result += separator+character.lower()
               else:
                   result += character.lower()           
       else:    
           for character in word[1:]:
               if character.isupper():
                   result += separator+character.lower()
               else:
                   result += character.lower()
       return result
       
if __name__ == "__main__":
    word = 'ThisIsCamelCased' 
    solution = Solution()
    print('The snake case of the word  is {}'.format(solution.solve(word)))
    print('The hyphen case of the word  is {}'.format(solution.solve(word,'-')))
