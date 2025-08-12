def countOperation(number):
    count = 0
    while number != 0:
        if number % 2 == 0:
            number /= 2
            count += 1
        else:
            number -= 1
            count += 1
    return count
            
print("1)Данные с клаывиатуры")
print("2)Данные из файла")
temp = int(input("Выберете способ 1) или 2):"))
if temp == 1:
    number = int(input("Введите число для подсчёта операций:"))
    print("Количкство операций до нуля =",countOperation(number))
elif temp == 2:
    file = open("operation.txt",'r+')
    strNumber = ""
    for line in file:
        strNumber = line
    number = int(strNumber)
    file.write("\n")
    file.write("Количкство операций до нуля ="+ str(countOperation(number)))
    file.close()
