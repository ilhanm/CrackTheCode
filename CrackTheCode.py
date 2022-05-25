constraintsList = [('690',1,1), ('741',1,0), ('504',2,0), ('387',0,0), ('219',1,0)]

def checkNumber(numberToCheck, number, numberOfCorrectDigit, numberOfCorrectPosition):
    countedCorrectDigit, countedCorrectPosition = 0,0
    digits = str(numberToCheck).zfill(len(str(number))) 
    for i in range(len(number)):
        if digits[i] in number:
            countedCorrectDigit += 1
        if digits[i] == number[i]:
            countedCorrectPosition += 1
    return numberOfCorrectDigit == countedCorrectDigit and numberOfCorrectPosition == countedCorrectPosition

def lockFounder(constraints):
    correctAnswers = []
    numberOfConstraints = len(constraints)
    for cnumber in range(1000):
        numberOfMatches=0
        for i in range(numberOfConstraints):
            if checkNumber(cnumber, *constraints[i]):
                numberOfMatches+=1
                if numberOfMatches == numberOfConstraints:
                    correctAnswers.append(str(cnumber).zfill(3))
    return correctAnswers

print(lockFounder(constraintsList))  #['150', '420', '495']
