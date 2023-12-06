import numpy as np

# when theres is no adjacent character return a dummy "." character
def get_char_aux(matrix, m, n):
    try:
        return matrix[m][n]
    except IndexError:
        return "."

def find_full_number(matrix, m, n):
    num_string = matrix[m][n]
    N = n
    # go right
    while(get_char_aux(matrix, m, n+1).isdigit()):
        num_string += get_char_aux(matrix, m, n+1)
        n = n + 1
    # go left
    n = N
    while(get_char_aux(matrix, m, n-1).isdigit()):
        num_string = get_char_aux(matrix, m, n-1) + num_string
        n = n - 1

    return int(num_string)

with open("input.txt", "r") as file:
    input = file.read()

mat = input.split("\n")
mat = np.array(mat)

result = 0

for i, line in enumerate(mat):
    for j, c in enumerate(line):
        if c == "*":
            adjacent_list = []

            for j_aux in [j-1, j+1]: # numbers left and right of gear
                if get_char_aux(mat,i,j_aux).isdigit():
                    adjacent_list.append(find_full_number(mat, i, j_aux))

            for i_aux in [i-1, i+1]: # numbers above and bellow gear
                if get_char_aux(mat,i_aux,j).isdigit(): # up
                    adjacent_list.append(find_full_number(mat, i_aux, j))
                else: # check diagonals
                    for j_aux in [j-1, j+1]:
                        if get_char_aux(mat, i_aux, j_aux).isdigit():
                            adjacent_list.append(find_full_number(mat, i_aux, j_aux))

            if len(adjacent_list) == 2:
                result += adjacent_list[0] * adjacent_list[1]

print(result)