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
    sentence_list = []
    # randomly select a dictionary entry to start with

    rand_key = random.choice(chains.keys())
    start_sentence = " ".join(rand_key)
    print start_sentence
    # randomly select one of the values for the tuple 
    rand_val = random.choice(chains[rand_key])
    print rand_val

    sentence_list.append(start_sentence).capitalize()
    sentence_list.append(rand_val)



    # loop:
        # take the key's second tuple along with a randomly selected entry value
        # search for a key tuple that matches

    sec_tuple = rand_key[1]
    search_tuple = (sec_tuple, rand_val)
    print search_tuple
    print random.choice(chains[search_tuple])



    # turn into text
    # return text string

    





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