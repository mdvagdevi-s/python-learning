from collections import deque
d=deque([10,20,30])
d.append(40)
d.appendleft(5)
d.popleft()
d.appendleft(5)
d.pop()


print(d)