#Crack the code, open the lock challenge
constraintsList = [('690',1,1), ('741',1,0), ('504',2,0), ('387',0,0), ('219',1,0)]

def checkNumber(number, checknumber, nr_correct, nr_correct_position):
    count_nr_correct, count_nr_correct_position = 0,0
    lnumber = str(number).zfill(len(str(checknumber)))
    for i in range(len(checknumber)):
        if lnumber[i] in checknumber:
            count_nr_correct += 1
        if lnumber[i] == checknumber[i]:
            count_nr_correct_position += 1
    return nr_correct == count_nr_correct and nr_correct_position == count_nr_correct_position

def lockFounder(constraints):
    numberOfConstraints = len(constraints)
    for cnumber in range(1000):
        numberOfMatches=0
        for i in range(numberOfConstraints):
            if checkNumber(cnumber, *constraints[i]):
                numberOfMatches+=1
                if numberOfMatches == numberOfConstraints:
                    print('found:', str(cnumber).zfill(3))

lockFounder(constraintsList)