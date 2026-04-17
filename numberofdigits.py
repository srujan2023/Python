n = int(input("Enter a number: "))
count = 0

if n == 0:
    count = 1
else:
    n = abs(n)  # handle negative numbers
    while n > 0:
        n //= 10
        count += 1

print("Number of digits:", count)