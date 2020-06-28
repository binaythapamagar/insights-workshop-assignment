class Solution:
    
    def manupulate(self, word,tag):
        return f'<{tag}>{word}</{tag}>'
    
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate('Hello from insights workshop academy. This is awesome assignment from insights workshop.','i')
    print(f"{result}")