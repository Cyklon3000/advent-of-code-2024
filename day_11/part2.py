from math import log10
from mytiming import timeit

stones = []

with open("day_11/input.txt", "r") as file:
    stones = [int(number) for number in file.read().strip().split()]

print(stones)

amountLookup = {}

def getStoneAmount(stone:int, blinks:int):
    if hash((stone, blinks)) in amountLookup.keys():
        return amountLookup[hash((stone, blinks))]
    
    if blinks == 0:
        return 1
    
    if stone == 0:
        amountLookup[hash((stone, blinks))] = getStoneAmount(1, blinks-1)
        return amountLookup[hash((stone, blinks))]
    
    digits = int(log10(stone))+1
    if digits % 2 == 0:
        firstHalf = int(stone / (10 ** (digits / 2)))
        lastHalf = int(stone - firstHalf * (10 ** (digits / 2)))
        amountLookup[hash((stone, blinks))] = getStoneAmount(firstHalf, blinks-1) + getStoneAmount(lastHalf, blinks-1)
        return amountLookup[hash((stone, blinks))]
    
    amountLookup[hash((stone, blinks))] = getStoneAmount(stone * 2024, blinks-1)
    return amountLookup[hash((stone, blinks))]

@timeit
def main():
    totalStones = 0

    for stone in stones:
        totalStones += getStoneAmount(stone, 75)

    print(totalStones)

if __name__ == "__main__":
    main()