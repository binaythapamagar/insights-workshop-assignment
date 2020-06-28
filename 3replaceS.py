class ReplaceS:
    
    def replaceS(self,word):
        """
        @argument word string
        @retuns string
        """
        return word.replace(word[word.find('s')],'$')
        
        
if __name__ == "__main__":
    replaceS = ReplaceS()
    print(replaceS.replaceS('Wsords'))