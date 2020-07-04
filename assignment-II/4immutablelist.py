class Solution:
    flist = []
    def __init__(self,flist):
        self.flist = flist
        
    def solve(self,fnames):
        print(f'id of list before adding is {id(self.flist)}')
        fnames = fnames.split(',')
        
        for name in fnames:
            self.flist.append(name)
            
        print(self.flist)        
        print(f'id of list after adding is {id(self.flist)}')
        
        print('first item in the list is {}'.format(self.flist[0]))
        print('second item in the list is {}'.format(self.flist[1]))
        
if __name__ == "__main__":
    
    solution = Solution([])
    fnames = str (input('Enter your friends name by comma separated : '))
    solution.solve(fnames)