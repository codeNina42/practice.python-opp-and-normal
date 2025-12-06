positive = 0
negative = 0
zero = 0

print("Enter 10 numbers:")

for i in range(10):
    num = int(input())
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)
