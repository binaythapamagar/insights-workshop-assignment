class Solution:
    
    def manupulate(self, lists,suffix):
        listed = []
        for item in lists:
            listed.append(f'{item}{suffix}')
        return listed
        
if __name__ == "__main__":
    s = Solution();
    result = s.manupulate([1,2,3,4],'emp')
    print(f"result is :{result}")