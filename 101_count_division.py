def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

numbers = []
for _ in range(10):
    num = int(input())
    numbers.append(num)

max_number = max(numbers)
divisors = count_divisors(max_number)

print(max_number, divisors)
