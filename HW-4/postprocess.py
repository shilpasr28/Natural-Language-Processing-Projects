#!/usr/bin/env python

import sys, fileinput
import tree

fil = open('train.post', 'w')
for line in fileinput.input():
    t = tree.Tree.from_str(line)
    if t.root is None:
        print
        continue
    t.restore_unit()
    t.unbinarize()
#    sys.stdout = open('outpost.trees.', 'a')
#    fil.write(format(t))
    
    fil.write(str(t) + '\n')
    print t
    
    
