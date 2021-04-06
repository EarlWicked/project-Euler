
sums=0
temp = 0
i=1
j=i

while i<= 4000000:
     
      temp=i
      i = i+j
      j= temp
      if  i%2 ==0:
            sums = sums+i

print (sums)
      
