#Префиксные суммы.
#Дан массив и m запросов вида:
#найти сумму элементов с L по R

n = int(input())
a = list(map(int, input().split()))
sums = [0] * (n + 1)
for i in range(1, n + 1):
    sums[i] = sums[i - 1] + a[i - 1]
m = int(input())
for i in range(m):
    l, r = map(int, input().split())
    print(sums[r] - sums[l - 1])
