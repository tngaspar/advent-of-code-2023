import numpy as np

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
        game_num , hands = line_to_rgb(line)
        
        hands = np.array(hands)
        power = np.prod([np.max(hands[:,i]) for i in range(3)])
        result += power

        print([np.max(hands[:,i]) for i in range(3)], power)

print(result)







