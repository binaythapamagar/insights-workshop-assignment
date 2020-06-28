class Solution:
    
    def manupulate(self, string,word):
        count = int(len(string)/2)

        return f'{string[:count]}{word}{string[count:]}'
    
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate('{{}}','hello')
    print(f"{result}")