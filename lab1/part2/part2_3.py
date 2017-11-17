f=file('/home2/s171162/work/compbio/lab1/part1_KMP.txt')
part1=[]

for i in f:
    i=i.split('\t')
    i[3]=i[3].replace('\r\n','')
    if int(i[3])<0:
        if i[2]=='F':
            a=i[0]
            i[0]=i[1]
            i[1]=a
            i[3]=0-int(i[3])
            part1.append(i)
        else:
            i[3]=0-int(i[3])
            i.insert(3,'F')
            b=i[0]
            i[0]=i[1]
            i[1]=b
            part1.append(i)
    else:
        part1.append(i)

edge=[]
redu=[]

for j in part1:
    if len(j)==4:
        j.insert(2,'F')
for eg in part1:
    edge.append([eg[0],eg[1],eg[2],eg[3]])

for m in range(len(part1)):
    o=part1[m][0]
    b=part1[m][1]
    ldir=part1[m][2]
    rdir=part1[m][3]
    n=m+1
    while n<len(part1):
        if part1[n][1]==o and part1[n][3]==ldir:
            a=part1[n][0]
            ldir=part1[n][2]
            if ldir=='R' and rdir=='R':
                a=b
                b=part1[n][0]
                ldir,rdir='F','F'
            if [a,b,ldir,rdir] in edge and [a,b,ldir,rdir] not in redu:
                redu.append([a,b,ldir,rdir])
#                if a=='035' or b=='035':
#                    print part1[m],part1[n],[a,b,ldir,rdir,1]
            elif [b,a,ldir,rdir] in edge and ldir=='R' and rdir=='F' and [b,a,ldir,rdir] not in redu:
                redu.append([b,a,ldir,rdir])
#                if b=='035' or a=='035':
#                    print part1[m],part1[n],[b,a,ldir,rdir,2]
            elif [b,a,ldir,rdir] in edge and ldir=='F' and rdir=='R' and [b,a,ldir,rdir] not in redu:
                redu.append([b,a,ldir,rdir])
#                if b=='035' or a=='035':
#                    print part1[m],part1[n],[b,a,ldir,rdir,3]
            n+=1
            b=part1[m][1]
            ldir,rdir=part1[m][2],part1[m][3]
        elif part1[n][0]==b and part1[n][2]==rdir:
            c=part1[n][1]
            rdir=part1[n][3]
            if ldir=='R' and rdir=='R':
                c=o
                o=part1[n][1]
                ldir,rdir='F','F'
            if [o,c,ldir,rdir] in edge and [o,c,ldir,rdir] not in redu:
                redu.append([o,c,ldir,rdir])
#                if o=='035' or c=='035':
#                    print part1[m],part1[n],[o,c,ldir,rdir,4]
            elif [c,o,ldir,rdir] in edge and ldir=='R' and rdir=='F' and [c,o,ldir,rdir] not in redu:
                redu.append([c,o,ldir,rdir])
#                if c=='035' or o=='035':
#                    print part1[m],part1[n],[c,o,ldir,rdir,5]
            elif [c,o,ldir,rdir] in edge and ldir=='F' and rdir=='R' and [c,o,ldir,rdir] not in redu:
                redu.append([c,o,ldir,rdir])
#                if o=='035' or c=='035':
#                    print part1[m],part1[n],[c,o,ldir,rdir,6] 
            n+=1
            o=part1[m][0]
            ldir,rdir=part1[m][2],part1[m][3]
        elif part1[n][1]==b and [ldir,rdir,part1[n][2],part1[n][3]]!=['F','F','F','F'] and [ldir,rdir,part1[n][2],part1[n][3]]!=['R','F','F','F'] :
            if rdir==part1[n][2]:
                c=part1[n][0]
                rdir=part1[n][3]
                if ldir=='R' and rdir=='R':
                    c=o
                    o=part1[n][1]
                    ldir,rdir='F','F'
                if [o,c,ldir,rdir] in edge and [o,c,ldir,rdir] not in redu:
                    redu.append([o,c,ldir,rdir,])
#                    if o=='035' or c=='035':
#                        print part1[m],part1[n],[o,c,ldir,rdir,7]
                elif [c,o,ldir,rdir] in edge and ldir=='R' and rdir=='F' and [c,o,ldir,rdir] not in redu:
                    redu.append([c,o,ldir,rdir])
#                    if c=='035' or o=='035':
#                        print part1[m],part1[n],[c,o,ldir,rdir,8]
                elif [c,o,ldir,rdir] in edge and ldir=='F' and rdir=='R' and [c,o,ldir,rdir] not in redu:
                    redu.append([c,o,ldir,rdir])
#                    if c=='035' or o=='035':
#                        print part1[m],part1[n],[c,o,ldir,rdir,9]
            elif ldir=='F' and rdir=='R' and part1[n][2]=='F' and part1[n][3]=='F':
                c=part1[n][0]
                rdir='R'
                if [o,c,ldir,rdir] in edge and [o,c,ldir,rdir] not in redu:
                        redu.append([o,c,ldir,rdir])
#                        if o=='035' or c=='035':
#                            print part1[m],part1[n],[c,o,ldir,rdir,10]
                elif [c,o,ldir,rdir] in edge and [c,o,ldir,rdir] not in redu:
                        redu.append([c,o,ldir,rdir])
#                        if o=='035' or c=='035':
#                            print part1[m],part1[n],[c,o,ldir,rdir,11]
            n+=1
            o=part1[m][0]
            ldir,rdir=part1[m][2],part1[m][3]
        elif part1[n][0]==o and [ldir,rdir,part1[n][2],part1[n][3]]!=['F','F','F','F'] and [ldir,rdir,part1[n][2],part1[n][3]]!=['F','F','F','R']:
            if rdir==part1[n][2]:
                c=part1[n][1]
                o=part1[m][1]
                rdir=part1[n][3]
                if ldir=='R' and rdir=='R':
                    c=o
                    o=part1[n][1]
                    ldir,rdir='F','F'
                if [o,c,ldir,rdir] in edge and [o,c,ldir,rdir] not in redu:
                        redu.append([o,c,ldir,rdir])
#                        if o=='035' or c=='035':
#                            print part1[m],part1[n],[o,c,ldir,rdir,12]
                elif [c,o,ldir,rdir] in edge and ldir=='R' and rdir=='F' and [c,o,ldir,rdir] not in redu:
                        redu.append([c,o,ldir,rdir])
#                        if o=='035' or c=='035':
#                            print part1[m],part1[n],[c,o,ldir,rdir,13]
                elif [c,o,ldir,rdir] in edge and ldir=='F' and rdir=='R' and [c,o,ldir,rdir] not in redu:
                    redu.append([c,o,ldir,rdir])
#                    if o=='035' or c=='035':
#                        print part1[m],part1[n],[c,o,ldir,rdir,14]
            elif ldir=='F' and rdir=='F' and part1[n][2]=='R' and part1[n][3]=='F':
                c=part1[m][1]
                o=part1[n][1]
                rdir=part1[n][3]
                ldir='R'
                if [o,c,ldir,rdir] in edge and [o,c,ldir,rdir] not in redu:
                        redu.append([o,c,ldir,rdir])
#                        if o=='035' or c=='035':
#                            print part1[m],part1[n],[o,c,ldir,rdir,15]
                elif [c,o,ldir,rdir] in edge and [c,o,ldir,rdir] not in redu:
                        redu.append([c,o,ldir,rdir])
#                        if o=='035' or c=='035':
#                            print part1[n],part1[m],[c,o,ldir,rdir,16]

            n+=1
            o=part1[m][0]
            ldir,rdir=part1[m][2],part1[m][3]
        else:
            n+=1


for q in redu:
    for p in part1:
        if q==[p[0],p[1],p[2],p[3]]:
            part1.remove(p)
print len(redu),len(part1)
for item in part1:
    if item[0]=='040' or item[1]=='040':
        print item
num=len(part1)
for b in range(0,num):
    if part1[b][2]=='F' and part1[b][3]=='F':
        part1.append([part1[b][1],part1[b][0],'R','R',part1[b][4]])
    elif part1[b][2]=='F' and part1[b][3]=='R':
        part1.append([part1[b][1],part1[b][0],'F','R',part1[b][4]])
    elif part1[b][2]=='R' and part1[b][3]=='F':
        part1.append([part1[b][1],part1[b][0],'R','F',part1[b][4]])


uni_list,mono=[],[]
while part1!=[]:
    uni=[part1[0]]
    a=part1[0][0]
    b=part1[0][1]
    ad=part1[0][2]
    bd=part1[0][3]
    q,nex,bef=0,[],[]
    for re in part1:
        if re[0]==part1[0][1] and re[1]==part1[0][0]:
            part1.remove(re)
    for u in part1:
        ml,mr,mll,mrr,end=0,0,0,0,0
        if u[1]==part1[0][1] and u[3]==part1[0][3] and u!=part1[0]:
            part1.remove(u)
            for ele in part1:
                if ele[0]==u[1] and ele[1]==u[0] and ele in part1:
                    part1.remove(ele)
                elif ele[0]==u[1] and ele[2]==u[3]:
                    mr+=1
            for el in part1:
                if el[1]==part1[0][0] and el[3]==part1[0][2]:
                    mrr+=1
            if mr==0 or mr>1:
                if part1[0][1] not in mono:
                    mono.append(part1[0][1])
                    uni_list.append('%s\t%s\t%i'%(part1[0][1],part1[0][3],0))
            if mrr==0 and part1[0][0] not in mono:
                mono.append(part1[0][0])
                uni_list.append('%s\t%s\t%i'%(part1[0][0],part1[0][2],0))
            q=len(part1)
            uni=None
        elif u[0]==part1[0][0] and u[2]==part1[0][2] and u!=part1[0]:
            part1.remove(u)
            for elem in part1:
                if elem[0]==u[1] and elem[1]==u[0] and elem in part1:
                    part1.remove(elem)
                elif elem[1]==u[0] and elem[3]==u[2]:
                    ml+=1
                elif elem[0]==u[1] and elem[2]==u[3]:
                    end+=1
            if end==0 and u[1] not in mono:
                mono.append(u[1])
                uni_list.append('%s\t%s\t%i'%(u[1],u[3],0))
            for element in part1:
                if element[0]==part1[0][1] and element[2]==part1[0][3]:
                    mll+=1
            if ml==0 or ml>1:
                if part1[0][0] not in mono:
                    mono.append(part1[0][0])
                    uni_list.append('%s\t%s\t%i'%(part1[0][0],part1[0][2],0))
            if mll==0 and part1[0][1] not in mono:
                mono.append(part1[0][1])
                uni_list.append('%s\t%s\t%i'%(part1[0][1],part1[0][3],0))
            q=len(part1)
            uni=None
    part1.pop(0)
    while q<len(part1):
        if b==part1[q][0] and bd==part1[q][2]:
            if part1[q] not in nex:
                nex.append(part1[q])
                q+=1
            else:
                q+=1
        elif a==part1[q][1] and ad==part1[q][3]:
            if part1[q] not in bef:
                bef.append(part1[q])
                q+=1
            else:
                q+=1
        else:
            q+=1
        if q==len(part1):
            if len(nex)==1:
                next=nex.pop(0)
                q,mul,mulen,nex,lef=0,[],[],[],0
                for h in part1:   
                    if h[1]==next[1] and h[3]==next[3] and h!=next:
                        mulen.append(h)
                    elif h[0]==next[1] and h[2]==next[3]:
                        mul.append(h)
                part1.remove(next)
                for j in part1:
                    if j[0]==next[1] and next[0]==j[1]:
                        part1.remove(j)
                if len(mulen)==0:
                    uni.append(next)
                    b=next[1]
                    bd=next[3]
                elif len(mulen)>0:
                    for m in mulen:
                        part1.remove(m)
                        for n in part1:
                            if n[0]==m[1] and n[1]==m[0]:
                                part1.remove(n)
                            if n[1]==m[0] and n[3]==m[2]:
                                lef+=1
                        if lef==0 and m[0] not in mono:
                            uni_list.append('%s\t%s\t%i'%(m[0],m[2],0))
                    if len(mul)==0 and  next[1] not in mono:
                        mono.append(next[1])
                        uni_list.append('%s\t%s\t%i'%(next[1],next[3],0))
                    elif len(mul)>1 and next[1] not in mono:
                        mono.append(next[1])
                        uni_list.append('%s\t%s\t%i'%(next[1],next[3],0))
                        for r in mul:
                            part1.remove(r)
                            for s in part1:
                                if r[0]==s[1] and r[1]==s[0]:
                                    part1.remove(s)
                    b='rightend'
                    bd='rightendir'
            elif len(nex)>1:                
                for x in nex:
                    part1.remove(x)
#                    print 'remove5',x
                    mc=0
                    for y in part1:
                        if y[0]==x[1] and y[1]==x[0]:
                            part1.remove(y)
#                            print 'remove6',y
                        elif y[0]==x[1] and y[2]==x[3]:
                            mc+=1
                    if mc==0 and x[1] not in mono:
                        mono.append(x[1])
                        uni_list.append('%s\t%s\t%i'%(x[1],x[3],0))
                b='rightend'
                bd='rightendir'
                nex=[]
            if len(bef)==1:
                befo=bef.pop(0)
                q,mull,mu,bef,rig=0,[],[],[],0
                for g in part1:
                    if g[0]==befo[0] and g[2]==befo[2] and g!=befo:
                        mull.append(g)
                    elif g[1]==befo[0] and g[3]==befo[2]:
                        mu.append(g)
                part1.remove(befo)
                for s in part1:
                    if s[0]==befo[1] and s[1]==befo[0]:
                        part1.remove(s)
                if len(mull)==0:
                    uni.insert(0,befo)
                    a=befo[0]
                    ad=befo[2]
#debug
                    if a=='269':
                        print befo,uni,mull,mu
                elif len(mull)>0:
                    for c in mull:
                        part1.remove(c)
                        for d in part1:
                            if c[0]==d[1] and c[1]==d[0]:
                                part1.remove(d)
#                                print 'remove10',d
                            if d[0]==c[1] and d[2]==c[3]:
                                rig+=1
                        if rig==0 and c[1] not in mono:
                            mono.append(c[1])
#                            print 'c',c
                            uni_list.append('%s\t%s\t%i'%(c[1],c[3],0))
                        rig=0
                    if len(mu)==0 and befo[0] not in mono:
                        mono.append(befo[0])
                        uni_list.append('%s\t%s\t%i'%(befo[0],befo[2],0))
                    elif len(mu)>1:
                        mono.append(befo[0])
                        uni_list.append('%s\t%s\t%i'%(befo[0],befo[2],0))
                        for j in mu:
                            part1.remove(j)
                            for k in part1:
                                if j[0]==k[1] and j[1]==k[1]:
                                    part1.remove(k)
                    a='leftend'
                    ad='leftendir'            
            elif len(bef)>1:
                for e in bef:
                    part1.remove(e)
#                    print 'remove11',e
                    md=0
                    for f in part1:
                        if f[0]==e[1] and f[1]==e[0]:
                            part1.remove(f)
#                            print 'remove12',f
                        elif f[1]==e[0] and f[3]==e[2]:
                            md+=1
                    if md==0 and e[0] not in mono:
                        mono.append(e[0])
                        uni_list.append('%s\t%s\t%i'%(e[0],e[2],0))
                a='leftend'
                a='leftendir'
                bef=[]
    if uni!=None:
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





