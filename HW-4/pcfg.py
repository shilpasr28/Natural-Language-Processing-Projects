"""
Created on Sat Sep 30 15:04:39 2017

@author: SHILPASHREE RAO
"""
import sys
import nltk
from itertools import repeat
from nltk import Tree
import math
import re
import time  
import matplotlib.pyplot
import pylab
import matplotlib.pyplot as plt
import numpy as np

def key_prob_diag(word, weight, gram):
    unk = '<unk>'
    key_probList = []
    for k in gram:
        for wor in gram[k]:
            if  wor[1:-1] == word:
                store = (k, weight + gram[k][wor])
                key_probList.append(store)
    if len(word.split()) == 1 and not key_probList:
        for k in gram:
            for wor in gram[k]:
                if unk == wor[1:-1]:
                    store = (k, gram[k][wor])
                    key_probList.append(store)
    return key_probList

def key_prob_other(word, weight, gram):
    unk = '<unk>'
    key_probList = []
    for k in gram:
        for wor in gram[k]:
            if  wor == str(word):
                store = (k, weight + gram[k][wor])
                key_probList.append(store)
    if len(word.split()) == 1 and not key_probList:
        for k in gram:
            for wor in gram[k]:
                if unk == wor[1:-1]:
                    store = (k, gram[k][wor])
                    key_probList.append(store)
    return key_probList

def convTree(fTree):
    i = 0
    while(i < len(fTree)):
        if isinstance(fTree[i], list):
            fTree[i] = convTree(fTree[i])   
        i += 1
    return "({})".format(' '.join(fTree))

def finTree(entryTable, backInd, upperSentence, x, y, z):     
    if backInd[x][y]:
        rightList= []
        X1 = backInd[x][y][z][0][0] 
        Y1 = backInd[x][y][z][0][1]
        Z1 = backInd[x][y][z][0][2]
        rightList.append(finTree(entryTable, backInd, upperSentence, X1, Y1, Z1))
        X2 = backInd[x][y][z][1][0]
        Y2 = backInd[x][y][z][1][1]
        Z2 = backInd[x][y][z][1][2]
        rightList.append(finTree(entryTable, backInd, upperSentence, X2, Y2, Z2))
    else:
        rightList = [sentence[y-1]]
    ftree = [entryTable[x][y][z][0]]
    ftree.extend(rightList)
    return ftree
    
fil = open('dev.parses', 'w')

with open('train.trees.pre.unk', 'r') as f:
    data = f.readlines()
productions = []
t = []
TOP = nltk.Nonterminal('TOP')
for i in data:
    t = Tree.fromstring(i)
    productions += t.productions()
grammar = nltk.induce_pcfg(TOP, productions)
gramDict = {}
gramDictUpper = gramDict
g = str(grammar).splitlines()
del g[0]
for i in g:
    sep = i.strip().split()
    prob = math.log10(float(sep[-1].strip('[]')))   
    if len(sep[2:-1]) > 1:
        if (sep[0]) in gramDict:
            gramDict[sep[0]][' '.join(sep[2:-1])] = prob
        else:
            gramDict[sep[0]] = {' '.join(sep[2:-1]):prob}
    else:
        lowCaseList = []
        for i in sep[2:-1]:
            i = i.lower()
            lowCaseList.append(i)
        if (sep[0]) in gramDict:
            gramDict[sep[0]][' '.join(lowCaseList)] = prob
        else:
            gramDict[sep[0]] = {' '.join(lowCaseList):prob}
        print gramDict
       

        
with open('dev.strings', 'r') as f:
    datasen = f.readlines()
datasen = [x.strip() for x in datasen]

timeList = []
senLenlist = []
startTime = time.time()
for each in datasen:
    sentence = []
    sentenceUpper = []
    sent = each.split()
    for i in sent:
        sentence.append(i.lower())
    for i in sent:
        sentenceUpper.append(i)
    
    senLen = len(sentence)
    
    #Entry table
    entTable = [None for i in range(senLen)]
    p = 0
    while(p < senLen):
        entTable[p] = [None for i in range(senLen + 1)]
        q = 0
        while(q < senLen + 1):
            entTable[p][q] = []
            q += 1
        p += 1
    
    # Indexing table
    ind = [None for i in range(senLen)]
    p = 0
    while(p < senLen):
        ind[p] = [None for i in range(senLen + 1)]
        q = 0
        while(q < senLen + 1):
            ind[p][q] = []
            q += 1
        p += 1
             
#
    i = 1
    while(i < senLen + 1):
        entTable[i-1][i].extend(key_prob_diag(sentence[i-1], 0, gramDict))
        i += 1
#    
    a = 1
    while(a < senLen + 1):
        b = p - 2
        while(b > -1):
            c = b + 1
            while(c < a):
                d = 0
                while(d < len(entTable[b][c])):
                    e = 0
                    while(e < len(entTable[c][a])):
                        weights = entTable[b][c][d][1] + entTable[c][a][e][1]
                        words = entTable[b][c][d][0] + ' '+ entTable[c][a][e][0]
                        keys = key_prob_other(words, weights, gramDict) 
                        if keys:
                            entTable[b][a].extend(keys)
                            ind[b][a].extend([[[b, c, d], [c, a, e]]]*len(keys)) 
                        e += 1
                    d += 1
                c += 1
            b -= 1
        a += 1 

    if entTable[0][senLen]:     
        fin_weight = entTable[0][senLen][0][1]
        f = 0
        i = 1
        while(i < len(entTable[0][senLen])):
            weights = entTable[0][senLen][i][1]
            if weights > fin_weight:
                fin_weight = weights
                f = i
            i += 1
        finalTree =  finTree(entTable, ind, sentenceUpper, 0, senLen, f)
    else:
        finalTree =  None
    
    if finalTree is None:
        fakList = ['TOP']
        for i, word in enumerate(sentence):
            for k in gramDict:
                for wor in gramDict[k]:
                    if  wor[1:-1] == word:
                        check = sentenceUpper[i]
                        c = False
                        for j in fakList:
                            if check in j:
                                c = True       
                                break
                        if c == False:
                            fakList.append([k, check])
        fil.write(convTree(fakList) + '\n')
    else:
        fil.write(convTree(finalTree) + '\n')
        print convTree(finalTree)
            
    print fin_weight
    
    totalTime = (time.time() - startTime)
    timeList.append(totalTime)
    senLenlist.append(senLen)
#y = timeList
#x = senLenlist
#import numpy as np
#x.sort()
#y.sort()
#plt.scatter(x,y)
#plt.title('Graph')
#plt.xlabel('Sentence Length')
#plt.ylabel('Time')
#plt.show()
#slope, intercept = np.polyfit(np.log(x), np.log(y), 1)
#print(slope)
#plt.loglog(x, y, '--')
#plt.show()