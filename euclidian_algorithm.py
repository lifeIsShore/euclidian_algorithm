def euclidianAlgorithm(firstNumber, secondNumber):
   
    remainders = []
    remainders.append(secondNumber % firstNumber)
   
    while remainders[-1] != 0:
   
        secondNumber = firstNumber
        firstNumber = remainders[-1]
        remainders.append(secondNumber % firstNumber)
   
    return firstNumber, remainders

euclidianAlgorithm(1701, 3768)