

file = open("input.txt","r", encoding="utf-8")

result = 0
num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in file:
    number_str = ""
    line_aux = "" # used for detecting name of numbers

    for char in line:
        line_aux += char
        # add digits to string
        if char.isdigit():
            number_str += char
        #find words in line_aux
        else:
            for i,elem in enumerate(num_list):
                if elem in line_aux:
                    number_str += str(i)
                    # replace line_aux string with number string minus first letter
                    line_aux = elem[1:]
                    break

    # sum first and last digits
    result += int(number_str[0] + number_str[-1])


print(result)
