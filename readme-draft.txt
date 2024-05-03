The Liber Primus is an unsolved cipher manuscript produced by the mysterious Cicada 3301. It uses a unique rune-based substitution alphabet combined with (at least in the solved pages) a variety of combinations of atbash, Caesar and vignere ciphers. The vast majority of the manuscript remains unsolved, mysterious and impenetrable. This repository contains a variety of python files for poking and prodding at the text, attempting to wring something, anything out of it, that might help access the solution.--


Folders
rune-sentences: Unsolved pages, runic form, separated by sentence.
pseudo-sentences: Unsolved pages converted to the "pseudo-readable" alphabet.
pseudo-labeled: Unsolved pages converted to "pseudo-readable" with sentences labeled.
rune-solved: Solved pages in runic.

The transcriptions are sourced from https://github.com/scream314/cicada3301/blob/master/liber_primus.md


Files
crunes.py
Alphabets, basic functions.

convertor.py
Converts the runic transcriptions to as ASCII alphabet that's kind of readable if the underlying text isn't encrypted beyond having been converted to runes. Makes the text easier to manipulate without worrying about encoding. Also generates the labeled-sentence files. So any changes to the underlying transcriptions can easily be propagated... or changes to the alphabet. I've been told that using parentheses for those two letters is not very good.

solved.py
Solves the already-solved pages using their known solutions. This includes pages 56 and 57 from the otherwise unsolved sections, whoch is why they're labeled as "unsolved" despite being, you know, solved.

buffer.py
One of the most interesting things about the unsolved pages is the statistical lack of doublets. The easiest way to explain this is some kind of autokey cipher where the amout of "f" runes (first in the runic alphabet, so a value of zero) in the text before autokeying is low. In fact Cicada has played with "f" rune before, so them engineering text to have low "f"s isn't unthinkable. This file undoes the presumed autokey encryption. It doesn't really reveal anything, but there it is anyway.

wordconverter.py
Converts words to runic form. The dictiomary used for brute force attempts was made using this and a selection of Cicada's writings, to get likely vocabuary. Some assumptions are made about certain problem points- for example, is the word "aeon" processed as ae-o-n or a-eo-n? A converter that works in alphabetical order ar Mprtlach's does will convert the 'eo' first, while one that goes through the word letter-by-letter as mine does would convert the 'ae' first.
This can be even worse. For example if the letters "aeoe" somehow ended up in plaintext, would that be turned into "ae-oe" or "a-eo-e"? The runic length is ambiguous! Cicada pls

brute.py
Low-quality brute-force tester.

cribpoints.py
Program for crib-testing various "points of interest", sentences where some clear limit is placed on what the underlying text can be. Includes a sentence from a solved page that used a vignere cipher to demonstrate that it actually works.

lengths.py
Converts unsolved pages into word-length things. needs apostrophe fix

decribulator.py
Comedy crib generator. Randomly picks matching words by length.