#!/usr/bin/env python
###################################
# Name of the author: SHILPASHREE RAO
# Email id: shilpasr@usc.edu
# Date: 3/9/2017
####################################
import argparse
import sys
import codecs
if sys.version_info[0] == 2:
  from itertools import izip
else:
  izip = zip
from collections import defaultdict as dd
import re
import os.path
import gzip
import tempfile
import shutil
import atexit

# Use word_tokenize to split raw text into words
from string import punctuation

import nltk
from nltk.tokenize import word_tokenize

scriptdir = os.path.dirname(os.path.abspath(__file__))

reader = codecs.getreader('utf8')
writer = codecs.getwriter('utf8')

def prepfile(fh, code):
  if type(fh) is str:
    fh = open(fh, code)
  ret = gzip.open(fh.name, code if code.endswith("t") else code+"t") if fh.name.endswith(".gz") else fh
  if sys.version_info[0] == 2:
    if code.startswith('r'):
      ret = reader(fh)
    elif code.startswith('w'):
      ret = writer(fh)
    else:
      sys.stderr.write("I didn't understand code "+code+"\n")
      sys.exit(1)
  return ret

def addonoffarg(parser, arg, dest=None, default=True, help="TODO"):
  ''' add the switches --arg and --no-arg that set parser.arg to true/false, respectively'''
  group = parser.add_mutually_exclusive_group()
  dest = arg if dest is None else dest
  group.add_argument('--%s' % arg, dest=dest, action='store_true', default=default, help=help)
  group.add_argument('--no-%s' % arg, dest=dest, action='store_false', default=default, help="See --%s" % arg)



class LimerickDetector:

    def __init__(self):
        """
        Initializes the object to have a pronunciation dictionary available
        """
        self._pronunciations = nltk.corpus.cmudict.dict()

    def num_syllables(self, word):
        """
        Returns the number of syllables in a word.  If there's more than one
        pronunciation, take the shorter one.  If there is no entry in the
        dictionary, return 1.
        """
        # TODO: provide an implementation!
        word = word.lower()
        if word in self._pronunciations:
            sy_uListd = self._pronunciations[word]
            allsyl_Count = []
            for i in range(len(sy_uListd)):
                sy_List = [str(x) for x in sy_uListd[i]]
                syl_Count = 0
                for ele in range(len(sy_List)):
                    end_Char = sy_List[ele][-1]
                    if end_Char.isdigit():
                        syl_Count = syl_Count + 1
                allsyl_Count.append(syl_Count)
            return min(allsyl_Count)
           
        return 1

    def rhymes(self, a, b):
        """
        Returns True if two words (represented as lower-case strings) rhyme,
        False otherwise.
        """
        # TODO: provide an implementation!
        arpabet_List = ['AO', 'AA', 'IY', 'UW', 'EH', 'IH', 'UH', 'AH', 'AX', \
                        'AE', 'EY', 'AY', 'OW', 'AW', 'OY', 'ER', 'AXR', 'EH R',\
                        'UH R', 'AO R', 'AA R', 'IH R', 'IY R', 'AW R']
        a = a.lower()
        b = b.lower()
        isRhyme = False
        if a in self._pronunciations:
            ry_uLista = self._pronunciations[a]
            norms_a = []
            for i in range(len(ry_uLista)):
                ry_Lista = [str(x) for x in ry_uLista[i]]
                ryA = []
                for ele in range(len(ry_Lista)):
                    ry_a = re.sub('[0-9]+', '', ry_Lista[ele])
                    ryA.append(ry_a)
                ind_a = []
                for i in ryA:
                    if i in arpabet_List:
                        ind_a.append(ryA.index(i))
                norm_a = ryA[ind_a[0] : ]
                norms_a.append(norm_a)
 
                    
        if b in self._pronunciations:
            ry_uListb = self._pronunciations[b]
            norms_b = []
            for i in range(len(ry_uListb)):
                ry_Listb = [str(x) for x in ry_uListb[i]]
                ryB = []
                for ele in range(len(ry_Listb)):
                    ry_b = re.sub('[0-9]+', '', ry_Listb[ele])
                    ryB.append(ry_b)
                ind_b = []
                for i in ryB:
                    if i in arpabet_List:
                        ind_b.append(ryB.index(i))
                norm_b = ryB[ind_b[0] : ]
                norms_b.append(norm_b)

            for x in norms_a:
                if x == []:
                    isRhyme = True
                    break
                for y in norms_b:
                    if y == []:
                        isRhyme = True
                        break
                    if(len(x) >= len(y)):
                        check_a = x[-(len(y)): ]
                        if check_a == y:
                            isRhyme = True
                            break
                    elif(len(y) > len(x)):
                        check_b = y[-(len(x)): ]
                        if check_b == x:
                            isRhyme = True
                            break
                if isRhyme == True:
                    break
            return isRhyme
            
        return isRhyme

    def is_limerick(self, text):
        """
        Takes text where lines are separated by newline characters.  Returns
        True if the text is a limerick, False otherwise.

        A limerick is defined as a poem with the form AABBA, where the A lines
        rhyme with each other, the B lines rhyme with each other, and the A lines do not
        rhyme with the B lines.


        Additionally, the following syllable constraints should be observed:
          * No two A lines should differ in their number of syllables by more than two.
          * The B lines should differ in their number of syllables by no more than two.
          * Each of the B lines should have fewer syllables than each of the A lines.
          * No line should have fewer than 4 syllables

        (English professors may disagree with this definition, but that's what
        we're using here.)


        """
        # TODO: provide an implementation!
        isLimerick = False
        txt_Lines = text.splitlines()
        txt_Lines = [x.strip(' ') for x in txt_Lines]
        while '' in txt_Lines:
            txt_Lines.remove('')

        if len(txt_Lines) == 5:
            s = []
            lW = []
            for line in txt_Lines:
                wrds = word_tokenize(line)
  
            
                if(wrds[-1].isalpha()):
                    lw = wrds[-1]
                else:
                    lw = wrds[-2]   ##check  if -2 has special char
                    
                lW.append(lw)
                tsyl_C = 0
                syl_C = 0
                finWords = []
                for x in wrds:
                    if x.startswith("'") or x.isalpha():
                        finWords.append(x)
  
                    
                for wrd in finWords:
                    syl_C = self.num_syllables(wrd)
                    tsyl_C += syl_C
                s.append(tsyl_C)

            
            if(all(i >= 4 for i in s)):
             
                if(s[2]<s[0] and s[2]<s[1] and s[2]<s[4] and s[3]<s[0] and \
                   s[3]<s[1] and s[3]<s[4]):
        
                    if(abs(s[0]-s[1]) and abs(s[0]-s[4]) and abs(s[1]-s[4])) <= 2:
                        if(abs(s[2]-s[3])) <= 2:
            
                            
                            if(self.rhymes(lW[0],lW[1]) and self.rhymes(lW[1],lW[4]) and \
                               self.rhymes(lW[0],lW[4]) and self.rhymes(lW[2],lW[3])):
        
                                
                                if(~(self.rhymes(lW[2],lW[0]) or self.rhymes(lW[2],lW[1]) or\
                               self.rhymes(lW[2],lW[4]) or self.rhymes(lW[3],lW[0]) or \
                               self.rhymes(lW[3],lW[1]) or self.rhymes(lW[3],lW[4]))):
       
                                
                                
                                    isLimerick = True
                            
        
        return isLimerick


# The code below should not need to be modified
def main():
  parser = argparse.ArgumentParser(description="limerick detector. Given a file containing a poem, indicate whether that poem is a limerick or not",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  addonoffarg(parser, 'debug', help="debug mode", default=False)
  parser.add_argument("--infile", "-i", nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="input file")
  parser.add_argument("--outfile", "-o", nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="output file")




  try:
    args = parser.parse_args()
  except IOError as msg:
    parser.error(str(msg))

  infile = prepfile(args.infile, 'r')
  outfile = prepfile(args.outfile, 'w')

  ld = LimerickDetector()
  lines = ''.join(infile.readlines())
  outfile.write("{}\n-----------\n{}\n".format(lines.strip(), ld.is_limerick(lines)))

if __name__ == '__main__':
  main()
