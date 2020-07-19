class CharacterCount:
    
    def count(self,word):
        """
        word as attribute to count
        returns result dictionary result: key as character, value as count 
        """
        result = {}
        for ch in word:
            #count function counts the character in given string
            result[ch] = word.count(ch)
        return result


if __name__ == "__main__":
    word  = input('enter the input word: ')
    characterCount = CharacterCount()
    print(characterCount.count(word))