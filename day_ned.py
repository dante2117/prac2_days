year = int(input("Введите год для подсчёта: \n"))
sum = 0
for day in range(1,32):
    sum = sum + day // 10 + day % 10
if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0)):
    print(sum*7+(sum-4)*4+(sum-18)+11)
else:
    print(sum*7+(sum-4)*4+(sum-18))