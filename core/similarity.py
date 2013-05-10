from pprint import pprint


def calculateSimilarityMatrix(tfm):
    # find the set of all terms available
    termset = set()
    for doc in tfm:
        for term in tfm[doc]:
            termset.add(term)

    # term_term_matrix[i,j] = sum of term_i in doc times term_j in doc for all docs
    term_term_matrix = {}
    for term_i in termset:
        for term_j in termset:
            termsum = 0
            if(term_i != term_j):
                for doc in tfm:
                    termsum += tfm[doc].get(term_i, 0) * tfm[doc].get(term_j, 0)
            tmp = term_term_matrix.get(term_i, {})
            tmp[term_j] = termsum
            term_term_matrix[term_i] = tmp

    return term_term_matrix

if __name__ == '__main__':
    # term frequency matrix / vector model example from the book
    tfm = {
        "Item 1": {"Term 2":4, "Term 6":2, "Term 7":1, "Term 8":3},
        "Item 2": {"Term 1":3, "Term 2":1, "Term 3":4, "Term 4":3, "Term 5":1, "Term 6":2, "Term 8":1},
        "Item 3": {"Term 1":3, "Term 5":3, "Term 7":3},
        "Item 4": {"Term 2":1, "Term 4":3, "Term 7":2},
        "Item 5": {"Term 1":2, "Term 2":2, "Term 3":2, "Term 4":3, "Term 5":1, "Term 6":4, "Term 8":2}
    }

    ttmatrix = calculateSimilarityMatrix(tfm)

    pprint(ttmatrix)
