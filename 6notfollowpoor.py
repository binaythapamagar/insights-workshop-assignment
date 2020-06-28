class Solution:
    
    def manupulate(self, word):
        pnot = word.find('not')
        ppoor = word.find('poor')
        
        if pnot < ppoor and pnot > 0  and ppoor > 0:
            return word.replace(word[pnot:(ppoor+4)],'good')
        else:
            return word
    
if __name__ == "__main__":
    s = Solution();
    print(s.manupulate("The lyrics is not that poor!"))
    print(s.manupulate("The lyrics is poor!"))