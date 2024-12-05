versions = [
[["X","M","A","S"],
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0]],

[["S","A","M","X"],
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0]],

[["X",0,0,0],
 [0,"M",0,0],
 [0,0,"A",0],
 [0,0,0,"S"]],

[["S",0,0,0],
 [0,"A",0,0],
 [0,0,"M",0],
 [0,0,0,"X"]],

[[0,0,0,"S"],
 [0,0,"A",0],
 [0,"M",0,0],
 ["X",0,0,0]],

[[0,0,0,"X"],
 [0,0,"M",0],
 [0,"A",0,0],
 ["S",0,0,0]],

[["X",0,0,0],
 ["M",0,0,0],
 ["A",0,0,0],
 ["S",0,0,0]],

[["S",0,0,0],
 ["A",0,0,0],
 ["M",0,0,0],
 ["X",0,0,0]]
]

input_file = "04/input.txt"
letters_matrix = []
lin_pad = ["O"]*3
with open(input_file, "r") as f:
    data = f.readline()
    line_len = len(data.strip())

col_pad = ["O"]*(line_len+3)

with open(input_file, "r") as f:
    data = f.readlines()

    for line in data:
        letters_matrix.append(list(line.strip())+col_pad)

for i in range(3):
    letters_matrix.append(col_pad)

print(letters_matrix)


def count_version_matches(letters_matrix, versions):
    def does_version_match(matrix, version, start_row, start_col):
        """Check if the version fits in the matrix at the given start position."""
        for i in range(len(version)):
            for j in range(len(version[0])):
                # Skip wildcard checks
                if version[i][j] == 0:
                    continue
                # Check boundaries and match
                if (start_row + i >= len(matrix) or 
                    start_col + j >= len(matrix[0]) or 
                    matrix[start_row + i][start_col + j] != version[i][j]):
                    return False
        return True

    matches_count = 0

    # Iterate over all versions
    for version in versions:
        version_rows, version_cols = len(version), len(version[0])
        
        # Slide the version over the letters_matrix
        for i in range(len(letters_matrix) - version_rows + 1):
            for j in range(len(letters_matrix[0]) - version_cols + 1):
                if does_version_match(letters_matrix, version, i, j):
                    matches_count += 1

    return matches_count


# Count the matches
total_matches = count_version_matches(letters_matrix, versions)
print(f"Total number of matches: {total_matches}")