while True:
    try: 
        n = input().split()
        
        a = int(n[0])
        b = int(n[1])
        c = int(n[2])
        
        end = 12*12
        dist = (end + (a*a))**0.5 # hipotenusa
        
        temp_ladrao = 12/b        
        temp_guarda = dist/c
        
        if temp_guarda <= temp_ladrao:
            print("S")
        else: print("N")
        
    except: break