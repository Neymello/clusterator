# this is from our own module
from util import Util
from tokenator import Tokenator

# pprint is like print_r from php to python. just use pprint(stuff)
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4)
def pprint(stuff):
    pp.pprint(stuff)


if __name__ == '__main__':
    doc = Util().getFileContent("../examples/TEST.DAT")
    t = Tokenator()
    tfm = t.createTermFrequencyMatrix(doc)
    pprint(tfm)
    
    
