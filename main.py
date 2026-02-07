# 16-mashq
try:
    yosh = int(input("Yosh: "))
    print("Yosh:", yosh)
except ValueError:
    print("Yosh son bo‘lishi kerak")

# 17-mashq
try:
    l = []
    print(l[-1])
except IndexError:
    print("List bo‘sh")

# 18-mashq
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print("Nolga bo‘lish mumkin emas")
except ValueError:
    print("Son kiritilmadi")

# 19-mashq
try:
    d = {"ism": "Ali"}
    k = input("Kalit: ")
    print(d[k])
except KeyError:
    print("Bunday kalit yo‘q")

# 20-mashq
import math

try:
    x = float(input("Son: "))
    print(math.sqrt(x))
except ValueError:
    print("Manfiy yoki xato son")
