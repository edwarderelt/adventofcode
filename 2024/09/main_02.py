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

#print(blocks)
n_block_pos = block_pos
#print(n_block_pos)



moved_ids = set()
current_id = blocks[n_block_pos-1]
current_block_size = 0
id_start = n_block_pos
#print(current_id)
for i in range(n_block_pos-1, 0, -1):
    print("i: ", i)
    if blocks[i] == ".":
        continue
    if blocks[i] == current_id:
        current_block_size += 1
        id_start -= 1
    else:
        #print("current_id: ", current_id)
        #print("current_block_size: ", current_block_size)
        # End of block

        empty_size = 0
        empty_start = 0
        # Find empty block
        if current_id not in moved_ids:
            for j in range(empty_start, n_block_pos, 1):
                #print("j: ", j, "empty_size: ", empty_size, "empty_start: ", empty_start)
                if blocks[j] == ".":
                    empty_size += 1
                    if empty_size == current_block_size and empty_start <= i+1:
                        # Move block
                        for k in range(empty_start, empty_start+current_block_size, 1):
                            blocks[k] = current_id
                        for t in range(id_start, id_start+current_block_size, 1):
                            #print("t: ", t)
                            blocks[t] = "."
                        break
                else:
                    empty_size = 0
                    empty_start = j+1


        moved_ids.add(current_id)
        #print(blocks)
        blocks_str = "".join(str(v) for v in blocks.values())
        #print(blocks_str)
        # Start new block
        current_id = blocks[i]
        current_block_size = 1
        id_start = i
# list to str, values are ints
blocks_str = "".join(str(v) for v in blocks.values())
#print(blocks_str)
#print(blocks)

total = 0
for i in range(len(blocks.keys())):
    if blocks[i] != ".":
        total += blocks[i]*i

print(total)
