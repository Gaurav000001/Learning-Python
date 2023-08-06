# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"
from queue import *

st = LifoQueue()

def push(n):
    st.put(n)
    
push(2)
push(3)

while not st.empty():
    print(st.get())
    
q = PriorityQueue()

q.put(20)
q.put(303)
q.put(40)

while not q.empty():
    print (q.get())