class Similarity(object):
    '''
    Class to handle similarity functions.
    '''


    def __init__(self):
        '''
        Constructor 
        '''
        
    def calculateSimiliarity(self, docWordsStruct, term1, term2):
        similarity = 0
        
        for doc in docWordsStruct:
            if( term1 in docWordsStruct[doc] and term2 in docWordsStruct[doc]):
                similarity += docWordsStruct[doc][term1] * docWordsStruct[doc][term2]
                
        return similarity

if __name__ == '__main__':
    from util import Util
    from tokenator import Tokenator
    a = Util().getFileContent("../examples/TEST_light.DAT")
    
    struct = Tokenator().createDocWordsStruct(a)
    
    print Similarity().calculateSimiliarity(struct,"TERM", "ABOUT")
