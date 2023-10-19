while True:
    try:
        i = int(input())
        
        botas_e = [0]*61
        botas_d = [0]*61
        
        val = 0
        
        for a in range(i):
            b = str(input()).split()

            if b[1] == "D":
                botas_d[int(b[0])] += 1 
            else: 
                botas_e[int(b[0])] += 1 
                
                
        for a, b in zip(botas_e, botas_d):
            while True:
                if a >= 1 and b >= 1:
                    val += 1
                    
                    a -= 1
                    b -= 1
                else: break
            
        print(val)

    except: break      
            
