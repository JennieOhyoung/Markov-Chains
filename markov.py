#!/usr/bin/env python

from sys import argv
import random
import string

script, text = argv
f = open(text).read().lower()
corpus = f.replace(",", "").replace(".", "").replace("?", "")
   

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chains_dict = {}
    words = corpus.split()
    
    # use if statement to check if there is a word in the 0th and 1st position in our text
    # if true, then append 0th position as tup0 in dict, 1st position as tup1, 2nd as value
    # else: break

    for pos in range(len(words)-1):
        if pos != len(words) -2:
            key = (words[pos], words[pos + 1])
            chains_dict[key] = chains_dict.get(key, [])
            chains_dict[key].append(words[pos + 2]) 

    #print chains_dict
    return chains_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # randomly select a dictionary entry to start with

    search_tuple = random.choice(chains.keys())
    sentence_list = [search_tuple[0], search_tuple[1]]
    
    #loop goes here
    
    while len(" ".join(sentence_list)) <= 80:
        rand_val = random.choice(chains[search_tuple])
        sentence_list.append(rand_val)
        search_tuple = (search_tuple[1], rand_val)
        if not chains.get(search_tuple):
            break

    sentence = " ".join(sentence_list).capitalize()
    print sentence



def main():
    #args = sys.argv

    # Change this to read input_text from a file
    input_text = "Some text"

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

# if __name__ == "__main__":
    # main()

make_text(make_chains(corpus))