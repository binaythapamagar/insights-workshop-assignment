class SingleString:
    
    def merge(self,fword,lword):
        """
        @argument two string to merge and swap character
        @retuns string
        """
        return f"{lword[:-1]}{fword[-1]} {fword[:-1]}{lword[-1]}"
        
        
if __name__ == "__main__":
    singlestring = SingleString()
    print(singlestring.merge('abc','xyz'))