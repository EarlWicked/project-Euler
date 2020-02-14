#polu argos kwdikas
upol=0
j=0
temp=0
while True:
      j=j+1
      upol=0
      for i in range(1,j):
            if j%i==0:
                  upol =upol +1
            if upol>1:
                  break

      if upol ==1:
            temp= temp+1
            
      if temp==10001:
            break




print (j)
