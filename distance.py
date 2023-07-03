n1 = input()
n2 = input()

x1, y1 = n1.split(' ')
x1 = float(x1)
y1 = float(y1)

x2, y2 = n2.split(' ')
x2 = float(x2)
y2 = float(y2)

distance = (((x2-x1)**2) + ((y2-y1)**2))**0.5

print(f'{distance:.4f}')