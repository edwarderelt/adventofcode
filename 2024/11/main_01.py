with open("11/input.txt", "r") as f:
    stones = f.readline().strip().split(" ")

stones = list(map(int, stones))
print(stones)
reduced_stones = {}

for stone in stones:
    reduced_stones[stone] = reduced_stones.get(stone, 0) + 1

seen_transforms = dict()
def transform_stone(stone):
    if stone in seen_transforms:
        return seen_transforms[stone]
    if stone == 0:
        seen_transforms[stone] = [1]
        return [1]
    if len(str(stone))%2 == 0:
        stone_1 = int(str(stone)[:len(str(stone))//2])
        stone_2 = int(str(stone)[len(str(stone))//2:])
        seen_transforms[stone] = [stone_1, stone_2]
        return [stone_1, stone_2]
    seen_transforms[stone] = [stone*2024]
    return [stone*2024]


for i in range(75):
    print(i)
    stones = reduced_stones.keys()
    new_reduced_stones = {}
    for stone in stones:
        new_stones = transform_stone(stone)
        for new_stone in new_stones:
            new_reduced_stones[new_stone] = new_reduced_stones.get(new_stone, 0) + reduced_stones[stone]
    reduced_stones = new_reduced_stones

total = 0
for amount in reduced_stones.values():
    total += amount
print(total)