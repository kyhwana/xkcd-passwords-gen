__author__ = 'kyhwana'

#TODO: randomly generate sentances, specify how many to generate.
#TODO: add max output length. Make max output length either cut off words or not output sentences more than <x>
#TODO: Output to stdout vs output to file.
import os
import sys
import argparse
import string
import itertools
import hashlib
import io
from collections import Counter

def makesentence(words):
    mswordcount = len(words)
    if debug: print(mswordcount)


    sentence = ""
    inwordcount = 0
    for word in words:
        #if we don't check what word we're on, we end up with the modifier on the end of the sentence.
        inwordcount += 1
        if debug: print(inwordcount)
        if inwordcount == mswordcount:
            sentence = sentence + word
        else:
            sentence = sentence + word + modifier
    if hashalgo:
        return hashsentence(sentence) + hasspasswordseperator + sentence
    else:
        return sentence

def hashsentence(sentence):
    hashin = hashlib.new(hashalgo[0])
    hashin.update(sentence.encode())
    return hashin.hexdigest()

debug=0

parser = argparse.ArgumentParser(description="XKCD style password generator")
parser.add_argument('-d', help="<filename of dictionary>", required=True)
parser.add_argument('-wc', help="<Number of words in sentence>", required=False, default='4')
parser.add_argument('-m', help="<Modifier>", required=False, default='')
parser.add_argument('-r', help="Repeating words ", required=False, dest='repeats',action='store_true')
parser.add_argument('-nr', help="No repeating words ", required=False, dest='repeats',action='store_false')
parser.add_argument('-hash', help="Hash with <algorithm>", required=False, nargs=1)
parser.add_argument('-o',help="Output file <file>", required=False)
parser.set_defaults(repeats=False)

#pull the arguments from the parser
opts = vars(parser.parse_args())
dictionaryfile = opts.pop('d')
wordcount = opts.pop('wc')
modifier = opts.pop('m')
repeatwords = opts.pop('repeats')
hashalgo = opts.pop('hash')
outputfile = opts.pop('o')

#hash/password seperator. This is only used if we are hashing.
hasspasswordseperator = ":"
if debug:
    print(hashlib.algorithms_available)
    print(hashlib.algorithms_guaranteed)

if debug: print(dictionaryfile)
if debug: print(wordcount)
if debug: print(repeatwords)
if debug: print(hashalgo)
#pull all the words from our dictionary file, strip the CR/LF's off the word, bung them into "words" as a list.
words = [line.strip() for line in open(dictionaryfile)]
if outputfile:
    try:
        with open(outputfile, "w") as outputfilehandle:
            pass
    except IOError as e:
        print("IOERROR ", e)
        exit()
    outputfilehandle = open(outputfile, "w")

for nwords in range(0,int(wordcount)):
    for word in itertools.product(words,repeat=int(wordcount)):
        if (debug): print(word)
        #Lets see if we have any repeated words.
        repeatedwords = False
        for checkword in word:
            checkwordcount = max(Counter(word).values())
            if debug: print("checkwordcount=%s",checkwordcount)
            if checkwordcount > 1:
                repeatedwords = True
        if repeatwords == False and repeatedwords == True:
            #Do nothing. We don't want repeated words.
            if debug: print("Doing nothing, not allowed repeating words.")
        else:
            if outputfile:
                #We need the \n if we want each sentence on a different line :|
                outputfilehandle.write(makesentence(word) + "\n")
            else:
                print(makesentence(word))
if outputfile:
    outputfilehandle.close()


