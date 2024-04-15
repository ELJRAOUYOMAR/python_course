#It is possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”)
#learn more about collection.deque  https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


queue = deque(['Ahmed','Yasser','Ali'])
queue.append('Omar')  # Omar arrives
queue.popleft()   # The first to arrive now leaves('Ahmed')

print(queue)