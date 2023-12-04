

file = open("input.txt","r", encoding="utf-8")

result = 0

for line in file:
    number_str = ""

    for char in line:
        if char.isdigit():
            number_str += char
    # sum first and last digits
    result += int(number_str[0] + number_str[-1])

print(result)
