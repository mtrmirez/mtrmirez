#lassoLetter ('A', -3 ='D')
def lassoLetter(letter, shiftAmount):
    #letterCode = 90
    letterCode = ord(letter);

    #begAlphaCode: 65
    begAlphaCode = ord('A')
    alphabetSize = 26

    #decodedLetterCode = 93
    decodedLetterCode = letterCode + shiftAmount;
    print(decodedLetterCode)

    #trueLetterCode = 67
    trueLetterCode = begAlphaCode + ((letterCode - begAlphaCode) + shiftAmount) % alphabetSize
    print(trueLetterCode)

    decodedLetter = chr(trueLetterCode)

    

    return decodedLetter

print (lassoLetter('A', 3))

#print("The letter " + letter + "'s ASCII code is : "letterCode)