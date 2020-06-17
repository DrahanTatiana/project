

y = int(input("Enter a number: "))
x = 2
i = 1

while x**i <= y:
    i += 1
print(y, i-1, x**(i-1) )
