
num = int(input("Enter a number: "))
a = num % 10
b = num % 100 // 10
c = num // 100

res = a * 100 + b * 10 + c
print(res)

# Добрый день Николай. Я сделала еще вариант для четырехзначного числа, для проверки себя, что я разобралась.

num = int(input("Enter a number: "))
a = num // 1000
b = num // 100 % 10
c = num // 10 % 10
d = num % 10

my = d * 1000 + c * 100 + b * 10 + a
print(my)
