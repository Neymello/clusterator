from pprint import pprint

class Graph(object):

    def __init__(self, term_term_matrix, threshold=10):
        self.graph = {}
        for term_a in term_term_matrix:
            for term_b in term_term_matrix:
                if (term_term_matrix[term_a][term_b] >= threshold):
                    tmp = self.graph.get(term_a, [])
                    tmp.append(term_b)
                    self.graph[term_a] = tmp
            if( not self.graph.has_key(term_a)):
                self.graph[term_a] = []


if __name__ == '__main__':
    # term frequency matrix / vector model example from the book
    tfm = {
        "Item 1": {"Term 2":4, "Term 6":2, "Term 7":1, "Term 8":3},
        "Item 2": {"Term 1":3, "Term 2":1, "Term 3":4, "Term 4":3, "Term 5":1, "Term 6":2, "Term 8":1},
        "Item 3": {"Term 1":3, "Term 5":3, "Term 7":3},
        "Item 4": {"Term 2":1, "Term 4":3, "Term 7":2},
        "Item 5": {"Term 1":2, "Term 2":2, "Term 3":2, "Term 4":3, "Term 5":1, "Term 6":4, "Term 8":2}
    }
    from similarity import Similarity
    ttmatrix = Similarity.calculateSimilarityMatrix(tfm)
    
    g = Graph(ttmatrix)
    pprint(g.graph)
#    {'Term 1': ['Term 3', 'Term 4', 'Term 5', 'Term 6'],
#     'Term 2': ['Term 4', 'Term 6', 'Term 8'],
#     'Term 3': ['Term 1', 'Term 4', 'Term 6'],
#     'Term 4': ['Term 1', 'Term 2', 'Term 3', 'Term 6'],
#     'Term 5': ['Term 1'],
#     'Term 6': ['Term 1', 'Term 2', 'Term 3', 'Term 4', 'Term 8'],
#     'Term 7': [],
#     'Term 8': ['Term 2', 'Term 6']}

