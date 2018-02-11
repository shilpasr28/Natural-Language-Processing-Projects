###################################
# Name of the author: SHILPASHREE RAO
# Email id: shilpasr@usc.edu
# Date: 3/16/2017
####################################
import argparse
import sys
from fst import FST
from fsmutils import composewords

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"

    return list("%03i" % integer)


def french_count():
    f = FST('french')
    f.add_state('start')
    f.add_state('1')
    f.add_state('2')
    f.add_state('s10to19')
    f.add_state('s17to19')  
    f.add_state('20to69')
    f.add_state('sevts')
    f.add_state('eigts')
    f.add_state('nints')
    f.add_state('s10to19h')
    f.add_state('s17to19h')  
    f.add_state('20to69h')
    f.add_state('sevtsh')
    f.add_state('eigtsh')
    f.add_state('nintsh')
    f.add_state('hun')
    f.add_state('2h')
    
    
    f.initial_state = 'start'
    f.set_final('2')
    f.set_final('s10to19')
    f.set_final('s17to19')
    f.set_final('20to69')
    f.set_final('sevts')
    f.set_final('eigts')
    f.set_final('nints')
    f.set_final('2h')
    f.set_final('s10to19h')
    f.set_final('s17to19h')
    f.set_final('20to69h')
    f.set_final('sevtsh')
    f.set_final('eigtsh')
    f.set_final('nintsh')
    f.set_final('hun')

    
#    
    f.add_arc('start', '1', '0', ())
    f.add_arc('1', '2', '0', ())
    f.add_arc('2', '2', '0', [kFRENCH_TRANS[0]])
#
# 1 to 10 
    for ii in xrange(1, 10):
        f.add_arc('2', '2', [str(ii)], [kFRENCH_TRANS[ii]])
        
# 10 to 19    
    f.add_arc('1', 's10to19', '1', ())
    for ii in xrange(0,7):
        f.add_arc('s10to19', 's10to19', [str(ii)], [kFRENCH_TRANS[ii+10]])
   
    f.add_arc('s10to19', 's10to19', '7', [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[7]])
    f.add_arc('s10to19', 's10to19', '8', [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[8]])
    f.add_arc('s10to19', 's10to19', '9', [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[9]])
        
#  20 to 69
    for ii in xrange(2, 7):
        f.add_arc('1', '20to69', [str(ii)], [kFRENCH_TRANS[ii * 10]])
    f.add_arc('20to69', '20to69', '1', [kFRENCH_AND+" "+kFRENCH_TRANS[1]])
    f.add_arc('20to69', '20to69', '0', ())
    for ii in xrange(2,10):
        f.add_arc('20to69', '20to69', [str(ii)], [kFRENCH_TRANS[ii]])
          
# 70s
    f.add_arc('1', 'sevts', '7', [kFRENCH_TRANS[60]])
    f.add_arc('sevts', 'sevts', '0', [kFRENCH_TRANS[10]])
    f.add_arc('sevts', 'sevts', '1', [kFRENCH_AND+" "+kFRENCH_TRANS[11]])
    for ii in xrange(2,7):
        f.add_arc('sevts', 'sevts', [str(ii)], [kFRENCH_TRANS[ii+10]])
    f.add_arc('sevts', 'sevts', '7' , [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[7]])
    f.add_arc('sevts', 'sevts', '8' , [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[8]])
    f.add_arc('sevts', 'sevts', '9' , [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[9]])
            
    
#80s
    f.add_arc('1', 'eigts', '8', [kFRENCH_TRANS[4]+" "+kFRENCH_TRANS[20]])
    f.add_arc('eigts', 'eigts', '0', ())
    for ii in xrange(1, 10):
        f.add_arc('eigts', 'eigts', [str(ii)], [kFRENCH_TRANS[ii]])
        
#90s
    f.add_arc('1', 'nints', '9', [kFRENCH_TRANS[4]+" "+kFRENCH_TRANS[20]])
    f.add_arc('nints', 'nints', '0', [kFRENCH_TRANS[10]])
    for ii in xrange(1, 7):
        f.add_arc('nints', 'nints', [str(ii)], [kFRENCH_TRANS[ii+10]])
    f.add_arc('nints', 'nints', '7', [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[7]])
    f.add_arc('nints', 'nints', '8', [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[8]])
    f.add_arc('nints', 'nints', '9', [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[9]])


################### >100 ######################################################

    f.add_arc('start', 'hun', '1', [kFRENCH_TRANS[100]])
    for ii in xrange(2, 10):
        f.add_arc('start', 'hun', [str(ii)],  [kFRENCH_TRANS[ii]+" "+kFRENCH_TRANS[100]])
    
    f.add_arc('hun', '2h', '0', ())
    f.add_arc('2h', '2h', '0', ())
# 1 to 10 
    for ii in xrange(1, 10):  
        f.add_arc('2h', '2h', [str(ii)], [kFRENCH_TRANS[ii]])
        
# 10 to 19    
    f.add_arc('hun', 's10to19h', '1', ())
    for ii in xrange(0,7):
        f.add_arc('s10to19h', 's10to19h', [str(ii)], [kFRENCH_TRANS[ii+10]])
    f.add_arc('s10to19h', 's10to19h', '7', [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[7]])
    f.add_arc('s10to19h', 's10to19h', '8', [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[8]])
    f.add_arc('s10to19h', 's10to19h', '9', [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[9]])
        
#  20 to 69
    for ii in xrange(2, 7):
        f.add_arc('hun', '20to69h', [str(ii)], [kFRENCH_TRANS[ii * 10]])
    f.add_arc('20to69h', '20to69h', '1', [kFRENCH_AND+" "+kFRENCH_TRANS[1]])
    f.add_arc('20to69h', '20to69h', '0', ())
    for ii in xrange(2,10):
        f.add_arc('20to69h', '20to69h', [str(ii)], [kFRENCH_TRANS[ii]])
          
# 70s
    f.add_arc('hun', 'sevtsh', '7', [kFRENCH_TRANS[60]])
    f.add_arc('sevtsh', 'sevtsh', '0', [kFRENCH_TRANS[10]])
    f.add_arc('sevtsh', 'sevtsh', '1', [kFRENCH_AND+" "+kFRENCH_TRANS[11]])
    for ii in xrange(2,7):
        f.add_arc('sevtsh', 'sevtsh', [str(ii)], [kFRENCH_TRANS[ii+10]])
    f.add_arc('sevtsh', 'sevtsh', '7' , [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[7]])
    f.add_arc('sevtsh', 'sevtsh', '8' , [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[8]])
    f.add_arc('sevtsh', 'sevtsh', '9' , [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[9]])        
    
#80s
    f.add_arc('hun', 'eigtsh', '8', [kFRENCH_TRANS[4]+" "+kFRENCH_TRANS[20]])
    f.add_arc('eigtsh', 'eigtsh', '0', ())
    for ii in xrange(1, 10):
        f.add_arc('eigtsh', 'eigtsh', [str(ii)], [kFRENCH_TRANS[ii]])
        
#90s
    f.add_arc('hun', 'nintsh', '9', [kFRENCH_TRANS[4]+" "+kFRENCH_TRANS[20]])
    f.add_arc('nintsh', 'nintsh', '0', [kFRENCH_TRANS[10]])
    for ii in xrange(1, 7):
        f.add_arc('nintsh', 'nintsh', [str(ii)], [kFRENCH_TRANS[ii+10]])
    f.add_arc('nintsh', 'nintsh', '7', [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[7]])
    f.add_arc('nintsh', 'nintsh', '8', [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[8]])
    f.add_arc('nintsh', 'nintsh', '9', [kFRENCH_TRANS[10]+" "+kFRENCH_TRANS[9]])

#    print f  
    return f

if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))