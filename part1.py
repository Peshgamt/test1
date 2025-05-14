user_input = input("Введите числа через запятую: ")
numbers = []
for num in user_input.split(','):
    numbers.append(int(num.strip()))

# 1. 
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
print("Четные числа:", even)

# 2. 
max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Максимальное число:", max_num)
print("Минимальное число:", min_num)

# 3. 
for i in range(len(numbers)):
    for j in range(len(numbers)-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Отсортированный список:", numbers)
