from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q) 
q.popleft()
print(q) 

#pallindrome using queue 

def pal(string):
    d = deque(string)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True 
print(pal("madam")) 

#implement stack using queue 

stack = deque()
stack.append("python")
stack.append("java")
stack.append("c")
print(stack) 
stack.pop() #lifo 
print(stack) 


dq = deque([1, 2, 3, 4, 5])

dq.rotate(2)  # Rotate right by 2
print("After right rotation:", dq)

dq.rotate(-3)  # Rotate left by 3
print("After left rotation:", dq)

#maxlen 

dq1 = deque(maxlen=3)
dq1.append(1)
dq1.append(2)
dq1.append(3)
dq1.append(4) #now removes 1 and insert the 4 

print(dq1) 

#count freq for queue 

from collections import Counter 

dq2 = deque('sivaaa')

freq = Counter(dq2) 
print(freq) 