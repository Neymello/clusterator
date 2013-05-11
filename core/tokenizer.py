from collections import Counter

def createTokens(string):
    result = []

    for word in string.split(" "):
        if(word.strip() != ""):
            result.append(word.strip())

    return result


def createTermFrequencyMatrix(docWordsStruct, threshold=1):
    result = dict()

    ignore_list = []
    if threshold > 1:
        all_words = []
        for document in docWordsStruct:
            all_words += docWordsStruct[document]

        word_counter = Counter(all_words)

        for word in word_counter:
            if word_counter[word] < threshold:
                ignore_list.append(word)

    for doc in docWordsStruct:
        result[doc] = dict()

        for word in docWordsStruct[doc]:
            if word not in ignore_list:
                if(word not in result[doc]):
                    result[doc][word] = 0

                result[doc][word] += 1


    return result
