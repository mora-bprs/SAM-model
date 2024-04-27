# Main thread waits until all the threads finish executing 

import threading
import time

# Function to print "Hello", with a 2-second sleep at the 11th iteration
def print_hello():
    for i in range(20):
        if i == 10:
            time.sleep(2)
        print("Hello")

# Function to print numbers till a given number
def print_numbers(num):
    for i in range(num + 1):
        print(i)

# Main program
print("Greetings from the main thread.")

# Creating threads with target functions and arguments
thread1 = threading.Thread(target=print_hello, args=())
thread2 = threading.Thread(target=print_numbers, args=(10,))

# Starting the two threads
thread1.start()
thread2.start()

# Waiting for threads to finish execution
thread1.join()
thread2.join()

print("It's the main thread again!")
print("Threads 1 and 2 have finished executing.")
