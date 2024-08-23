def count_divisors(n):
    count = 0
    n = int(n)
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

numbers = []
for _ in range(10):
    num = float(input())
    numbers.append(num)

max_number = max(numbers)
divisors = count_divisors(max_number)


if max_number.is_integer():
    max_number = int(max_number)
else:
    max_number = round(max_number, 2)

print(max_number, divisors)
