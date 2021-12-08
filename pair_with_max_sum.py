#Найти пару элементов, расположенных на расстоянии
#не меньшем k, с максимальной суммой

n, k = map(int, input().split())

mem = [int(input()) for i in range(k)]
mx = -int(1e9)
sm = -int(1e9)
for i in range(k, n):
    a = int(input())
    if mem[i % k] > mx:
        mx = mem[i % k]
    mem[i % k] = a
    if a + mx > sm:
        sm = a + mx
print(sm)
