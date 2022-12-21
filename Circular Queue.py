queue = [0]*10

startPointer = 0
endPointer = -1
queueFull = 10
queueLength = 0

def enQueue(item):
    global queueLength, endPointer
    if endPointer < queueFull:
        if endPointer < len(queue) -1:
            endPointer += 1
        else:
            endPointer = 0
        queueLength += 1
        queue[endPointer] = item
    if endPointer == 0:
        print('Queue is full, cannot enqueue')
        
def deQueue():
    global queueLength, startPointer
    if queueLength == 0:
        print("Queue is empty, cannot dequeue")
    else:
        queue[startPointer] = 0
        if startPointer == len(queue) -1:
            startPointer = 0
        else:
            startPointer += 1
    queueLength -= 1
    
enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)
print(queue)

deQueue()
deQueue()
deQueue()
deQueue()
print(queue)

enQueue(1)
enQueue(1)
print(queue)
        
