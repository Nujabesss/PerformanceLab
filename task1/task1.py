import sys
n = int(sys.argv[1])
m = int(sys.argv[2])
arr = [i + 1 for i in range(n)] 
path=''
start = 0
while True:
    current = arr[start]
    path+=str(current)
    end = (start + m - 1) % n
    if arr[end] == arr[0]:
        break
    start = end
print(path)