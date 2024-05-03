from crunes import *

input_folder = "rune-sentences/"
filenames = ["00.txt","03.txt","08.txt","15.txt","23.txt","27.txt",
             "33.txt","40.txt","54.txt"]

out1_folder = "pseudo-sentences/"
out2_folder = "pseudo-labeled/"

def convert_file(fn):

    file = open(input_folder + fn, encoding = 'utf8')
    text = ""
    for m in file:
        text += m
    file.close()

    out1 = ""
    out2 = ""
    n = 0

    for line in text.split('\n'):
        #add label to each non-empty line.
        #some formatting-only lines might be .....
        if len(line) > 0:
            out1 += fn.split('.')[0] +' ' + str(n) + ':' + line
            out2 += fn.split('.')[0] +' ' + str(n) + ':'

            for char in line:
                #print(char)
                if char in runes:
                    out2 += pseudo[ runes.index(char) ]
                else:
                    out2 += char
            
            n += 1
        else:
            out1 += line
            out2 += line
        out1 += '\n'
        out2 += '\n'

    file = open(out1_folder + fn, 'w', encoding = 'utf8')
    print(out1, file=file)
    file.close()

    file = open(out2_folder + fn, 'w', encoding = 'utf8')
    print(out2, file=file)
    file.close()

    
for f in filenames:
    convert_file( f )


