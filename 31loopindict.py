class Solution:
    
    def manupulate(self, dict):
        for key,value in dict.items():
            print(f'key :{key}, value:{value}')

if __name__ == "__main__":
    s = Solution();
    result = s.manupulate({0: 10, 1: 20})