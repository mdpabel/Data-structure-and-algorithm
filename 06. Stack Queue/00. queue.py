from collections import deque

#FIFO

queue = deque()
queue.append(1)
queue.append(2)

queue.popleft()

print(queue)