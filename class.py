a = int(input("Сколько учеников в первом классе:"))
b = int(input("Сколько учеников во втором классе"))
c = int(input("Сколько учеников в третьем классе"))
desk = (a % 2 + a // 2) + (b % 2 + b // 2) + (c % 2 + c // 2)
print(desk)
