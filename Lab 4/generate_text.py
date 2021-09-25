#!/usr/bin/env python3

import sys
import string
from collections import Counter
import numpy as np
import random
import collections
import numpy
from numpy.random import choice
from text_stats import raw_data
from text_stats import word_list
from collections import defaultdict



#import os.path

def text_generator(maximum_number, given_word, file_name):
    """Generation of text based on random choice of the successors of current word, weighted by how likely the word is
    to be succeeded by it. Work with three inputs as stated for exercise.
        """
    data=raw_data(file_name)
    wordlist=word_list(data)
    cur_word = given_word
    msg = cur_word
#########################################################################################

    all_unique_words = [w for w in Counter(wordlist).keys()]
    lookup = defaultdict(list)
    for i, j in zip(wordlist[:], wordlist[1:]):
        lookup[i].append(j)

#######################################################################################

    if cur_word in all_unique_words:
            for i in range(maximum_number-1):
                successor_stats = {cur_word: Counter(lookup[cur_word])}
                # print(successor_stats)
                words = list(successor_stats[cur_word])
                # listing all frequencies for random selection based on weights
                weights = list(successor_stats[cur_word].values())
                # random selection based on weights
                cur_word = np.random.choice(words, p=weights / np.sum(weights))
                # print(cur_word) # to check cur word is changing every time

                msg = msg + " " + cur_word  # adding to the sequence for output
                msg
    else:
        msg

    return(msg)


def main(pars):
    file_name=pars[1]
    given_word=pars[2]
    maximum_number=int(pars[3])


    #checking existance of file to write or build up a file :
    if len(sys.argv) > 4:
        if os.path.exists(pars[4]):
            filename = sys.argv[4]
            #f = open(filename, 'w')
            with open(filename, "w+")as f:
                f.write(text_generator(maximum_number, given_word, file_name))

        else:
            # write to a new file in (non-append mode) as per e-mail requirement
            with open(pars[4], "w")as f:
                f.write(text_generator(maximum_number, given_word, file_name))
            #print("File does not exists")
    else: # print on terminal
         print(text_generator(maximum_number, given_word, file_name))


if __name__ == "__main__":  # execute only if run as a script
    try:
        file_name = sys.argv[1]
    except IndexError:
        print('Usage:generate_text.py<file_name>')
    else:
        main(pars=sys.argv)
 # Reference : https://docs.python.org/3/library/__main__.html