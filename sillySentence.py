from random import *
nouns = ("james","gabe","brian","gulermo","androoz","sabooboobear")
adjectives = ("sussy","baka","imposter","stinky","fun","weird")
verbs = ("ran","commited vehicular homicide against","ate","told","gamed","rekt")
nonLen = len(nouns) -  1
adjLen = len(adjectives) - 1
verLen = len(verbs) - 1
noun = nouns[randrange(0,nonLen)]
adjective = adjectives[randrange(0,adjLen)]
verb = verbs[randrange(0,verLen)]
noun1 = nouns[randrange(0,nonLen)]
adjective1 = adjectives[randrange(0,adjLen)]
verb1 = verbs[randrange(0,verLen)]
print(noun, verb, "the", adjective, noun1,"")