

with open("input.txt", "r") as file:
    input = file.read()

input = [row.split() for row in input.split("\n")]
input = [[row[0], int(row[1])] for row in input]


cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

# replace card symbols with numbers for easier sorting
replacements = [
    ["A", "14"],
    ["K", "13"],
    ["Q", "12"],
    ["J", "11"],
    ["T", "10"],
    ["9", "09"],
    ["8", "08"],
    ["7", "07"],
    ["6", "06"],
    ["5", "05"],
    ["4", "04"],
    ["3", "03"],
    ["2", "02"]
]

for hand in input:
    card_counts = []
    for card in cards:
        card_counts.append(hand[0].count(card))
    if max(card_counts) == 5:
        hand.append(1) # five of a kind
    elif 4 in card_counts:
        hand.append(2) # four of a kind
    elif 3 in card_counts:
        if  2 in card_counts:
            hand.append(3) # full house
        else:
            hand.append(4) # three of a kind
    elif 2 in card_counts:
        if card_counts.count(2) == 2:
            hand.append(5) # two pair
        else:
            hand.append(6) # one pair
    else:
        hand.append(7) # high card

    # add element to each hand with replacement values:
    hand_aux = hand[0]
    for row in replacements[::-1]:
       hand_aux = hand_aux.replace(row[0], row[1])
    hand.append(hand_aux)


sorted = sorted(input, key=lambda x: -x[2]*10**10 + int(x[3]))

result = 0
for i, hand in enumerate(sorted):
    result += (i + 1) * hand[1]

print(result)
