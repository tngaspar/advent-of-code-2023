## Note: This solution is cpu intensive. It took some time to run on my home server.
## I intend on rewriting this solution in the future

# READING INPUT:

with open("input.txt", "r") as file:
    input = file.read()

maps = input.split("\n\n")

seeds = [int(n) for n in maps[0].replace("seeds: ", "").split(" ")]


def get_mapping(map_str):
    map_str = map_str.split("\n")[1:]
    map = [[int(n) for n in line.split()] for line in map_str]
    return map

maps = [get_mapping(m) for m in maps[1:]]


# USING MAPPINGS

def find_destination_number(source_number, map):
    
    destination_number = source_number # default, if there is no mapping
    for line in map:
        if source_number >= line[1] and source_number < line[1] + line[2]:
            destination_number = line[0] + (source_number - line[1])
            break
    return destination_number


min_number = 9999999999999999
L = int(len(seeds)/2) # number of pairs
for m in range(0, len(seeds), 2):
    seed = seeds[m]
    progress_of_pair = 0
    while(seed < seeds[m] + seeds[m+1]):
        source_num = seed
        for map in maps:
            source_num = find_destination_number(source_num, map)
        if source_num < min_number:
            min_number = source_num
        seed = seed + 1
        progress_of_pair += 1
        if progress_of_pair % 1000000 == 0: # print progress every 1000000 seeds
            print("Progress: ", round(progress_of_pair/seeds[m+1]*100, 2),"% for pair:", int(m/2+1)," of ", L, " | Current lowest: ", min_number)

print(min_number)

# creating file with output
file = open("output.txt","w") 
file.write(str(min_number)) 
file.close() 
