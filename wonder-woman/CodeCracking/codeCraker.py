def lassoLetter(letter, shiftAmount):
    letterCode = ord(letter);

    
    begAlphaCode = ord('A')
    alphabetSize = 26

    decodedLetterCode = letterCode + shiftAmount;

    trueLetterCode = begAlphaCode + ((letterCode - begAlphaCode) + shiftAmount) % alphabetSize

    decodedLetter = chr(trueLetterCode)

    

    return decodedLetter

def lassoWord(word, shifAmount):
    decodedWord = ""

    for letter in word:
        decodedLetter = lassoLetter(letter, shifAmount)

        decodedWord = decodedWord + decodedLetter
    
    return decodedWord

print(lassoWord("WHY", 13))