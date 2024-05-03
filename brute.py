from crunes import *


#shortened wordlist for brutal, since words 3-4 chars and below tend to show
#up by chance too easily
brutedict = {
    'L4': wordict['L4'],
    'L5': wordict['L5'],
    'L6': wordict['L6'],
    'L7': wordict['L7'],
    'L8': wordict['L8'],
    'L9': wordict['L9'],
    'L10': wordict['L10'],
    'L11': wordict['L11'],
    'L12': wordict['L12'],
    'L13': wordict['L13'],
    'L14': wordict['L14']
}



#try to vignere-decode text with a key, using all "rotations" of the key. so
#like divinity, ivinityd, vinitydi,... ydivinit... this accounts for skips
def vig_section(text, key):
    k = 0
    q = len(key)

    arreys = []
    for m in range(0,q):
        arreys.append('')

    for char in text:
        if char in pseudo or char in runes:
            for m in range(0,q):
                arreys[m] += sub( char, key[(k+m)%q])
            k = (k+1)%q
        else:
            for m in range(0,q):
                arreys[m] += char
    #print(arreys)
    return arreys


def brute_text(text, key, n):
  #takes a single piece of text, so a single [] of arrey
  #key and n are just used to label the outcome so you can put in whatever
    for dic in brutedict:
      for word in brutedict[dic]:#isolate word
        worb = ['-'+word+'-',#this is missing some combos. fix it later
                '.'+word+'-',
                '-'+word+'.',
                ' '+word+' ',
                '.'+word+' ',
                ' '+word+'.',
                '•'+word+'•',
           ]
        for worg in worb:
          #assume text is a sentence:labeled page
          for line in text.split('\n'):
            if line.find(worg) >0:
              print(key,n,word,'  ',line)

def brute_vig_section(text, key):
    q = len(key)
    arreys = vig_section(text, key)

    #brute
    #for n in arreys call brute_text
    for ay in range( len(arreys) ):
      #print(ay)
      brute_text(arreys[ay], key, ay)



file = open('rune-solved/03.txt','r', encoding = 'utf8')
text = ""
for m in file:
    text+=m
file.close()

brute_vig_section(text,'DIVINITY')


file = open('rune-solved/14.txt','r', encoding = 'utf8')
text = ""
for m in file:
    text+=m
file.close()

brute_vig_section(text,'FIRFVMFERENFE')


