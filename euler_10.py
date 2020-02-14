upol=0
sums=0

for j in range (0,2000000):
      upol=0
      for i in range(1,j):
            if j%i==0:
                  upol =upol+1
                  
            
            if upol>1:
                  
                  break
      if upol==1:
            sums=sums+j
            
            

