#Отрезок массива с мксимальной суммой элементов (элементы - целые)
n = int(input())
a = list(map(int, input().split()))

sums = [0] * (n + 1)
for i in range(1, n + 1):
    sums[i] = sums[i - 1] + a[i - 1]
    
razn = a[0]
razn_left = 1
razn_right = 1
mni = 0
for i in range(1, n + 1):
    if sums[i] - mn > razn:
        razn = sums[i] - sums[mni]
        razn_left = mni + 1
        razn_right = i
    if sums[i] < sums[mni]:
        mni = i
print(razn, razn_left, razn_right)
