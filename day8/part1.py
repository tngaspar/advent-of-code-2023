import numpy as np

with open("input.txt", "r") as file:
    instructions = file.readline().replace("\n", "")
    input = file.read()

nodes = input.split("\n")[1:]
nodes = [node.replace("(","").replace(")","").replace("=",",").replace(" ","").split(",") for node in nodes]
nodes = np.array(nodes)

current_node = "AAA"
steps = 0

while(current_node != "ZZZ"):
    index = np.where(nodes[:,0] == current_node)
    if instructions[steps % len(instructions)] == "L":
        current_node = nodes[index][0,1]
    else:
        current_node = nodes[index][0,2]
    steps += 1

print(steps)

