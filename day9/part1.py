

with open("input.txt", "r") as file:
    input = file.read()

# list of reads. each read is a list of integers
reads = [[int(n) for n in i.split()] for i in input.split("\n")]


def next_list(current_list):
    next_list = []
    for i, elem in enumerate(current_list[1:]):
        next_list.append(elem - current_list[i])
    return(next_list)


def difference(current_list):
    nlist = next_list(current_list)
    if any(nlist) == False: # if all elements are 0 reached the end
        return current_list[-1]
    else:
        r = current_list[-1] + difference(nlist)
        return r
    
result = 0
for read in reads:
    result += difference(read)

print(result)
