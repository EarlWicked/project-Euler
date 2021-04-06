upol =0
maxi=0
for j in range (0,6008513):
      upol=0
      for i in range(1,j):
            if j%i==0:
                  upol =upol +1
                  
            if upol>1:
                  break

      if upol ==1:
            print (j)
            


print ('largest prime factor is %d' %maxi)
