stones = []

with open("day_11/input.txt", "r") as file:
    stones = [int(number) for number in file.read().strip().split()]

print(stones)

for _ in range(25):
    i = 0
    while i < len(stones):
        stone = stones[i]
        
        if stone == 0:
            stones[i] = 1
            i+=1
            continue
        
        if len(str(stone)) % 2 == 0:
            stones.insert(i, int(str(stone)[int(len(str(stone))/2):]))
            stones[i+1] = int(str(stone)[:int(len(str(stone))/2)])
            i+=2
            continue
        
        stones[i] *= 2024
        i += 1

print(len(stones))