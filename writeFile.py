from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# создадим класс Observer-а с мотодом выполняющимся при условии выполнения каких либо дейстивий в объекте
class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
            with open("wfile.txt", "r") as file:
                print(file.readlines()[-1])


observer = Observer()
observer.schedule(Watcher(), path="C:\\Users\\kolpa\\PycharmProjects\\FourthTaskPython")
observer.start()
try:
    while 1:
        pass
except KeyboardInterrupt:
    observer.stop()
    print("Наблюдение завершино!")
