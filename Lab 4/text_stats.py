#!/usr/bin/env python3

import sys
import string
from collections import Counter
import random
import itertools
import collections
from numpy.random import choice
import os.path

def raw_data(file_name):
    """Function opens file and returns data and list of words"""
    with open(file_name, "r",encoding="utf8")as file:
        data = file.read()
        data=data.translate(str.maketrans('', '', string.punctuation))   #used .translate as advised
        data = data.lower()
    return data

def word_list(data):
    wordlist= data.split()
    return wordlist

def sequence_letter(data):
    """Returns number of letters in the file"""
    count = Counter(data)
    count = {i: count.get(i, 0) for i in string.ascii_lowercase}
    # sorting on basis of frequency of elements
    sequence =Counter(count).most_common()
    return sequence

def common_words(wordlist,x):
    """Returns counter of x number of most common word  in the file"""
    most_common_words=Counter(wordlist).most_common(x)
    return most_common_words


def main(pars):
    file_name=pars[1]
    data=raw_data(file_name)
    wordlist= word_list(data)
    sequence = sequence_letter(data)
    range_most_common_next_words = 5
    range_next_most_common_next_words = 3
    most_common_words = common_words(wordlist, 5)


  #checking existance of file to write or build up a file :
    if len(sys.argv) > 2:
        if os.path.exists(pars[2]):
            filename = sys.argv[2]
            with open(filename, "w")as f:
                f.write("frequency table for alphabetic letters, ordered from the most common to the least :\n")
                for letter in range(len(sequence)):
                    word_frequency = sequence[letter]
                    f.write(f' -- {word_frequency[0]} :{word_frequency[1]}\n')
                f.write("number of words are :\n")
                #f.write(f"{str(length_wordlist(wordlist))}\n")
                f.write(f"{len(wordlist)}\n")
                f.write("Number of unique words that text contains :\n")
                #f.write(f"{str(length_word(wordlist))}\n")
                f.write(f"{len(Counter(wordlist))}\n")
                f.write("Three words that most commonly follow  five most common next words :\n")
                for most_common_words, frequency in most_common_words:
                    f.write(f'{most_common_words},  ({ frequency}, occurences)\n')
                    most_follow_words = [wordlist[i + 1] for i in range(0, len(wordlist)) if
                                         wordlist[i] == most_common_words]
                    for most_common_next_words, freq_most_common_next_words, in Counter(most_follow_words).most_common(
                            range_next_most_common_next_words):
                        f.write(f'-- {most_common_next_words}, {freq_most_common_next_words}\n')


        else:
            print("File does not exists")
    else: # print on terminal
        # 1  printing of frequency table for alphabetic letters, ordered from the most common to the least
        print("frequency table for alphabetic letters, ordered from the most common to the least :")
        for letter in range(len(sequence)):
            word_frequency = sequence[letter]
            print(f' -- {word_frequency[0]} :{word_frequency[1]}')
        # 2 number of words
        print("number of words are :")
        #print(str(length_wordlist(wordlist)))
        print(len(wordlist))
        # 3. Number of unique words that the text contains
        print("Number of unique words that text contains :")
        #print(str(length_word(wordlist)))
        print(len(Counter(wordlist)))
        # 4. Three words that most commonly follow  three most common next words
        print("Three words that most commonly follow  five most common next words :")
        for most_common_words, frequency in most_common_words:
            print(most_common_words, " (", frequency, "occurences)")
            most_follow_words = [wordlist[i + 1] for i in range(0, len(wordlist)) if
                                 wordlist[i] == most_common_words]
            for most_common_next_words, freq_most_common_next_words, in Counter(most_follow_words).most_common(
                    range_next_most_common_next_words):
                print("--", most_common_next_words, ",", freq_most_common_next_words)



# Reference : https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":  # execute only if run as a script
    try:
        file_name = sys.argv[1]
    except IndexError:
        print('Usage:text_stats.py<file_name>')
    else:
        main(pars=sys.argv)

#  Answers : Additional questions
# 1. We opened the file in read mode ,cleaned up the content wherein we wanted to avoid all possible unwanted character
# (punctuations etc) and # save it  data variable , to be recalled later.Further, to avoid words counting same word with
# lower or upper case as different , we converted all of them into lower case for easy of operation using data.lower().

#2. We have majorly used list and counter datasets. It is because list is very flexible and easy to work with, while
# counter data set gives us the frequency counter which is very helpful for the current task as per its data structure
# and presentation requirement.It is also one of the quickest way to calculate ordered frequency and highlights unique
# words.