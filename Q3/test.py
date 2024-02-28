from threading import Thread
import time

def outp():
    while True:
        print('Hello')
        time.sleep(2)

def inp():
    while True:
        value = input("Enter a value:")

if __name__ == '__main__':
    out_thread = Thread(target=outp)
    in_thread = Thread(target=inp)
    out_thread.start()
    in_thread.start()
