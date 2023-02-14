#Printing tasks

# Consider the following situation in a computer science laboratory.
# On any average day about 10 students are working in the lab at any given hour.
# These students typically print up to twice during that time, and the length of these tasks ranges from 1 to 20 pages.
# The printer in the lab is older, capable of processing 10 pages per minute of draft quality.
# The printer could be switched to give better quality, but then it would produce only five pages per minute.
# The slower printing speed could make students wait too long. What page rate should be used?

from random import randint

class Queue():
    def __init__(self):
        self.l=list()
        self._size = 0

    def size(self):
        return self._size

    def enqueue(self,item):
        self._size = self._size + 1
        self.l.append(item)

    def dequeue(self):
        if self._size > 0:
            self._size = self._size - 1
            return self.l.pop(0)

    def is_empty(self):
        return self._size == 0

printtasks = Queue()
currentsecond = 0
pages_per_minute = 5
seconds_per_page = 60 / pages_per_minute
waiting_time_ALL = []

taskpending = False
busy = False

while currentsecond < 3600:
    currentsecond += 1
    if randint(1,180) == 1: #new task happening
        pages = randint(1,20)
        print(f"{currentsecond}: New task with {pages} pages")
        printtasks.enqueue((currentsecond,pages))

    if not busy and not printtasks.is_empty():
        busy = True
        starttime, pages = printtasks.dequeue()
        current_task_waited_for = currentsecond - starttime
        if current_task_waited_for != 0:
            waiting_time_ALL.append(current_task_waited_for)
        print(f"{currentsecond}: Task with {pages} pages is being printed, waited for {current_task_waited_for} seconds")
        timeremaining = pages*seconds_per_page

    elif busy and timeremaining > 0:
        timeremaining -= 1
        if timeremaining == 0:
            print(f"{currentsecond}: Task completed")
            busy = False

average = sum(waiting_time_ALL)/len(waiting_time_ALL)
#print(f"{currentsecond}: Average wait time: {average} seconds")
print(f"{currentsecond}: Average wait time: {int(average//60)}:{int(average%60)}")
tasksleft = 0
while not printtasks.is_empty():
    printtasks.dequeue()
    tasksleft += 1
print(f"{currentsecond}: Tasks left: {tasksleft}")
