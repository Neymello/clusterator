from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt


class Graph(object):
    def __init__(self, term_term_matrix, threshold=10):
        self.graph = {}
        for term_a in term_term_matrix:
            for term_b in term_term_matrix:
                if (term_term_matrix[term_a][term_b] >= threshold):
                    tmp = self.graph.get(term_a, [])
                    tmp.append(term_b)
                    self.graph[term_a] = tmp

            if(term_a not in self.graph):
                self.graph[term_a] = []

        self.nx_graph = nx.to_networkx_graph(self.graph)

    def cliques(self):
        return nx.algorithms.clique.find_cliques(self.nx_graph)


if __name__ == '__main__':
    # term frequency matrix / vector model example from the book
    tfm = {
        "Item 1": {"Term 2":4, "Term 6":2, "Term 7":1, "Term 8":3},
        "Item 2": {"Term 1":3, "Term 2":1, "Term 3":4, "Term 4":3, "Term 5":1, "Term 6":2, "Term 8":1},
        "Item 3": {"Term 1":3, "Term 5":3, "Term 7":3},
        "Item 4": {"Term 2":1, "Term 4":3, "Term 7":2},
        "Item 5": {"Term 1":2, "Term 2":2, "Term 3":2, "Term 4":3, "Term 5":1, "Term 6":4, "Term 8":2}
    }

    import similarity
    ttmatrix = similarity.calculateSimilarityMatrix(tfm)

    g = Graph(ttmatrix)

    pprint(g)

    print '### Cliques ###'
    pprint(g.cliques())
#    {'Term 1': ['Term 3', 'Term 4', 'Term 5', 'Term 6'],
#     'Term 2': ['Term 4', 'Term 6', 'Term 8'],
#     'Term 3': ['Term 1', 'Term 4', 'Term 6'],
#     'Term 4': ['Term 1', 'Term 2', 'Term 3', 'Term 6'],
#     'Term 5': ['Term 1'],
#     'Term 6': ['Term 1', 'Term 2', 'Term 3', 'Term 4', 'Term 8'],
#     'Term 7': [],
#     'Term 8': ['Term 2', 'Term 6']}
