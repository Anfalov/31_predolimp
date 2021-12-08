from collections import deque

a = list(map(int, input().split()[1:]))
n = len(a)

right_lower = [n] * n
st = deque()
st.append(0)

for i in range(1, n):
    while len(st) and a[st[-1]] > a[i]:
        right_lower[st[-1]] = i
        st.pop()
    st.append(i)

left_lower = [-1] * n
st = deque()
st.append(n - 1)

for i in range(n - 1, -1, -1):
    while len(st) and a[st[-1]] > a[i]:
        left_lower[st[-1]] = i
        st.pop()
    st.append(i)

mx = 0
for i in range(n):
    cur = a[i] * (right_lower[i] - left_lower[i] - 1)
    mx = max(mx, cur)
print(mx)
