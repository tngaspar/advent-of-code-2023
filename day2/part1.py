

MAX_CUBES = [12, 13, 14] # RGB

def line_to_rgb(line):

    game_number, line = line.split(':')
    game_number = int(game_number.replace('Game ', ""))
    hands = line.split(';')
    hands_rgb = []
    for hand in hands:
        rgb = [0,0,0]
        hand = hand.split(',')

        for color in hand:
            color = color.split()
            if color[1] == "red":
                rgb[0] = int(color[0])
            elif color[1] == "green":
                rgb[1] = int(color[0])
            elif color[1] == "blue":
                rgb[2] = int(color[0])
        #print(hand, rgb)
        hands_rgb.append(rgb)

    return game_number, hands_rgb


result = 0
with open("input.txt","r", encoding="utf-8") as file:
    for line in file:
        possible = True
        game_num , hands = line_to_rgb(line)
        for hand in hands:
            if not all([hand[i] <= MAX_CUBES[i] for i in range(len(MAX_CUBES))]):
                possible = False
                break

        if possible == True:
            result += game_num


print(result)







