def createTokens(self, string):
    result = []

    for word in string.split(" "):
        if(word.strip() != ""):
            result.append(word.strip())

    return result


def createTermFrequencyMatrix(self, docWordsStruct):
    result = dict()

    for doc in docWordsStruct:
        result[doc] = dict()

        for word in docWordsStruct[doc]:
            if(word not in result[doc]):
                result[doc][word] = 0

            result[doc][word] += 1

    return result
