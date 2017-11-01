
def table(seq, sanity_check = False):
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

            if a==s1_len:

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

            if b==s2_len:

                return a-b

        elif a==0:

            b=b+1

        else:
            a=fail1[a-1]+1

    return None             


def rc(s):



    rvs=s[::-1]



    cmpl={'a':'t','t':'a','c':'g','g':'c'}



    base=[cmpl[base]for base in rvs]



    return ''.join(base)







seqs1, seqs2, seq, seqid = [], [], '', ''



for line in open ('sample.fasta'):



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







result_file=file ('sample_unitig.txt','w')


tlist=[]
seqs=seqs1+seqs2
rlist=range(len(seqs))
f=0
while rlist!=[]:
    olist=[rlist[0]]
    f=f+1
    unitig=seqs[rlist[0]][1]
    if rlist[0]<len(seqs1):
        order=[[0,seqs[rlist[0]][0],'F']]
    else:
        order=[[0,seqs[rlist[0]][0],'R']]
    for n in range(1,len(rlist)):
        if rlist[n] <len(seqs1):
            over=getoverlap(unitig,seqs[rlist[n]][1])
            if over!=None:
                olist.append(rlist[n])
                if over>=0:
                    unitig=unitig[:(over-1)]+seqs[rlist[n]][1]
                    order.append([over,seqs[rlist[n]][0],'F'])
                else:
                    unitig=seqs[rlist[n]][1][:(-1-over)]+unitig
                    for m in range(len(order)):
                        order[m][0]=order[m][0]-over
                    order.append([0,seqs[rlist[n]][0],'F'])
        else:
            over=getoverlap(unitig,seqs[rlist[n]][1])
            if over!=None:
                olist.append(rlist[n])
                if over>=0:
                    unitig=unitig[:(over-1)]+seqs[rlist[n]][1]
                    order.append([over,seqs[rlist[n]][0],'R'])
                else:
                    unitig=seqs[rlist[n]][1][:(-1-over)]+unitig
                    for m in range(len(order)):
                        order[m][0]=order[m][0]-over
                    order.append([0,seqs[rlist[n]][0],'R'])

    order=sorted(order, key=lambda x:x[0])
    order[0].append(0)
    tlist.append('%s\t%02d\t%i\t%i'%('UNI',f,len(olist)+1,len(unitig)))
    tlist.append('%s\t%s\t%s'%('ReadID','Direction','Offset'))
    tlist.append('%s\t%s\t%s'%(order[0][1],order[0][2],order[0][3]))
    for i in range(1,len(order)):
        offset=order[i][0]-order[i-1][0]
        order[i].append(offset)
        tlist.append('%s\t%s\t%i'%(order[i][1],order[i][2],order[i][3]))
    del rlist[0]
    rlist=[x for x in rlist if x not in olist]



for item in tlist:
    result_file.write('%s\n'%item)





