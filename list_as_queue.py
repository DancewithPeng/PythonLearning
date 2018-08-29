# list也可以作为队列，但是请不要这么做，因为在入列时性能非常低下，每个元素需要移动一个位置
# 如需要用到队列，请 collections.deque 来实现
from collections import deque

# 初始化队列
Q = deque(['I', 'am', 'a', 'coder'])
print(Q)

# 入列
Q.append('Hello')
print(Q)

# 出列
e = Q.popleft()
print(e, Q)