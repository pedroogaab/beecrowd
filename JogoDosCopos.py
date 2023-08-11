a = int(input())
init = str(input())

if init == "A":
    pos = "A"
elif init == "B":
    pos = "B"
else: pos = "C"


def posicao(mov, pos):
    if mov == 1:
        if pos == "A":
            pos = "B"
            
        elif pos == "B":
            pos = "A"

        
    elif mov == 2:
        if pos == "B":
            pos = "C"
            
        elif pos == "C":
            pos = "B"
            
    else:
        if pos == "A":
            pos = "C"
            
        elif pos == "C":
            pos = "A"
            
    return pos

    
for i in range(a):
    mov = int(input())
    
    pos = posicao(mov, pos)
    
        
print(pos)