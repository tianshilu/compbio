pa2f=file('/home2/s171162/work/compbio/lab1/part2_uni.txt')
seqf=file('/home2/s171162/work/compbio/lab1/lab01.fasta')

seqs1, seqs2, seq, seqid = [], [], '', ''
def rc(s):

    rvs=s[::-1]

    cmpl={'a':'t','t':'a','c':'g','g':'c'}

    base=[cmpl[base]for base in rvs]

    return ''.join(base)

for line in seqf:

    line=line.strip()

    if line.startswith('>'):

        if seq!='':

            seqs1.append([seqid, seq])

            seqs2.append([seqid, rc(seq)])

        seqid=line[1:]

        seq=''

    else:

        seq=seq+line

seqs1.append([seqid, seq])

seqs2.append([seqid, rc(seq)])

unif=[]

for lin in pa2f:
    unif.append(lin)
unitig,uni,unid,unitigid,lenth=[],'',[],[],0
for p in range(len(unif)):
    pinfo=unif[p].split('\t')
    if unif[p].startswith('UNI'):
        if uni!='':
            unitig.append(uni)
            unitigid.append(unid)
            uni,unid,lenth='',[],0
    elif pinfo[1]=='F':
        lenth+=int(pinfo[2])
        unid.append([pinfo[0],pinfo[1],lenth])
        if p!=len(unif)-1 and unif[p+1].startswith('UNI'):
            for a in seqs1:
                if a[0]==pinfo[0]:
                    uni+=a[1]
        elif p==len(unif)-1:
            for a in seqs1:
                if a[0]==pinfo[0]:
                    uni+=a[1]
        else:
            nex=unif[p+1].split('\t')
            l=int(nex[2])
            for a in seqs1:
                if a[0]==pinfo[0]:
                    uni+=a[1][0:l]
    elif pinfo[1]=='R':
        lenth+=int(pinfo[2])
        unid.append([pinfo[0],pinfo[1],lenth])
        if p!=len(unif)-1 and unif[p+1].startswith('UNI'):
            for b in seqs2:
                if b[0]==pinfo[0]:
                    uni+=b[1]
        elif p==len(unif)-1:
            for b in seqs2:
                if b[0]==pinfo[0]:
                    uni+=b[1]
        else:
            nex=unif[p+1].split('\t')
            l=int(nex[2])
            for b in seqs2:
                if b[0]==pinfo[0]:
                    uni+=b[1][0:l]
    if p==len(unif)-1:
        unitig.append(uni)
        unitigid.append(unid)

def table(seq):
    fail=[-1]
    i,j=1,0
    while i<= len(seq)-1:
        if seq[i]==seq[j]:
            fail.append(j)
            i=i+1
            j=j+1
        elif j==0:
             fail.append(-1)
             i=i+1
        else:
                j=fail[j-1]+1
                if seq[i]==seq[j]:
                    fail.append(j)
                    i=i+1
                    j=j+1
    return fail
def getoverlap(s1,s2):
    s1_len,s2_len=len(s1),len(s2)
    a,b=0,0
    fail2=table(s2)
    while a < s1_len and b < s2_len-1:
        if s1[a]==s2[b]:
            a=a+1
            b=b+1
            if b>=40 and a==s1_len:
                return a-b
        elif b==0:
            a=a+1
        else:
            b=fail2[b-1]+1

    a,b=0,0
    fail1=table(s1)
    while a<=s1_len-1 and b<=s2_len-1:
        if s1[a]==s2[b]:
            a=a+1
            b=b+1
            if a>=40 and b==s2_len:
                return a-b
        elif a==0:
            b=b+1
        else:
            a=fail1[a-1]+1
    return None             

funi,runi,unit,i,ovuni=[],[],'',0,[]
for e in unitig:
    i+=1
    unid=i
    funi.append([unid, e])
    runi.append([unid, rc(e)])
for s1 in range(len(funi)):
    s1_id=funi[s1][0]
    for s2 in range(s1+1,len(runi)):
        s2_id=runi[s2][0]
        over1=getoverlap(funi[s1][1],funi[s2][1])
        over2=getoverlap(funi[s1][1],runi[s2][1])
        if over1>0:
            ovuni.append('%s\t%s\tF\t%i'%(s1_id,s2_id,over1))
        elif over1<0 and over1!=None:
            ovuni.append('%s\t%s\tF\t%i'%(s2_id,s1_id,-over1))
        if over2>0:
            ovuni.append('%s\t%s\tR\t%i'%(s1_id,s2_id,over2))
        elif over2<0 and over2!=None:
            ovuni.append('%s\t%s\tRF\t%i'%(s2_id,s1_id,-over2))
print 'ovuni',ovuni
nonpair=[]
for d in ovuni:
    mate=d.split('\t')
    m,n=int(mate[0])-1,int(mate[1])-1
    for p in unitigid[m]:
        if int(p[0]) %2==1:
            for q in unitigid[n]:
                if int(q[0])==int(p[0])+1:
                    if mate[2]=='F':
                        if q[1]!=p[1]:
                            distance=int(mate[3])-int(p[2])+int(q[2])
                            if distance<1900 or distance>3100:
                                if mate not in nonpair:
                                    nonpair.append(mate)
                                    print '1',distance,p,q,mate
                        elif mate not in nonpair:
                            nonpair.append(mate)
                            print '2',distance,p,q,mate
                    elif mate[2]=='R':
                        for w in funi:
                            if int(mate[1])==int(w[0]):
                                L=len(w[1])
                        if q[1]==p[1]:
                            distance=L+int(mate[3])-int(p[2])-int(q[2])
                            if distance<2400 or distance>3600:
                                if mate not in nonpair:
                                    nonpair.append(mate)
                                    print '3',distance,p,q,mate
                        elif mate not in nonpair:
                            nonpair.append(mate)
                            print '4',distance,p,q,mate
                    else:
                        for w in funi:
                            if int(mate[0])==int(w[0]):
                                L=len(w[1])
                        if q[1]==p[1]:
                            distance=int(mate[3])+int(p[2])+int(q[2])-L
                            if distance<1400 or distance>2600:
                                if mate not in nonpair:
                                    nonpair.append(mate)
                                    print '5',distance,p,q,mate
                        elif mate not in nonpair:
                            nonpair.append(mate)
                            print '6',distance,p,q,mate
print nonpair

pair=[]
for e in ovuni:
    mat=e.split('\t')
    if mat not in nonpair:
        pair.append(mat)
print 'pair',pair

