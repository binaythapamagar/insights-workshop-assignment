class Solution:
    
    def manupulate(self, word):
        lcase = word.lower()
        ucase = word.upper()
        return f"lowercase: {lcase} , uppercase: {ucase}"
    
if __name__ == "__main__":
    s = Solution();
    word = input('Enter the input :')
    result = s.manupulate(word)
    print(f"{result}")