'''
Created on Mar 30, 2013

@author: neymellosampaio
'''

class Tokenator(object):
    '''
    Class to handle tokens.
    '''


    def __init__(self):
        '''
        Constructor 
        '''
        
    def createTokens(self,string):
        result = []
        
        for word in string.split(" "):
            if(word.strip() != ""):
                result.append(word.strip())

        return result
    
if __name__ == '__main__':
    Tokenator().createTokens("ney mello    sampaio")