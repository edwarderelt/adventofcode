rules = {}
changes = []
store_rules = True
with open("05/input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() == "":
            store_rules = False
        elif store_rules:
            l, r = line.split("|")
            l, r = int(l), int(r)
            rules[l] = rules.get(l, set())
            rules[l].add(r)
        else:
            int_line = [int(i) for i in line.strip().split(",")]
            changes.append(int_line)

print(rules)
print(changes)

invalid_changes = []
for change in changes:
    valid_change = True
    for i in range(len(change)):
        if not valid_change:
            break
        if change[i] in rules:
            for j in range(i):
                if change[j] in rules[change[i]]:
                    valid_change = False
                    break
    if not valid_change:
        invalid_changes.append(change)

print(invalid_changes)

#Fail 1
# from graphlib import TopologicalSorter
# # Create the graph
# graph = {key: set() for key in rules.keys()}
# for key, values in rules.items():
#     for value in values:
#         graph.setdefault(value, set())  # Ensure all values are nodes in the graph
#         graph[key].add(value)

# # Perform topological sorting
# ts = TopologicalSorter(graph)
# sorted_list = list(ts.static_order())[::-1]

#Fail 2
# def compute_weights(dependencies):
#     # Compute the "priority weight" for each node
#     weights = {}

#     def calculate_weight(node, visited=None):
#         if visited is None:
#             visited = set()
#         if node in visited:
#             return 0  # Avoid cycles
#         if node in weights:
#             return weights[node]
#         visited.add(node)
#         weight = 1 + sum(calculate_weight(dep, visited) for dep in dependencies.get(node, []))
#         weights[node] = weight
#         visited.remove(node)
#         return weight

#     for node in dependencies:
#         calculate_weight(node)
    
#     return weights

def dependency_sort(input_list, dependencies):
    # Create a result list and a visited set
    result = []
    visited = set()

    def visit(node):
        if node in visited:
            return  # Node is already processed
        visited.add(node)
        for dep in dependencies.get(node, []):
            if dep in input_list:  # Only consider dependencies in the input list
                visit(dep)
        if node in input_list:
            result.append(node)  # Add the node after its dependencies

    # Visit all nodes in the input list
    for node in input_list:
        visit(node)
    
    return result[::-1]

sorted_list = dependency_sort(invalid_changes[0], rules)
print(sorted_list)
print("##########################")

# Sort the input list based on the topological order
total = 0
fixed_changes = []
for change in invalid_changes:
    sorted_input_list = dependency_sort(change, rules)
    print(sorted_input_list)
    fixed_changes.append(sorted_input_list)
    total += sorted_input_list[len(sorted_input_list)//2]

print(total)


still_invalid_changes = []
for change in fixed_changes:
    valid_change = True
    for i in range(len(change)):
        if not valid_change:
            break
        if change[i] in rules:
            for j in range(i):
                if change[j] in rules[change[i]]:
                    valid_change = False
                    break
    if not valid_change:
        still_invalid_changes.append(change)

print(still_invalid_changes)