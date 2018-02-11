#!/usr/bin/env python

import sys, fileinput
import tree

fil = open('train.trees.pre', 'w')

for line in fileinput.input():
    t = tree.Tree.from_str(line)

    # Binarize, inserting 'X*' nodes.
    t.binarize()

    # Remove unary nodes
    t.remove_unit()

    # The tree is now strictly binary branching, so that the CFG is in Chomsky normal form.

    # Make sure that all the roots still have the same label.
    assert t.root.label == 'TOP'
        
#    sys.stdout = open('train.trees.pre', 'a')
#    sys.stdout = open('train.post', 'a')
    fil.write(str(t) + '\n')
   
    print t
    
    
