import math

n = int(input("Insersci lunghezza lato: "))

for i in range(n):
    print("*"*n)

print("\n")

n *= 2

for i in range(math.ceil(n/2)):
    print(" " * ((n - (2*i+1))//2) + "*"*(2*i+1))

for i in range(math.ceil(n/2)-2, -1, -1):
    print(" " * ((n - (2*i+1))//2) + "*"*(2*i+1))

