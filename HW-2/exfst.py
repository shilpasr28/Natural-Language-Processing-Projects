# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 11:21:21 2017

@author: SHILPASHREE RAO
"""

import string
import sys
from fst import FST
from fsmutils import trace


vowels = ['a', 'e', 'i', 'o', 'u']

f = FST('devowelizer')

f.add_state('1')

f.initial_state = '1'
f.set_final('1')

for letter in string.ascii_lowercase:
    if letter in vowels:
        _ = f.add_arc('1', '1', (letter), ())
    else:
        _ = f.add_arc('1', '1', (letter), (letter))

print ''.join(f.transduce(['v', 'o', 'w', 'e', 'l']))
print ''.join(f.transduce('e x c e p t i o n'.split()))
print ''.join(f.transduce('c o n s o n a n t'.split()))

t = trace(f, ['v', 'o', 'w', 'e', 'l'])
print t