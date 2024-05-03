from crunes import *

divinity = "DIVINITY"
firf = "FIRFVMFERENFE"

#00 atbash
file = open('rune-solved/00.txt', encoding = 'utf8')
text = ""
for m in file:
    text += m
file.close()

out = ""

for char in text:
    if char in runes:
        out += atb(char)
    else:
        out += char

print(out)
print('\n')

#03 vignere 'divinity' with skips...
file = open('rune-solved/03.txt', encoding = 'utf8')
text = ""
for m in file:
    text += m
file.close()

out = ""
k = 0

for char in text:
    if char in runes:
        out += sub(char, divinity[k])
        k = (k+1)%8
    else:
        out += char
print(out)
print('\n')

#05 runic plaintext
file = open('rune-solved/05.txt', encoding = 'utf8')
text = ""
for m in file:
    text += m
file.close()

out = ""

for char in text:
    if char in runes:
        out += pseudo[identify(char)]
    else:
        out += char

print(out)
print('\n')

#06 atbash plus caesar
file = open('rune-solved/06.txt', encoding = 'utf8')
text = ""
for m in file:
    text += m
file.close()

out = ""

for char in text:
    if char in runes:
        c = atb(char)
        out += add(c,3)
    else:
        out += char

print(out)
print('\n')

#10 runic plaintext ...
file = open('rune-solved/10.txt', encoding = 'utf8')
text = ""
for m in file:
    text += m
file.close()

out = ""

for char in text:
    if char in runes:
        out += pseudo[identify(char)]
    else:
        out += char

print(out)
print('\n')

#14 vignere 'firfumferenfe' with skips...
file = open('rune-solved/14.txt', encoding = 'utf8')
text = ""
for m in file:
    text += m
file.close()

out = ""
k = 0

for char in text:
    if char in runes:
        out += sub(char, firf[k])
        k = (k+1)%len(firf)
    else:
        out += char
print(out)
print('\n')

#unsolved 56, vignere with running prime-totient stream, with skip
#skip[ is just baked into prime stream as a 1
someprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
          67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
          139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
          211, 223, 227, 229, 233, 239, 241, 251, 257, 263,
              1, 269, 271, 277,
          281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
          449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
          547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619,
          631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719,
          727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821,
          823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
          919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

file = open('rune-solved/56.txt', encoding = 'utf8')
text = ""
for m in file:
    text += m
file.close()

out = ""
k = 0

for char in text:
    if char in runes:
        out += sub(char, someprimes[k]-1)
        k +=1
    else:
        out += char
print(out)
print('\n')

#unsolved 57, plain text
file = open('rune-solved/57.txt', encoding = 'utf8')
text = ""
for m in file:
    text += m
file.close()

out = ""

for char in text:
    if char in runes:
        out += pseudo[identify(char)]
    else:
        out += char

print(out)
print('\n')
