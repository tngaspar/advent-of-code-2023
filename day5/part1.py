
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


destination_numbers = []
for seed in seeds:
    source_num = seed
    for map in maps:
        source_num = find_destination_number(source_num, map)
    destination_numbers.append(source_num)

print(min(destination_numbers))
