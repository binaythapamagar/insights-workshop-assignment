class Slice:
    
    def sliceWord(self,word):
        """
        @argument word to be sliced
        @returns slices string
        
        """
        if len(word) < 2:
            return "Empty String"
        elif len(word) == 2 :
            return word*2
        else:
            return f"{word[:2]}{word[-2:]}"

if __name__ == "__main__":
    word = input('Word will be sliced upto 2 character from fist and last. Enter the word: ')
    slice = Slice()
    print(slice.sliceWord(word))