class Util(object):
    '''
    Class to handle file
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def getFileContent(self, filePath):
        from tokenator import Tokenator
        result = {}
        fileObj = open(filePath, 'r')
        
        linesArray = fileObj.readlines()
        
        lastDocId = ""
        counter = 1
        for line in range(len(linesArray)):
            textLine = linesArray[line].strip()
            
            if(textLine != ""):
                """ Create the Docs Id """
                if (line < len(linesArray)-1 and linesArray[line+1].strip() == "" and len(textLine) < 10 ):
                    lastDocId = str(counter) + "_" + textLine
                    result[lastDocId] = []
                    counter += 1
                    
                elif (lastDocId != ""):
                    result[lastDocId] += Tokenator().createTokens(textLine) 
            
        return result

if __name__ == '__main__':
    print Util().getFileContent("../examples/TEST.DAT")
