import random

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

x = (input('Введите вещественное число '))
num = int(x.replace('.', ''))
summary = 0

while num > 0:
    summary += num % 10
    num //= 10

print(f'Сумма цифр в числе: {summary}')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input("Введите число "))
numb = [1]
for i in range(1, N + 1):
    numb.append(numb[i - 1] * i)
numb.pop(0)
print(f'Для N = {N}: {numb}')

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {2 ,2, 2, 2, 2, 3} -> 13

N = int(input("Введите число "))
numb = []
sum = 0
for i in range(1, N + 1):
    numb.append(round((1 + 1 / i) ** i))
for i in range(len(numb)):
    sum += numb[i]
print(f'Для N = {N}: {numb} -> {sum}')

# Задайте список из N элементов, заполненных числами из
# промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной
# строке одно число. Реализуйте алгоритм перемешивания списка.
N = int(input("Введите число "))
num = []
number = []
for i in range(1):
    for j in range(-N, N + 1):
        num.append(j)
f = open('file.txt')
n1 = int(f.read(1))
n2 = int(f.read(2))
mult = num[n1] * num[n2]
print(f'Массив -> {num}. Произведение элементов на позициях {n1} и {n2} -> {mult}')
for i in range(len(num)):
    number.append(i)

for i in range(len(num)):
    n = random.randint(0, len(number) - 1)
    helpa = num[i]
    num[i] = num[n]
    num[n] = helpa

print(f'Перемешанный массив -> {num}')
