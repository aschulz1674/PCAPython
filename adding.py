
n = int(input("How many numbers?: "))
num = []
f = 0
for i in range(n):
    y = float(input("Enter a number: "))
    num.append(y)
for i in range(n):
    f += num[i]
print(f)
