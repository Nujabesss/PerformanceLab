import sys
file = sys.argv[1]
arr = []
with open(file, 'r') as file:
    numbers = file.read().split()
    arr = [int(num) for num in numbers]

nums = len(arr)
s = sum(arr)
mid = int(s / nums)
count = 0

for i in range(nums):
    while arr[i] != mid:
        if arr[i] > mid:
            arr[i] -= 1
        else:
            arr[i] += 1
        count += 1

print(count)