# Создание потоков

from time import sleep, time
import threading

def write_words(word_count, file_name):
        with open(file_name, 'w') as file:
            for i in range(1, word_count + 1):
                file.write(f"Какое-то слово № {i}\n")
                sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")

start_time_1 = time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time = time()
print(f"Работа основных функций заняла: {end_time - start_time_1:.6f} секунд")

threads = []
start_time_2= time()

args = [
    (10, "example5.txt"),
    (30, "example6.txt"),
    (200, "example7.txt"),
    (100, "example8.txt")
]

for arg in args:
    thread = threading.Thread(target=write_words, args=arg)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = time()
print(f"Работа потоков заняла: {end_time_threads - start_time_2:.6f} секунд")