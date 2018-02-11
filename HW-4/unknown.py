#!/usr/bin/env python

import sys, fileinput
import collections
import tree

count = collections.defaultdict(int)
fil = open('train.trees.pre.unk', 'w')

trees = []
for line in fileinput.input():
    t = tree.Tree.from_str(line)
    for leaf in t.leaves():
        count[leaf.label] += 1
    trees.append(t)

for t in trees:
    for leaf in t.leaves():
        if count[leaf.label] < 2:
            leaf.label = "<unk>"
    
#    sys.stdout = open('train.trees.pre.unk', 'a')
    sys.stdout.write("{0}\n".format(t))
    fil.write("{0}\n".format(t))
