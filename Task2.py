num = int(input("Введите число: "))
i = 2  # первое простое число
list = []
while i <= num:
    if num % i == 0:
        list.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители вашего числа приведены в списке: {list}")