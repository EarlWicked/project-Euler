#euler 14
megisto = 0
for i in range (1000000, 1, -1):
    temp = i
    deiktis = 1
    
    while temp > 1:
        if temp%2 == 0:
            temp= temp/2
        else:
            temp = 3*temp +1
        deiktis = deiktis + 1

        
    if deiktis > megisto :
            megisto = deiktis
            arithmos = i

print ("megaluteri seira %s gia arithmo %s", megisto, arithmos)
            
