with open('input.txt') as f:
    lines = f.read()


searchString = ['m', 'u', 'l', '(']

totalSum = 0
for c, char in enumerate(lines): # for each line in lines:
    try:
        listFromNow = lines[c:]

        isValidOpener = True
        for s, seachChar in enumerate(searchString):
            isValidOpener = isValidOpener and seachChar == listFromNow[s]

        if not isValidOpener:
            continue
        
        listFromNowPrefix = listFromNow[len(searchString):]
        print(f"Passed Mul '{listFromNowPrefix[:10]}'")

        splittedList = listFromNowPrefix.split(",")
        if len(listFromNowPrefix) < 2:
            continue
        listFromNowPrefix = splittedList[0]
        num1 = int(listFromNowPrefix)
        
        if not (str(listFromNowPrefix).isnumeric() and int(listFromNowPrefix)<1000):
            continue
        print(f"Value 1: {listFromNowPrefix}")
        
        listFromNowPrefix = listFromNow[len(searchString):]
        listFromNowPrefixNum1 = listFromNowPrefix[len(str(num1))+1:]

        splittedList = listFromNowPrefixNum1.split(")")
        if len(listFromNowPrefixNum1) < 2:
            continue
        listFromNowPrefixNum1 = splittedList[0]
        num2 = int(listFromNowPrefixNum1)
        
        if not (str(listFromNowPrefixNum1).isnumeric() and int(listFromNowPrefixNum1)<1000):
            continue
        print(f"Value 2: {listFromNowPrefixNum1}")
        
        totalSum += int(num1) * int(num2)
        print(f"{num1} * {num2} = {int(num1) * int(num2)}")
    except:
        print("Exception!!!")
        pass

print(totalSum)