__author__ = 'kyhwana'

#TODO: output MD5/SHA1/other hashes of output sentences
#TODO: randomly generate sentances, specify how many to generate.
#TODO: add max output length. Make max output length either cut off words or not output sentences more than <x>
#TODO: Output to stdout vs output to file.
#TODO: do we assume that they words don't repeat??
import os
import sys
import argparse
import string
import itertools




def makesentence(words):
    mswordcount = len(words)
    if debug: print(mswordcount)
    sentence = ""
    inwordcount = 0
    for word in words:
        #if we don't check what word we're on, we end up with the modifier on the end of the sentence.
        inwordcount += 1
        if debug: print( inwordcount)
        if inwordcount == mswordcount:
            sentence = sentence + word
        else:
            sentence = sentence + word + modifier

    return(sentence)

debug=0

parser = argparse.ArgumentParser(description="XKCD style password generator")
parser.add_argument('-d', help="dict <filename of dictionary>", required=True)
parser.add_argument('-wc', help="Number of words in sentence", required=False, default='4')
parser.add_argument('-m', help="Modifier", required=False, default='')

opts = vars(parser.parse_args())

dictionaryfile = opts.pop('d')
wordcount = opts.pop('wc')
modifier = opts.pop('m')
if debug: print(dictionaryfile)
if debug: print(wordcount)

words = [line.strip() for line in open(dictionaryfile)]

for nwords in range(0,int(wordcount)):
    for word in itertools.product(words,repeat=int(wordcount)):
        if (debug): print(word)
        print(makesentence(word))

#for firstword in words:
#    wordlist = []
#    wordlist.append(firstword)
    #We already have the first word, so wordcount-1
#    for wordlistcreatecount in range(0,wordcount-1):

