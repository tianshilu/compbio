from datetime import datetime, date, time

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

    if sanity_check:
        for f in range(len(fail)):
            f_value = fail[f]
            for f2 in range(f_value+1):
                # " a  c a c"
                # "-1 -1 0 1"
                # "        ?"
                if seq[f - f_value + f2] != seq[f2]:
                    print "at %d: f_value of %d" % (f, f_value)
                    print "seq[%d]=%s vs. seq[%d]=%s" % (f - f_value + f2, seq[f - f_value + f2], f2, seq[f2])
                    for p in range(0, len(seq), 30):
                        s2_print, fail_print = "", ""
                        for s in range(p, p + 30):
                            s2_print += ("  %s" % seq[s])
                            fail_print += ("%3d" % fail[s])
                        print s2_print
                        print fail_print
                    assert False
                    
                    
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
'''
def simple_overlap(s1, s2):
    # Implement the brute-force overlap function
    s1_len,s2_len=len(s1),len(s2)

    for p in range(s1_len):

        same=True

        for q in range(s2_len-p):

            if s1[p+q]!=s2[q]:

                same=False

                break

        if same:

            offset=p

            length=s2_len-p

            if length >= 40:
                return offset

    for q in range(s2_len):

        same=True

        for p in range(s1_len-q):

            if s1[p]!=s2[p+q]:
                same=False

                break

        if same:

            offset=q

            length=s2_len-q

            if length >= 40:
                    return 0-offset


    return None

'''


def rc(s):

    rvs=s[::-1]

    cmpl={'a':'t','t':'a','c':'g','g':'c'}

    base=[cmpl[base]for base in rvs]

    return ''.join(base)



seqs1, seqs2, seq, seqid = [], [], '', ''

for line in open ('lab01.fasta'):

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



result_file=file ('sample_KMP.txt','w')


result=[]





for s1 in range(len(seqs1)):

    s1_id=seqs1[s1][0]
    #print "%s - %s" % (str(datetime.now()), s1_id)

    for s2 in range(s1+1,len(seqs2)):

        s2_id=seqs2[s2][0]

        over1=getoverlap(seqs1[s1][1],seqs1[s2][1])
        over2=getoverlap(seqs1[s1][1],seqs2[s2][1])
'''
        sanity_check = True
        if sanity_check :
            over1_cmp=simple_overlap(seqs1[s1][1],seqs1[s2][1])
            over2_cmp=simple_overlap(seqs1[s1][1],seqs2[s2][1])
        if over1!=over1_cmp:
            print over1,over1_cmp,seqs1[s1][0],seqs1[s2][0]
        if over2!=over2_cmp:
            print [over2,over2_cmp,seqs1[s1][0],seqs2[s2][0]]
        assert over1==over1_cmp
        assert over2==over2_cmp
'''
        
        #print '%s-%s_%s'%(str(datetime.now()),s1_id,s2_id)
        
        if over1!=None:

            result.append('%s\t%s\tF\t%i'%(s1_id,s2_id,over1))

        if over2!=None:

            result.append('%s\t%s\tR\t%i'%(s1_id,s2_id,over2))

result_file.write('Seq1ID'+'\t'+'Seq2ID'+'\t'+'overlap_len'+'\t'+'Direction'+'\t'+'Offset'+'\n')

for item in result:

    result_file.write('%s\n'%item)


