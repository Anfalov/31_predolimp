#Блиайший меньший (больший) слева / справа для каждого эемента массива

from collections import deque

n = int(input())
a = list(map(int, input().split()))

right_lower = [n] * n #для каждого элемента храним номер ближайшего меньшего справа
st = deque()
st.append(0)

for i in range(1, n):
    while len(st) and a[st[-1]] > a[i]: # "<", если хотим номер большего
        right_lower[st[-1]] = i
        st.pop()
    st.append(i)
    
print(*right_lower)


left_lower = [-1] * n #для ближайшего меньшего слева всё тоже самое, только с обходом в обратную сторону
st = deque()
st.append(n - 1)

for i in range(n - 2, -1, -1):
    while len(st) and a[st[-1]] > a[i]:
        left_lower[st[-1]] = i
        st.pop()
    st.append(i)

print(*left_lower)
