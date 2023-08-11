l = []

while True:
    try:
        l.append(input())
        
    except EOFError: #Gera este erro quando nao tem mais dados dentro do arquivo que esta sendo acessado
        break
        
l = set(l) #set vira um dicionario e pega o elemento apenas uma vez, se repetir ele nao pega mais. EX: {"A", "a", "2", "1"}
print(len(l))