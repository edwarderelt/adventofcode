with open("09/input.txt", "r") as f:
    data = f.read()

print(data)

blocks = {}

is_file = True
id = 0
block_pos = 0
for element in data:
    if is_file:
        for i in range(int(element)):
            blocks[block_pos] = id
            block_pos += 1
        id += 1
    else:
        for i in range(int(element)):
            blocks[block_pos] = "."
            block_pos += 1
    is_file = not is_file

print(blocks)
n_block_pos = block_pos
print(n_block_pos)

l = 0
r = n_block_pos-1

while l <= r:
    if blocks[l] == "." and blocks[r] != ".":
        blocks[l], blocks[r] = blocks[r], blocks[l]
    elif blocks[l] == ".":
        r -= 1
    else:
        l += 1

print(blocks)

pos = 0
total = 0
while blocks[pos] != ".":
    total += blocks[pos]*pos
    pos += 1

print(total)
