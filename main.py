print("Введите число")
x = int(input())
print("Введите второе число")
y = int(input())


print("ввудите операцию")
z = input()
print("результат равен")
# В зависимости от знака будем выполнять разные действия.
if z == "*":
    print(x * y)
if z == "/" or z == ":":
    print(x / y)
if z == "+":
    print(x + y)
if z == "-":
    print(x - y)
if z == "^" or z == "**":
    print(x ** y)
# print()
