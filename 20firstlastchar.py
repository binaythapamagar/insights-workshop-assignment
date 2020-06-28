class Solution:
    
    def manupulate(self, list):
        counter = 0
        for item in list:
            if len(item) > 1 and item[0] == item[-1]:
                counter +=1
        return counter
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate(['abc', 'xyz', 'aba', '1221'])
    print(f"count is :{result}")