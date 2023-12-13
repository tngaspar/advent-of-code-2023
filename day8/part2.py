import numpy as np
import math

with open("input.txt", "r") as file:
    instructions = file.readline().replace("\n", "")
    input = file.read()

nodes = input.split("\n")[1:]
nodes = [node.replace("(","").replace(")","").replace("=",",").replace(" ","").split(",") for node in nodes]
nodes = np.array(nodes)

start_nodes = [value for value in nodes[:,0] if value[-1] == "A"]


## With the following commented code I found out that every node hits XXZ on a cycle
## I.e. if a node hits XXZ on cycle N it will hit it every iN where i is an integer

# z_hits = []
# for node in start_nodes:
#     steps = 0
#     next_node = node
#     z_vector = []
#     while(steps < 100000):
#         if instructions[steps % len(instructions)] == "L":
#             side = 1 # left
#         else:
#             side = 2 # right
        
#         node_map = nodes[nodes[:,0] == next_node]
#         next_node = node_map[0][side]
#         print(steps)
#         steps += 1

#         if next_node[-1] == "Z":
#             z_vector.append(steps)
            
#     z_hits.append(z_vector)
    
# for z_vec in z_hits:
#     for z in z_vec:
#         print(z/z_vec[0], z , z_vec[0])




# find first hit of Z for each starting node
z_hits = []
for node in start_nodes:
    steps = 0
    next_node = node
    while(True):
        if instructions[steps % len(instructions)] == "L":
            side = 1 # left
        else:
            side = 2 # right
        
        node_map = nodes[nodes[:,0] == next_node]
        next_node = node_map[0][side]
        steps += 1

        if next_node[-1] == "Z":
            z_hits.append(steps)
            break

print(z_hits)

# find least common multiple of cycles
result = math.lcm(z_hits[0], z_hits[1], z_hits[2], z_hits[3], z_hits[4], z_hits[5])
print(result)