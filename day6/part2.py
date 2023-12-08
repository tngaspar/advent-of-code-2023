import math

# Example input:
# TIME = 71530
# DISTANCE = 940200

TIME = 57726992
DISTANCE = 291117211762026

# quadratic equation
a = 1
b = - TIME
c = DISTANCE

# any waiting time amount between the solutions for this equation will beat the record
x_big = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
x_small = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

# would need to adjust if x_big or x_small was an integer
result = math.floor(x_big) - math.ceil(x_small) + 1

print(result)
