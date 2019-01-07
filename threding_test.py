import threading 
import time

def square(num):
    print("Inside square function")
    time.sleep(5)
    print(num * num)

def multiply(num1,num2):
    print("Inside multiply function")
    print(num1 * num2)
    
# square(10)
# multiply(10,20)

t1 = threading.Thread(target= square,args=(10,))
t2 = threading.Thread(target= multiply,args= (5,6))
t3 = threading.Thread(target= square,args=(15,))

t1.start()
t2.start()
t3.start()