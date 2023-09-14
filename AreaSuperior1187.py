ex = input()
soma = True

val = 0
repet = 0

if ex == "M":
    soma = False

x = 0
y = 11

for i in range(12):
    for n in range(12):
        a = float(input())
        if n > x and n < y:
            repet += 1
            val += a
    x+=1
    y-=1

if soma:
    print(f'{val:.1f}')
else: print(f'{val/repet:.1f}')
        
        