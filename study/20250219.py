#서술형 출제 자주 됨

#stack(LIFO)
st=list()
# st=[]
st.append(2)
st.append(3)
st.append(4)
st.append(5)
test = st.pop()
st.pop()
print(st)

#queue(FIFO)
q=list()

q.append(3)
q.append(4)
q.append(5)
q.append(6)
q.append(7)
q.pop(0)
test=q.pop(0)
print(q)


#이걸 사용
from collections import deque
q=deque()
q.append(5)
q.append(15)
q.append(25)
q.append(35)
q.append(45)
print(q)
print(list(q))
q.popleft()
q.popleft()
print(list(q))


#거의 안 씀
import queue
q=queue.Queue()
q.put(5)
q.put(15)
q.put(25)

q.get()
print(q)
print(q.queue)