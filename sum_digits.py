n = int(input("Enter a number: "))
sum_digits = 0

n = abs(n)  # handle negative numbers

while n > 0:
    sum_digits += n % 10
    n //= 10

print("Sum of digits:", sum_digits)