import multiprocessing
from multiprocessing import Process
from datetime import datetime

# метод для возведения числа в степень, толучение суммы и запись в файл
def getData(queue):
    while True:
        """Когда перед циклом ввода процесс обращается к методу с пустой очерью
        из которой нечего считывать, программа выходит из цикла while True
        и так как процесс не закончен мы продолжаем основной код и делаем ввод данных,
        которые добавляются в очередь и используются в методе записи в файл"""
        if queue.empty():
            continue
        num, pow = queue.get()
        numberInPow = num ** pow
        dateTime = datetime.now()
        summa = sum(range(numberInPow + 1))
        with open("wfile.txt", "a", encoding='utf8') as file:
            file.write(str(dateTime) + " >> " + str(num) + " ^ " + str(pow) + " = " + str(numberInPow) + " Сумма от 0 до " + str(numberInPow) + " = " + str(summa) + "\n")


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    """Для того чтобы каждый раз не создавать 
    процесс, создаём и запускаем его перед циклом"""
    process = Process(target=getData, args=(queue,))
    process.start()
    while True:
        try:
            str = input("Введите число и степень(через пробел), в которую нужно возмести число: ")
            number, pow = (str.split(' '))# получаем значения от пользователя
            numberInInt: int = int(number)
            powInInt: int = int(pow)
            dataCarteg = [numberInInt, powInInt]
            queue.put(dataCarteg)
        except:
            print("Ошибка ввода!")
