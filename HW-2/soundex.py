###################################
# Name of the author: SHILPASHREE RAO
# Email id: shilpasr@usc.edu
# Date: 9/15/2017
####################################
import argparsefrom fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """
    bigList = [['a', 'e', 'i', 'o', 'u', 'w', 'h', 'y'], ['b', 'f', 'p', 'v'], ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],\
               ['d', 't'], ['l'], ['m', 'n'], ['r']]
    
    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    f1.add_state('start')
    f1.add_state('next_0')
    f1.add_state('next_1')
    f1.add_state('next_2')
    f1.add_state('next_3')
    f1.add_state('next_4')
    f1.add_state('next_5')
    f1.add_state('next_6')
    f1.initial_state = 'start'

    # Set all the final states
    f1.set_final('next_0')
    f1.set_final('next_1')
    f1.set_final('next_2')
    f1.set_final('next_3')
    f1.set_final('next_4')
    f1.set_final('next_5')
    f1.set_final('next_6')

    # Add the rest of the arcs
 
    for l in string.ascii_lowercase:
        if l in bigList[0]:
            f1.add_arc('start', 'next_0', (l), (l))
        elif l in bigList[1]:
            f1.add_arc('start', 'next_1', (l), (l))
        elif l in bigList[2]:
            f1.add_arc('start', 'next_2', (l), (l))
        elif l in bigList[3]:
            f1.add_arc('start', 'next_3', (l), (l))
        elif l in bigList[4]:
            f1.add_arc('start', 'next_4', (l), (l))
        elif l in bigList[5]:
            f1.add_arc('start', 'next_5', (l), (l))
        else:
            f1.add_arc('start', 'next_6', (l), (l))
            
        if l in bigList[1]:
            f1.add_arc('next_0', 'next_1', (l), ('1'))         
        elif l in bigList[2]:
            f1.add_arc('next_0', 'next_2', (l), ('2'))
        elif l in bigList[3]:
            f1.add_arc('next_0', 'next_3', (l), ('3'))
        elif l in bigList[4]:
            f1.add_arc('next_0', 'next_4', (l), ('4'))
        elif l in bigList[5]:
            f1.add_arc('next_0', 'next_5', (l), ('5'))
        elif l in bigList[6]:
            f1.add_arc('next_0', 'next_6', (l), ('6'))
        else:
            f1.add_arc('next_0', 'next_0', (l), ()) 
   
        
        if l in bigList[0]:
            f1.add_arc('next_1', 'next_0', (l), ())
        elif l in bigList[2]:
            f1.add_arc('next_1', 'next_2', (l), ('2'))
        elif l in bigList[3]:
            f1.add_arc('next_1', 'next_3', (l), ('3'))
        elif l in bigList[4]:
            f1.add_arc('next_1', 'next_4', (l), ('4'))
        elif l in bigList[5]:
            f1.add_arc('next_1', 'next_5', (l), ('5'))
        elif l in bigList[6]:
            f1.add_arc('next_1', 'next_6', (l), ('6'))
        else:
            f1.add_arc('next_1', 'next_1', (l), ()) 
            
        if l in bigList[0]:
            f1.add_arc('next_2', 'next_0', (l), ())
        elif l in bigList[1]:
            f1.add_arc('next_2', 'next_1', (l), ('1'))
        elif l in bigList[3]:
            f1.add_arc('next_2', 'next_3', (l), ('3'))
        elif l in bigList[4]:
            f1.add_arc('next_2', 'next_4', (l), ('4'))
        elif l in bigList[5]:
            f1.add_arc('next_2', 'next_5', (l), ('5'))
        elif l in bigList[6]:
            f1.add_arc('next_2', 'next_6', (l), ('6'))
        else:
            f1.add_arc('next_2', 'next_2', (l), ()) 
            
        if l in bigList[0]:
            f1.add_arc('next_3', 'next_0', (l), ())
        elif l in bigList[1]:
            f1.add_arc('next_3', 'next_1', (l), ('1'))
        elif l in bigList[2]:
            f1.add_arc('next_3', 'next_2', (l), ('2'))
        elif l in bigList[4]:
            f1.add_arc('next_3', 'next_4', (l), ('4'))
        elif l in bigList[5]:
            f1.add_arc('next_3', 'next_5', (l), ('5'))
        elif l in bigList[6]:
            f1.add_arc('next_3', 'next_6', (l), ('6'))
        else:
            f1.add_arc('next_3', 'next_3', (l), ())

        if l in bigList[0]:
            f1.add_arc('next_4', 'next_0', (l), ())
        elif l in bigList[1]:
            f1.add_arc('next_4', 'next_1', (l), ('1'))
        elif l in bigList[2]:
            f1.add_arc('next_4', 'next_2', (l), ('2'))
        elif l in bigList[3]:
            f1.add_arc('next_4', 'next_3', (l), ('3'))
        elif l in bigList[5]:
            f1.add_arc('next_4', 'next_5', (l), ('5'))
        elif l in bigList[6]:
            f1.add_arc('next_4', 'next_6', (l), ('6'))
        else:
            f1.add_arc('next_4', 'next_4', (l), ())
            
        if l in bigList[0]:
            f1.add_arc('next_5', 'next_0', (l), ())
        elif l in bigList[1]:
            f1.add_arc('next_5', 'next_1', (l), ('1'))
        elif l in bigList[2]:
            f1.add_arc('next_5', 'next_2', (l), ('2'))
        elif l in bigList[3]:
            f1.add_arc('next_5', 'next_3', (l), ('3'))
        elif l in bigList[4]:
            f1.add_arc('next_5', 'next_4', (l), ('4'))
        elif l in bigList[6]:
            f1.add_arc('next_5', 'next_6', (l), ('6'))
        else:
            f1.add_arc('next_5', 'next_5', (l), ())  

        if l in bigList[0]:
            f1.add_arc('next_6', 'next_0', (l), ())
        elif l in bigList[1]:
            f1.add_arc('next_6', 'next_1', (l), ('1'))
        elif l in bigList[2]:
            f1.add_arc('next_6', 'next_2', (l), ('2'))
        elif l in bigList[3]:
            f1.add_arc('next_6', 'next_3', (l), ('3'))
        elif l in bigList[4]:
            f1.add_arc('next_6', 'next_4', (l), ('4'))
        elif l in bigList[5]:
            f1.add_arc('next_6', 'next_5', (l), ('5'))
        else:
            f1.add_arc('next_6', 'next_6', (l), ())
            

    return f1

    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('1b')
    f2.add_state('1c')
    f2.add_state('1d')
    f2.add_state('1e')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')

    f2.initial_state = '1'
    f2.set_final('2')
    f2.set_final('3')
    f2.set_final('4')

    f2.set_final('1b')
    f2.set_final('1c')
    f2.set_final('1d')
    f2.set_final('1e')

    # Add the arcs
    for letter in string.letters:
        f2.add_arc('1', '1b', (letter), (letter))
     
    for n in range(10):
        f2.add_arc('1b', '1c', (str(n)), (str(n)))
        f2.add_arc('1c', '1d', (str(n)), (str(n)))
        f2.add_arc('1d', '1e', (str(n)), (str(n)))
        f2.add_arc('1e', '1e', (str(n)), ())
        f2.add_arc('1', '2', (str(n)), (str(n)))
        f2.add_arc('2', '3', (str(n)), (str(n)))
        f2.add_arc('3', '4', (str(n)), (str(n)))
        f2.add_arc('4', '4', (str(n)), ())
        

    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('1a')
    f3.add_state('1b')
    f3.add_state('2')
    
    f3.initial_state = '1'
    f3.set_final('2')

    for letter in string.letters:
        f3.add_arc('1', '1', (letter), (letter))
    
    for number in xrange(10):
        f3.add_arc('1', '1a', (str(number)), (str(number)))
        f3.add_arc('1a', '1b', (str(number)), (str(number)))
        f3.add_arc('1b', '2', (str(number)), (str(number)))
   
        
#    if count == 2:
    f3.add_arc('1b', '2', (), ('0'))
#    if count == 1:
    f3.add_arc('1a', '2', (), ('00'))
#    if count == 1:
    f3.add_arc('1', '2', (), ('000'))
    
    
    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))
   
