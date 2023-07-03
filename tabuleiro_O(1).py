"O(1)"

n = int(input())

branco = 0
preto = 0

tamanho = n**2

if n %2 == 0:
    branco = int(tamanho/2)
    preto = branco
    
else: 
    branco = int((tamanho+1)/2)
    preto = branco - 1

print(f'{branco} casas brancas e {preto} casas pretas')

