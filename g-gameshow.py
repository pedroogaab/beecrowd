n = int(input()) #quantidade de caixas

val = 100

results = []
results.append(val)
for a in range(n):
    np = int(input())
    val += np
    results.append(val)
    
print(max(results))