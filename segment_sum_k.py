#Отрезок в массиве с суммой равной k
n = int(input())
k = int(input())
a = list(map(int, input().split()))
sm = a[0]
l, r = 0, 0
while r < n - 1 or sm > k:
    if sm > k:
        sm -= a[l]
        l += 1
    elif sm < k:
        r += 1
        sm += a[r]
    if sm == k:
        break
if sm == k:
    print(l + 1, r + 1)
    
