import sys
circle=sys.argv[1]
dot=sys.argv[2]
def number(x,y,x1,y1):
    return  (x-x1)**2+(y-y1)**2
cord_cirle=[]
file = open(circle, 'r', encoding='utf-8')
cord_cirle = []
while True:
    char = file.read(1)
    if not char:
        break
    if char.isdigit():
        cord_cirle.append(char)
x=int(cord_cirle[0])
y=int(cord_cirle[1])
r=int(cord_cirle[2])
for line in open(dot):
    x1, y1= map(float, line.split(' '))
    if number(x,y,x1,y1)>r**2:
        print(2)
    elif number(x,y,x1,y1)==r**2:
        print(0)
    else:
        print (1)
 
