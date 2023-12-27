def lassoLetter(letter, shiftAmount):
    letterCode = ord(letter)

    CapACode = ord('A')
    CapZCode = ord('Z')
    lowACode = ord('a')
    lowZCode = ord('z')

    alphabetSize = 26

    if (letterCode >= CapACode) & (letterCode <= CapZCode):
        begAlphaCode = CapACode
    else:
        begAlphaCode = lowACode
        


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
print(lassoWord("OSKZA", -18))
print(lassoWord("OHUPO", -1))
print(lassoWord("ED", 25))