sumsquer=0
squersum=0


for i in range(0,101):
      temp= i*i
      sumsquer= sumsquer+temp
      squersum= squersum+i

squersum= squersum*squersum

dif= squersum - sumsquer

print (dif)
