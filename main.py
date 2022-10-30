import multiprocessing
from multiprocessing import Process
from datetime import datetime

# метод для возведения числа в степень, толучение суммы и запись в файл
def getData(queue):
    number = queue.get()
    pow = queue.get()
    numberInPow = number ** pow
    summa = 0
    dateTime = datetime.now()
    for i in range(numberInPow + 1):
        summa += i
    with open("wfile.txt", "a") as file:
        file.write(str(dateTime) + " >> " + str(number) + " ^ " + str(pow) + " = " + str(numberInPow) + " Сумма от 0 до " + str(numberInPow) + " = " + str(summa) + "\n")


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    list_process: list = []
    while True:
        try:
            str = input("Введите число и степень(через пробел), в которую нужно возмести число: ")
            number, pow = (str.split(' '))# получаем значения от пользователя
            numberInInt = int(number)
            powInInt = int(pow)
        except:
            print("Ошибка ввода!")
        queue.put(numberInInt)#добавляем значения в очередь
        queue.put(powInInt)
        process = Process(target=getData, args=(queue,))
        process.start()
        list_process.append(process)

    for process in list_process:# ожидание выполнения процесса
        process.join()
