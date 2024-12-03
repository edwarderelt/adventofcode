with open("02/input.txt", "r") as f:
    data = f.read()

total = 0

for line in data.splitlines():
    numbers = line.split(" ")
    numbers = [int(number) for number in numbers]
    growing = None
    valid = True
    for i in range(len(numbers)-1):
        #print(numbers[i], numbers[i+1])
        if abs(numbers[i] - numbers[i+1]) > 3 or abs(numbers[i] - numbers[i+1]) == 0:
            valid = False
            break

        if numbers[i] > numbers[i+1] and growing in [None, False]:
            growing = False
        elif numbers[i] < numbers[i+1] and growing in [None, True]:
            growing = True
        else:
            #print(numbers[i], numbers[i+1], growing)
            valid = False
            break
    if valid:
        print(numbers)
        total += 1

print(total)
