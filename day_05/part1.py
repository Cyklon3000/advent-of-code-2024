from pprint import pprint as pp

ruleSet = {}
isRuleSet = True

def addRule(line:str):
    beforeNumber = int(line.strip().split('|')[0])
    afterNumber = int(line.strip().split('|')[1])
    
    if beforeNumber in ruleSet.keys():
        ruleSet[beforeNumber].append(afterNumber)
    else:
        ruleSet[beforeNumber] = [afterNumber]

def checkPrint(line:str) -> int:
    printList = [int(page) for page in line.strip().split(',')]
    
    seenBefore = set()
    for page in printList:
        for afterNumber in ruleSet[page]:
            if afterNumber in seenBefore:
                return 0
        seenBefore.add(page)
    
    middlePageNumber = printList[int(len(printList) / 2)]
    return middlePageNumber

totalSum = 0
with open('day_05/input.txt') as file:
    for line in file.readlines():
        if len(line) <= 1:
            isRuleSet = False
            continue
        
        if isRuleSet:
            addRule(line)
            continue
        
        totalSum += checkPrint(line)

print(totalSum)