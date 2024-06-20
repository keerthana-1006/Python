count = 0
total_sum = 0

for num in range(101, 200):
    if num % 7 == 0:
        count += 1
        total_sum += num

print("Number of integers divisible by 7 between 100 and 200:", count)
print("Sum of these integers:", total_sum)
