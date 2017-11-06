f=file('/home2/s171162/work/compbio/lab1/part1_KMP.txt')
part1=[]
for i in f:
    i=i.split('\t')
    i[3]=i[3].replace('\r\n','')
    if int(i[3])<0:
        a=i[0]
        i[0]=i[1]
        i[1]=a
        i[3]=0-int(i[3])
        part1.append(i)
    else:
        part1.append(i)

edge=[]
redu=[]
for j in part1:
    edge.append([j[0],j[1]])
for m in range(len(part1)):
    o=part1[m][0]
    b=part1[m][1]
    mdir=part1[m][2]
    n=m+1
    while n<len(part1):
        left,right='',''
        if part1[n][1]==o and part1[n][2]=='F':
            a=part1[n][0]
            if [a,b] in edge and [a,b] not in redu:
                redu.append([a,b])

#                if a=='001' or b=='001':
#                   print 'left',[a,b]
#                    print part1[n],part1[m]
            else:
                left=part1[n][0]
            n+=1
        elif part1[n][0]==b and mdir=='F':
            c=part1[n][1]
            if [o,c] in edge and [o,c] not in redu:
                redu.append([o,c])
             #   if o=='001' or c=='001':
              #      print 'right',[o,c]
               #     print part1[m],part1[n]
            else:
                right=part1[n][1]
            n+=1
        else:
            n+=1
        if n==len(part1) and left!='':
            o=left
            n=m+1
        if n==len(part1) and right!='':
            b=right
            n=m+1
for q in redu:
    for p in part1:
        if q==[p[0],p[1]]:
            part1.remove(p)
#debug
'''
print part1,len(part1)
eg=[]
for e in part1:
    eg.append(e[0])
    eg.append(e[1])
print sorted(eg)
#debug
'''
num=len(part1)
for b in range(0,num):
    part1[b].insert(-2,'F')
    if part1[b][3]=='F':
        part1.append([part1[b][1],part1[b][0],'R','R',part1[b][4]])
    else:
        part1.append([part1[b][1],part1[b][0],'F','R',part1[b][4]])

uni_list=[]
while part1!=[]:
    uni=[part1[0]]
    a=part1[0][0]
    b=part1[0][1]
    ad=part1[0][2]
    bd=part1[0][3]
    for u in part1:
        if u[0]==part1[0][1] and u[1]==part1[0][0]:
            part1.remove(u)
    part1.pop(0)
    m,n,q=0,0,0
    nex,bef='',''
    while q<len(part1):
        if b==part1[q][0] and bd==part1[q][2]:
            if part1[q]!=nex:
                m+=1
                nex=part1[q]
                q+=1
            else:
                q+=1
        elif a==part1[q][1] and ad==part1[q][3]:
            if part1[q]!=bef:
                n+=1
                bef=part1[q]
                q+=1
            else:
                q+=1
        else:
            q+=1
        if q==len(part1):
            if m==1:
                b=nex[1]
                bd=nex[3]
                uni.append(nex)
                part1.remove(nex)
                q,m=0,0
                for h in part1:
                    if h[0]==nex[1] and h[1]==nex[0]:
                        part1.remove(h)
                    elif h[1]==nex[1] and h[3]==nex[3] and nex in uni:
                        uni.pop(-1)
                        b='rightend'
                        bd='rightenddir'
                        part1.remove(h)
                        mulr,mul=0,[]
                        for k in part1:
                            if k[0]==h[1] and k[1]==h[0]:
                                part1.remove(k)
                            elif k[0]==nex[1] and k[2]==nex[3]:
                                mulr+=1
                                mul.append(k)
                        if mulr>1:
                            uni_list.append('%s\t%s\t%i'%(nex[1],nex[3],0))
                            for l in mul:
                                part1.remove(l)
                                for r in part1:
                                    if l[0]==r[1] and l[1]==r[0]:
                                        part1.remove(r)
                        elif mulr==0:
                            uni_list.append('%s\t%s\t%i'%(nex[1],nex[3],0))
                                                    
            elif m>1:
                q+=1
            if n==1:
                a=bef[0]
                ad=bef[2]
                uni.insert(0,bef)
                part1.remove(bef)
                q,n=0,0
                for g in part1:
                    if g[0]==bef[1] and g[1]==bef[0]:
                        part1.remove(g)
                    elif g[0]==bef[0] and g[2]==bef[2] and nex in uni:
                        uni.pop(0)
                        a='leftend'
                        ad='leftenddir'
                        part1.remove(g)
                        mul,mu=0,[]
                        for s in part1:
                            if s[0]==g[1] and s[1]==g[0]:
                                                part1.remove(s)
                            elif s[1]==bef[0] and s[3]==bef[2]:
                                                mul+=1
                                                mu.append(s)
                        if mul>1:
                            uni_list.append('%s\t%s\t%i'%(bef[0],bef[2],0))
                            for t in mul:
                                part1.remove(t)
                                for v in part1:
                                    if t[0]==v[1] and t[1]==v[0]:
                                        part1.remove(v)
                        elif mul==0:
                            uni_list.append('%s\t%s\t%i'%(bef[0],bef[2],0))
            elif n>1:
                q+=1
    uni_list.append(uni)
    
tlist=[]
num=0
for item in uni_list:
    len_uni=0
    num+=1
    if isinstance(item,str):
        print item
        tlist.append('%s\t%02d\t%i\t%i'%('UNI',num,1,500))
        tlist.append(item)
    else:
        for f in item:
            len_uni+=int(f[4])
        tlist.append('%s\t%02d\t%i\t%i'%('UNI',num,len(item)+1,len_uni+500))
        for e in item:
            if e==item[0]:
                tlist.append('%s\t%s\t%i'%(e[0],e[2],0))
                tlist.append('%s\t%s\t%i'%(e[1],e[3],int(e[4])))
            else:
                tlist.append('%s\t%s\t%i'%(e[1],e[3],int(e[4])))    
result_file=file('/home2/s171162/work/compbio/lab1/part2_uni.txt','w')

for o in tlist:
    result_file.write('%s\n'%o)





