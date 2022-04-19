import multiprocessing
  
def populate_queue(Students, queue):
    """
    function to square a given list
    """
    # append students to queue
    for student in Students:
        queue.put(student)
  
def print_queue(queue):
    """
    function to print students in queue
    """
    print("Queue elements:")
    while not queue.empty():
        print(queue.get())
    print("Queue is now empty!")
  
if __name__ == "__main__":
    # input list
    Students = ["Kim", "John", "Sarah", "Jim", "Kevin", "Pam"]
    print("We'll be transferring our list into the queue and then print it!")
  
    # creating multiprocessing Queue
    queue = multiprocessing.Queue()
    
     # creating new processes
    p1 = multiprocessing.Process(target=populate_queue, args=(Students, queue))
    p2 = multiprocessing.Process(target=print_queue, args=(queue,))
  
    # running process p1 to append to queue
    p1.start()
    p1.join()
  
    # running process p2 to get queue elements
    p2.start()
    p2.join()
