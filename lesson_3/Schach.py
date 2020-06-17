
x = int(input("Вертикаль1: "))
y = int(input("Горизонталь1: "))

if x > 8:
    print("Ошибка")
if y > 8:
    print("Ошибка")

c = int(input("Вертикаль2: "))
d = int(input("Горизонталь2: "))

if ( x + 1 == c or x - 1 == c ) and ( y + 2 == d or y - 2 == d ):
    print(" GO! ")
elif ( x + 2 == c or x - 2 == c ) and ( y + 1 == d or y - 1 == d ):
    print(' GO! ')
else:
    print(' No! ')