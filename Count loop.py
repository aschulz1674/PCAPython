count = 0
result = 0
number = 0
while True:
    number = int(input("Type a number: "))
    result += number
    count += 1
    if count == 10:
        break
    else:
        continue
print(result)
