
lel=0
g=0
temp=0
a=b=c=0

for a in range (1,1000):
            if lel==1:
                  break
            for b in range (1,a):
                  
                  if lel==1:
                        break
                        for c in range (1,b):
                              g= b**2 + c**2
                              temp = a+b+c                              
                              g1=a**2
                              if (g1==g or temp==1000):
                                    print ("temp is " ,temp)
                                    lel=1
                                    break

temp=a*b*c
print ("a= ", a)
print ("b= ", b)
print ("c= ", c)
                  
