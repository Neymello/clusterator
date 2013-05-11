# create a histogram to be plotted in the paper.

import util

# pprint is like print_r from php to python. just use pprint(stuff)
from pprint import pprint

if __name__ == '__main__':
    docs = util.getFileContent("../examples/TEST.DAT")
    
    print len(docs.keys())

    # stores all words of all documents, with repetitions
    all_words = []
    for document in docs:
        all_words += docs[document]

    unique_words = set(all_words)

    print "Total words: ", len(all_words)
    print "Unique words:", len(unique_words)

    biggest_len = 0
    biggest_word = ""
    smallest_len = float("inf")
    smallest_word = ""
    for word in all_words:
        if len(word) > biggest_len:
            biggest_len = len(word)
            biggest_word = word
        if len(word) < smallest_len:
            smallest_len = len(word)
            smallest_word = word
    print "Longest word:", biggest_word
    print "shortest word:", smallest_word


    word_count = {}
    for word in unique_words:
        word_count[word] = all_words.count(word)
    import operator
    sorted_word_count = sorted(word_count.iteritems(), key=operator.itemgetter(1))
    pprint(sorted_word_count )
    

    histogram_data = []
    for word in unique_words:
        histogram_data.append(all_words.count(word))

    histogram_data.sort()

    frequencies = list(set(histogram_data))  # remove duplicates
    frequencies.sort()  # sets are not always ordered
    for freq in frequencies:
        print "there are %d words that appear %d times" % (histogram_data.count(freq), freq)
        
    import matplotlib.pyplot as plt
    import numpy as np 
    
    hist, bin_edges = np.histogram(histogram_data, bins = range(len(frequencies)))
    
    plt.bar(bin_edges[:-1], hist, width = 1)
    xmin = min(bin_edges)
    if(xmin==0):
        xmin = 1
    plt.xlim(xmin, max(bin_edges))
    plt.xlabel("Occurrence")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()  
    
    
