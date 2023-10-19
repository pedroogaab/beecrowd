n = int(input()) #quantidade de caixas


ord_ = int(input()) #primeiro valor que define a ordem

val = 100

ord = abs(ord_)

if ord_ >= 0:
    val += ord

for a in range(n-1):
    np = int(input())
    
    if np >= 0:
        val += ord
            
print(val)