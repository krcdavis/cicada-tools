runes   = ["ᚠ", "ᚢ",  "ᚦ", "ᚩ", "ᚱ",  "ᚳ", "ᚷ", "ᚹ", "ᚻ", "ᚾ", "ᛁ",  "ᛄ",  "ᛇ",
           "ᛈ", "ᛉ", "ᛋ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ",   "ᛝ",  "ᛟ", "ᛞ", "ᚪ",  "ᚫ",
           "ᚣ",  "ᛡ",  "ᛠ"]
pseudo  = ["F", "V",  "t", "O", "R", "C", "G", "W", "H", "N", "I", "J",  "e",
           "P", "X", "S", "T", "B", "E", "M", "L",  "g",  "o", "D", "A",  "(",
           "Y",  "i",  ")"]


#to add: things like 'U' and 'V' both returning pseudo.index('V'), 'C'/'K' etc
def identify(char):#key specifically might also just be int
    if char in pseudo:
        return pseudo.index(char)
    if char in runes:
        return runes.index(char)
    if isinstance(char, int):
        #print(char)
        return char
    return 0


def add(a,b):
    return pseudo[ (identify(a) + identify(b))%29 ]

def sub(a,b):
    return pseudo[ (identify(a) - identify(b) +29)%29 ]

def atb(ch):
    return pseudo[ (28 - identify(ch)) ]

def rlen(word):
    l = 0
    for char in word:
        if char in runes or char in pseudo:
            l += 1
    return l
