import numpy as np

# Returns true if the input is a symbol
def is_symbol(character):
    if character.isdigit() or character == ".":
        return False
    else:
        return True

# when theres is no adjacent character return a dummy "." character
def get_char_aux(matrix, m, n):
    try:
        return matrix[m][n]
    except IndexError:
        return "."

# Returns true if there is any symbol around the given character
def adjacent_symbols(matrix, m, n):
    adjacent_characters = [
        get_char_aux(matrix ,m-1, n-1), 
        get_char_aux(matrix ,m, n-1), 
        get_char_aux(matrix ,m+1, n-1),
        get_char_aux(matrix ,m-1, n),
        get_char_aux(matrix ,m+1, n),
        get_char_aux(matrix ,m-1, n+1),
        get_char_aux(matrix ,m, n+1),
        get_char_aux(matrix ,m+1, n+1),
        ]

    return any([is_symbol(c) for c in adjacent_characters])


with open("input.txt", "r") as file:
    input = file.read()


mat = input.split("\n")
mat = np.array(mat)

result = 0
current_num = ""
to_add = False

for i, line in enumerate(mat):
    for j, c in enumerate(line):
        if c.isdigit():
            current_num += c
            if to_add is False:
                to_add = adjacent_symbols(mat, i, j)
            # if at end of line
            if j == len(line) - 1:
                if to_add is True:
                    result += int(current_num)
                    to_add = False
                current_num = ""
        # found the full number
        elif current_num != "":
            if to_add is True:
                result += int(current_num)
                to_add = False
            current_num = ""
        
print(result)
            

