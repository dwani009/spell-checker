# -*- coding: utf-8 -*-
"""
@author: Dhiraj
"""
import re
import os, sys
import operator
import enchant
import threading

from difflib import get_close_matches 

pathname, scriptname = os.path.split(sys.argv[0])
enchantDict = enchant.Dict('en_US')
word = {} 
outputWord =''
wordfreq = {}
matchRes = []

def createDictThread():
    makeDictThread = threading.Thread(target=makeDict)
    makeDictThread.start()
    
def makeDict():
    #try:
    print("\nSpell checker in action......")
    with open(os.path.abspath(pathname)+"\corpus.txt", "r") as f:
        for line in f:
            #print(line)
            for val in line.split():
                val = re.sub(r"[^a-z]+", '', val.lower())
                if val:
                    #p = enchantDict.check(val)
                    #print(p)
                    #if p:
                        #print("here")
                    if val in wordfreq:
                        wordfreq[val] += 1
                    else:
                        wordfreq[val] = 1
    return wordfreq
    '''except:
        print("Error while creating dictionary")'''
        
def findOutput(iWord):
    try:
        print("\nOutput:")
        outputWord = {}
        cntr = 0
        for inp in iWord:
            matchRes = get_close_matches(iWord[inp], wordfreq.keys(), 3)
            #print(matchRes)
            maxRes = {}
            for res in matchRes:
                freqVal = wordfreq.get(res)
                maxRes[res] = freqVal
            #print(maxRes)
            #maxRes = sorted(maxRes.items(), key=lambda x: x[0])
            firstWrd = list(maxRes.keys())[0]
            #print("\n\n")
            p = enchantDict.check(firstWrd)
            if p:
                outputWord[cntr] = firstWrd
            elif p and iWord[inp]==firstWrd:
                outputWord[cntr] = firstWrd
            else:
                outputWord[cntr] = max(maxRes.items(), key=operator.itemgetter(1))[0]
            cntr += 1

        for i in outputWord:
            print(outputWord[i])
        print("\nThanks for using spell checker built on python 3.7")
        
    except:
        print("Error while spell checking input words")

print("\n")
print("***********************************************************************************************")
print("Built on Python version - 3.7")
print("***********************************************************************************************")
print("\n")

try:
    createDictThread()
    print("Kindly enter the word(s) which needs to spell checked")
    wordCnt = int(input("\nPlease enter the count of input word(s): "))
    print("\n")
    print("You choose to enter %d words" %wordCnt)
    for i in range(1, wordCnt+1):
        word[i] = input("Please enter the input word no. %d: " %i)
    print("\n")
    #print(word)
    print("Input:")
    for inp in list(word):
        print(word[inp])
        if word[inp].isdigit():
            del word[inp]

    findOutput(word)
    
except ValueError:
    print("Kindly enter integer value")
    exit()
