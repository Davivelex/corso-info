import math

for t in range(0, 25):
    print(f"{round(math.exp(-math.log(2) / 6 * t)*100, 2):.2f}%")

