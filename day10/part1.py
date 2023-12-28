import numpy as np

with open("input.txt", "r") as file:
    input = file.read()

# list of reads. each read is a list of integers
pipe_rows = input.split("\n")
pipe_mat = [[c for c in row] for row in pipe_rows]

pipe_mat = np.matrix(pipe_mat)

m, n = pipe_mat.shape

start_coords = np.where(pipe_mat == "S")

def find_start_connecting_pipes(pipe_matrix, coords, m, n):
    connections = []
    if coords[0]!=0: # up
        if pipe_matrix[coords[0]-1,coords[1]] in ["|","F","7"]:
            connections.append((coords[0]-1,coords[1]))
    if coords[0]!=m-1: # down
        if pipe_matrix[coords[0]+1, coords[1]] in ["|", "J","L"]:
            connections.append((coords[0]+1, coords[1]))
    if coords[1]!=0: # left
        if pipe_matrix[coords[0], coords[1]-1] in ["-","L","F"]:
            connections.append((coords[0],coords[0]-1))
    if coords[1]!=n-1: # right
        if pipe_matrix[coords[0], coords[1]+1] in ["-","J","7"]:
            connections.append((coords[0],coords[0]+1))

    return connections

current_pipe_coords = start_coords
next_pipe_coords = find_start_connecting_pipes(pipe_mat, start_coords, m, n)[0] #select an adjacent pipe
num_pipes = 0

while pipe_mat[next_pipe_coords] != "S":
    if pipe_mat[next_pipe_coords] == "|":
        connections = [(next_pipe_coords[0]-1,next_pipe_coords[1]), (next_pipe_coords[0]+1,next_pipe_coords[1])]
    elif pipe_mat[next_pipe_coords] == "-":
        connections = [(next_pipe_coords[0],next_pipe_coords[1]-1), (next_pipe_coords[0],next_pipe_coords[1]+1)]
    elif pipe_mat[next_pipe_coords] == "F":
        connections = [(next_pipe_coords[0]+1,next_pipe_coords[1]), (next_pipe_coords[0],next_pipe_coords[1]+1)]
    elif pipe_mat[next_pipe_coords] == "7":
        connections = [(next_pipe_coords[0]+1,next_pipe_coords[1]), (next_pipe_coords[0],next_pipe_coords[1]-1)]
    elif pipe_mat[next_pipe_coords] == "J":
        connections = [(next_pipe_coords[0]-1,next_pipe_coords[1]), (next_pipe_coords[0],next_pipe_coords[1]-1)]
    elif pipe_mat[next_pipe_coords] == "L":
        connections = [(next_pipe_coords[0]-1,next_pipe_coords[1]), (next_pipe_coords[0],next_pipe_coords[1]+1)]

    connections.remove(current_pipe_coords)
    current_pipe_coords, next_pipe_coords = next_pipe_coords, connections[0]
    num_pipes += 1

steps = (num_pipes + 1) // 2 

print(steps)

