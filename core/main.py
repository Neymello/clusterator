# this is from our own module
import util
import tokenizer

# pprint is like print_r from php to python. just use pprint(stuff)
from pprint import pprint

if __name__ == '__main__':
    doc = util.getFileContent("../examples/TEST.DAT")
    tfm = tokenizer.createTermFrequencyMatrix(doc)
    pprint(tfm)
