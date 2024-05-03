from crunes import *
import random

#lol

def lol(fn):
    file = open("lengths/"+fn+".txt",'r')
    
    st = ""
    for m in file:
        st += m
    file.close()

    sn = st.split('\n')#split sentences

    #fun time
    
    sr = ""
    sevenflag = False
    #split : [1] pls
    for line in sn:
        if ':' in line:
            splt = line.split(':')
            sr += splt[0] + ':'
            #print(splt[1].split(' '))
            for n in splt[1].split(' '):
                if n != '':#man
                    match n[0]:
                        case '7':
                            sr += '7'#chance to transform next L1 into th...
                            sevenflag = random.choice([False,False,True])
                        case 'L':
                            if n == 'L1' and sevenflag:
                                sr += ' t'#keep the spacing consistent for now
                                sevenflag = False
                            #pick random from...
                            else:
                                sr += random.choice( list(wordict[n].values())) + ' '
                        case ' ':
                            if not sevenflag: sr += ' '
                        case _:
                            sr += n + ' '
        sr+='\n'
    print(sr)

lol('03')
