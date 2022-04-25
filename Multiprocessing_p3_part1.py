# importing the modules
from threading import *		
import time		

# creating thread instance where count = 3
obj = Semaphore(3)		

# creating instance
def display(name):	
	
	# calling acquire method
	obj.acquire()				
	for i in range(5):
		print('Hello, ', "round: " ,i,'' ,  end = '')
		time.sleep(1)
		print(name)
		
		# calling release method
		obj.release()	
		
# creating multiple thread
thread1 = Thread(target = display , args = ('Thread-1',))
thread2 = Thread(target = display , args = ('Thread-2',))
thread3 = Thread(target = display , args = ('Thread-3',))
thread4 = Thread(target = display , args = ('Thread-4',))
thread5 = Thread(target = display , args = ('Thread-5',))

# calling the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

# References: <author(s) GeekforGeeks (2020) Semaphore source code (Version 1.0) [Source code]. GeekforGeeks.com
