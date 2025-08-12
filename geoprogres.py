def geoprogres(b,q,n):
        sum = (b * (1 - (q ** n))) / (1 - q)
        return sum
print("1)Данные с клаывиатуры")
print("2)Данные из файла")
temp = int(input("Выберете способ 1) или 2):"))
if temp == 1:
    strNumbers = input("Введите три значения для обработки:")
    numbers = strNumbers.split()
    b = int(numbers[0])
    q = int(numbers[1])
    n = int(numbers[2])
    print("Сумма прогрессии =",geoprogres(b,q,n))
elif temp == 2:
    
    file = open("geoprogres.txt",'r')
    strNumbers = ""
    for line in file:
        strNumbers = line 
    numbers = strNumbers.split()
    b = int(numbers[0])
    q = int(numbers[1])
    n = int(numbers[2])
    file.close()
    print("Сумма прогрессии =",geoprogres(b,q,n))
else:
    print("Выберете один из двух выше указаных выриантов!")