class Solution:
    
    def manupulate(self, word):
        return f"{word[-1]}{word[1:-1]}{word[0]}"
    
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate('hihellotaxi')
    print(f"{result}")