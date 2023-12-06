

with open("input.txt", "r") as file:
    input = file.read()


cards = input.split("\n")
cards = [card.split(":")[1] for card in cards]
cards = [card.split("|") for card in cards]

win_numbers = [[ int(n) for n in card[0].split()] for card in cards]
card_numbers = [[ int(n) for n in card[1].split()] for card in cards]

total_points = 0

for i in range(len(cards)):
    num_win_numbers = 0
    for w_num in win_numbers[i]:
        if w_num in card_numbers[i]:
            num_win_numbers += 1
    if num_win_numbers !=0:
        total_points += 2 ** (num_win_numbers-1)


print(total_points)
