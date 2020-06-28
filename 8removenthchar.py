class Solution:
    
    def manupulate(self, word,n):
        if(n < 0  and n >len(word)):
            return "invalid number"
        return f"{word[:n-1]}{word[n:]}"
    
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate('hihellotaxi',3)
    print(f"{result}")