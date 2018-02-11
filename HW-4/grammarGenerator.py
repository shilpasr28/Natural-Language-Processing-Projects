# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:50:28 2017

@author: SHILPASHREE RAO
"""
import sys
import nltk
from itertools import islice
from nltk import Tree
import collections

#with open(sys.argv[1], 'r') as f:
with open('train.trees.pre.unk', 'r') as f:
#    data = f.read()
    data = f.readlines()

productions = []
t = []
TOP = nltk.Nonterminal('TOP')
for i in data:
    t = Tree.fromstring(i)
    productions += t.productions()
grammar = nltk.induce_pcfg(TOP, productions)
lefRule = []
rightRule = []
for i in productions:
    lefRule.append(i.lhs())
    rightRule.append(i.rhs())
tupList = zip(lefRule, rightRule)
count = collections.Counter(tupList)
maxv = max([i for i in count.values()])
out = (count.keys()[count.values().index(maxv)], maxv)
print "Frequently occuring rule and it's frequency", out
num = len(grammar.productions())
print "Number of rules in the grammar:", num
#print nltk.grammar.lhs.grammar.productions()



    