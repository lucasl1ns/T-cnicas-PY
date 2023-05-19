while True:
    try:
        m, n = input().split()
        m, n = int(m), int(n)
        
        fat_m = 1
        for i in range(1, m + 1):
            fat_m *= i
    
        fat_n = 1
        for i in range(1, n + 1):
            fat_n *= i
    
        print(fat_m + fat_n)
    except:
        break

