class MakeIng:
    
    def makeIng(self,word):
        """
        @argument word string
        @retuns string
        """
        if len(word) < 3:
            return "length of string must be greater than 3."
        
        if word.endswith('ing'):
            return f"{word}ly"
        else:
            return f"{word}ing"
        
        
if __name__ == "__main__":
    word = input('Enter a word: ')
    makeing = MakeIng()
    print(makeing.makeIng(word))