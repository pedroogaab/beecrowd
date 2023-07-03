"O(n^2)"

n = int(input())

branco = 0
preto = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if j%2 != 0 and i%2 != 0:
            branco += 1
            
        elif j%2 != 0 and i%2 == 0:
            preto += 1            
            
        elif j != 0 and i&2 == 0:
            branco += 1
            
        else: preto += 1
        
print(f'{branco} casas brancas e {preto} casas pretas')

