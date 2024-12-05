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

def checkPrint(line:str) -> bool:
    printList = [int(page) for page in line.strip().split(',')]
    
    seenBefore = set()
    for page in printList:
        for afterNumber in (ruleSet[page] if page in ruleSet.keys() else []):
            if afterNumber in seenBefore:
                return False
        seenBefore.add(page)
    
    return True

def fixPrint(line:str) -> int:
    printList = [int(page) for page in line.strip().split(',')]
    
    seenBefore = []
    p = 0
    
    def isBreakingRule(page):
        for afterNumber in (ruleSet[page] if page in ruleSet.keys() else []):
            if afterNumber in seenBefore:
                return True
        return False
    
    while p < len(printList):
        if isBreakingRule(printList[p]):
            printList[p-1], printList[p] = printList[p], printList[p-1]
            seenBefore.pop()
            p -= 1
            continue
        
        seenBefore.append(printList[p])
        p += 1
    
    # print(printList)
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
        
        if not checkPrint(line):
            totalSum += fixPrint(line)

print(totalSum)