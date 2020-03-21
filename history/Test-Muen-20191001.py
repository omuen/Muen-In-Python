m=[8,6,8,9,9,1,1,9,9,5,9,1,5,2,5,4,6,8,1,7,6,1,3,6,4,9,7,2,8,5]
maxvalue = len(m)
o = 0
while(o<maxvalue):
    i=0
    while(i<maxvalue-o-1):
        x = m[i]
        # print(x, m[i+1])    
        if(x>m[i+1]):
            m[i]=m[i+1]
            m[i+1]=x
        i=i+1

    o=o+1


for v in m:
    print(v)
