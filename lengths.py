from crunes import *

infolder = "pseudo-labeled/"
outfolder = "lengths/"
filenames = ["00.txt","03.txt","08.txt","15.txt","23.txt","27.txt",
             "33.txt","40.txt","54.txt"]

def convert(fn):
    file = open(infolder + fn,'r')
    text = ""
    for m in file:
        text += m
    file.close()
    
    #length engine
    L = 0
    strn=""
    ex=""
    apos = ""
    #now line by line
    for line in text.split('\n'):
        snor = line.split(':')
        #print(snor)

        if len(snor) > 1:#should be [line num, line]
            strn += snor[0] +':'
            for char in snor[1]:#add: ...
                if char in '12345':
                    strn += char+'- '
                elif char == '7':
                    strn += '7 '# '7th'
                elif char == "'":#words w/ ' draw from sept 'La' dict
                    apos = "a"
                elif char in pseudo:
                    L += 1
                else:#'-' or end of line means end of word
                    if char in '\"-':
                        if L > 0:
                            strn += 'L'+apos+str(L)+ ' '
                            L = 0
                            apos = ""
                    if char in "./&%$\"":
                        strn += char + ' '
                    else:
                        if char != '-': ex += char
        #strn += last word
        if L > 0:
            strn += 'L'+apos+str(L)+ ' '
            L = 0
            apos = ""
        strn += '\n'
            
    print(ex + ' ex')
    #print(fn)
    file = open(outfolder + fn,'w')
    print(strn,file=file)#to file
    file.close()


for f in filenames:
    convert( f )
