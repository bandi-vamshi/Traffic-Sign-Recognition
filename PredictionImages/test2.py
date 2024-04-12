#python prgrams on important topic mulithreading or multiprocessing
import threading
def even(num):
    for value in range(num):
        if value%2==0:
            print(f"even numbers {value}")

def odd(num):
    for value in range(num):
        if value%2!=0:
            print(f'even numbers {value}')

obj1=threading.Thread(target=even(20))
obj2=threading.Thread(target=odd(20))
obj1.start()
obj2.start()
