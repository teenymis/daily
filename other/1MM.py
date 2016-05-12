c=0
def ff(n):
    global c
    c=c+1
    if n==1:
        return 1
    if n%2==0:
        return ff(n/2)
    else:
        return ff(n*3+1)
#listx=[]
#listz=[]
addict = {}
for i in range(1,1000001):
    ff(i)
    addict[i] = c
    #listx.append(str(c)+'.'+str(i))
    #listz=[float(j) for j in listx]
    #print i , c
    c=0
#print listx
#print max(listz)
print(max(addict.items(), key=lambda x: x[1]))
