value = 0
repet = 0
while True:
    a = int(input())
    if a < 0:
        break
    repet += 1
    value += a
    
print(f'{value/repet:.2f}')