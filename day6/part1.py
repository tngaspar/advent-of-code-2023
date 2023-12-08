
# Example input:
# time = [7, 15, 30]
# distance = [9, 40, 200]

time = [57, 72, 69, 92]
distance = [291, 1172, 1176, 2026]

result = 0
for i in range(len(time)):
    wins = 0
    # 0 and max waiting time will never win
    for t in range(1, time[i]):
        if t * (time[i] - t) > distance[i]:
            wins += 1
    if wins != 0:
        if result == 0:
            result = wins
        else:
            result *= wins

print(result)
