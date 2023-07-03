"O(n^2)"

n = int(input())

branco = 0
preto = 0

for i in range(n):
    for j in range(n):
        if j%2 == 0 and i%2 == 0:
            branco += 1
              
        elif j%2 != 0 and i%2 != 0:
            branco += 1
            
            
        elif j%2 == 0 and i%2 != 0:
            preto += 1            
            
        elif j%2 != 0 and i%2 == 0:
            preto += 1
        
print(f'{branco} casas brancas e {preto} casas pretas')

