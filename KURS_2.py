import time
def Z2(m: list[int]):
    l = len(m)
    if l==0 : return m
    elif l==1 : return m
    else:
        if l%2==0: a=l/2
        else: a=(l-1)/2+1
        mr = list()
        ml = list()
        for i in range(0,l):
            if m[i]>m[int(a)]:
                mr.append(m[i])
            else:
                ml.append(m[i])
        mr_t = mr
        ml_t = ml
        return Z2(ml_t) + Z2(mr_t)

LIST = list(range(1000, 0, -1))
time_s = time.time()
slist = Z2(LIST)
time_e = time.time()
print(slist)
print(time_e-time_s)

    
n=0
LIST.sort()
for i in range(0, len(LIST)):
    if slist[i]-LIST[i] != 0 :
        n+=1
        print(slist[i], LIST[i])
if(n==0): print("sorted")


