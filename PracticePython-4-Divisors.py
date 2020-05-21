print("Divisor Checker".center(40, '-'))
number = int(input("Please enter a positive integer number: "))
d = []
for num in range(2, number):
    if number % num == 0:
        d.append(num)

if not d:   # note a list that is not empty returns a True boolean value
    print("Your number is a prime number")
else:
    print(f"Your number has the following divisors: {d}")
