import matplotlib.pyplot as plt
bangladesh_flag = [
    "G G G G G G G G",
    "G G R R G G G G",
    "G R R R R G G G",
    "G G R R G G G G",
    "G G G G G G G G"
]

for row in bangladesh_flag:
    for color in row.split():
        if color == "R":
            print("\033[41m  \033[0m", end="")
        elif color == "G":
            print("\033[42m  \033[0m", end="")
        elif color == "W":
            print("\033[47m  \033[0m", end="")
    print()
uzor= [
    "R R R R R",
    "R G G G R",
    "R G R R R",
    "R G R G G ",
    "R G R R R",
]
for row1 in uzor:
    for color in row1.split():
        if color == "R":
            print("\033[41m  \033[0m", end="")
        elif color == "G":
            print("\033[42m  \033[0m", end="")
        elif color == "W":
            print("\033[47m  \033[0m", end="")
    print()


with open('sequence.txt', 'r') as file:
    numbers = [float(line) for line in file.readlines()]

first_sum = sum(numbers[:125])
second_sum = sum(numbers[125:])
print("Сумма первых 125 чисел:", first_sum)
print("Сумма вторых 125 чисел:", second_sum)

x = list(range(10))
y = [2*x_val + 3 for x_val in x]
plt.plot(x, y)
plt.show()

