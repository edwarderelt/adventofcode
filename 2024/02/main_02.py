with open("02/input.txt", "r") as f:
    data = f.read()

total = 0

def is_valid(numbers):
    growing = None
    for i in range(len(numbers)-1):
        #print(numbers[i], numbers[i+1])
        if abs(numbers[i] - numbers[i+1]) > 3 or abs(numbers[i] - numbers[i+1]) == 0:
            return False
        if numbers[i] > numbers[i+1] and growing in [None, False]:
            growing = False
        elif numbers[i] < numbers[i+1] and growing in [None, True]:
            growing = True
        else:
            return False
        
    return True

for line in data.splitlines():
    numbers = line.split(" ")
    numbers = [int(number) for number in numbers]
    for i in range(len(numbers)):
        if is_valid(numbers[:i]+numbers[i+1:]):
            print(numbers[:i]+numbers[i+1:])
            total += 1
            break

print(total)
