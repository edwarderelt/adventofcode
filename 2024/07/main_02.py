tests = []

with open("07/input.txt", "r") as f:
    for line in f:
        tests.append(line.strip().split(" "))

print(tests)


def get_list_results(test_list):
    results = []
    if len(test_list) == 1:
        return [test_list[0]]
    prev_results = get_list_results(test_list[:-1])
    for prev_result in prev_results:
        results.append(prev_result * test_list[-1])
        results.append(prev_result + test_list[-1])
        results.append(int(str(prev_result) + str(test_list[-1])))
    return results

total_sum = 0
for test in tests:
    target = int(test[0][:-1])
    #print(target)

    test_list = [int(i) for i in test[1:]]
    results = get_list_results(test_list)
    #print(results)
    if target in results:
        #print("Target found")
        total_sum += target

print(total_sum)


