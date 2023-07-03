"O(n)"

n = int(input())

n1 = int(n/2) + 1
n2 = n1 - 1

branco = 0
preto = 0

if n%2 != 0:
    for i in range(1, n+1):
        if i%2 != 0:
            branco += n1
            preto += n2

        else:
            preto += n1
            branco += n2
else: 
    tamanho = n**2
    
    branco = int(tamanho/2)
    preto = int(tamanho/2)
        
print(f"{branco} casas brancas e {preto} casas pretas")

