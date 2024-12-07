testValues = []
equations = []

with open("day_07/input.txt", "r") as file:
    for line in file.readlines():
        testValue, equation = line.split(": ")
        
        testValues.append(int(testValue))
        equations.append([int(num) for num in equation.strip().split()])

lineCount = len(testValues)

# for testValue, equation in zip(testValues, equations):
#     print(f"{testValue}: {equation}")
# print()

totalSum = 0
for testValue, equation in zip(testValues, equations):
    # Loops through every space between numbers
    nextFirstValues = [equation[0]]

    for secondValueIndex in range(1, len(equation)):
        firstValues = nextFirstValues.copy()
        nextFirstValues = []
        
        for firstValue in firstValues:
            secondValue = equation[secondValueIndex]
            
            numberSum = firstValue + secondValue
            numberProduct = firstValue * secondValue
            numberConcatenation = int(str(firstValue) + str(secondValue))

            if numberSum <= testValue:
                nextFirstValues.append(numberSum)
            if numberProduct <= testValue:
                nextFirstValues.append(numberProduct)
            if numberConcatenation <= testValue:
                nextFirstValues.append(numberConcatenation)
    
    if max(nextFirstValues) == testValue:
        totalSum += testValue

print(totalSum)