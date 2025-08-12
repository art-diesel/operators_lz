def isSimple(number):
    
    for i in range(2,number):
        if number % i == 0:
            print("N")
            break
        print("Y")
        break
print("1)Данные с клаывиатуры")
print("2)Данные из файла")
temp = int(input("Выберете способ 1) или 2):"))
if temp == 1:
    number = int(input("Введите число для проверки:"))
    isSimple(number)
elif temp == 2:
    file = open("simple.txt",'r')
    strNumber = ""
    for line in file:
        strNumber = line
    number = int(strNumber)
    isSimple(number)

    file.close()
    