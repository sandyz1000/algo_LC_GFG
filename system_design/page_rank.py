from __future__ import print_function
import numpy as np


def build_index(links):
    website_list = links.keys()
    return {website: index for index, website in enumerate(website_list)}


def build_transition_matrix(links, index):
    total_links = 0
    A = np.zeros((len(index), len(index)))
    for webpage in links:
        # dangling page
        if not links[webpage]:
            # Assign equal probabilities to transition to all the other pages
            A[index[webpage]] = np.ones(len(index)) / len(index)
        else:
            for dest_webpage in links[webpage]:
                total_links += 1
                A[index[webpage]][index[dest_webpage]] = 1.0 / len(links[webpage])
    return A


def pagerank(A, eps=0.0001, d=0.85):
    """
    Now we'll write the actual PageRank algorithm. The algorithm takes 2 parameters:

    1. eps: stop the algorithm when the difference between 2 consecutive iterations is smaller
    or equal to eps

    2. d: damping factor: With a probability of 1-d the user will simply pick a web page at
    random as the next destination, ignoring the link structure completely.

    """
    P = np.ones(len(A)) / len(A)
    while True:
        new_P = np.ones(len(A)) * (1 - d) / len(A) + d * A.T.dot(P)
        delta = abs((new_P - P).sum())
        if delta <= eps:
            return new_P
        P = new_P


if __name__ == '__main__':
    links = {
        'webpage-1': {'webpage-2', 'webpage-4', 'webpage-5', 'webpage-6', 'webpage-8', 'webpage-9',
                      'webpage-10'},
        'webpage-2': {'webpage-5', 'webpage-6'},
        'webpage-3': {'webpage-10'},
        'webpage-4': {'webpage-9'},
        'webpage-5': {'webpage-2', 'webpage-4'},
        'webpage-6': set([]),  # dangling page
        'webpage-7': {'webpage-1', 'webpage-3', 'webpage-4'},
        'webpage-8': {'webpage-1'},
        'webpage-9': {'webpage-1', 'webpage-2', 'webpage-3', 'webpage-8', 'webpage-10'},
        'webpage-10': {'webpage-2', 'webpage-3', 'webpage-8', 'webpage-9'},
    }

    website_index = build_index(links)
    # print(website_index)

    A = build_transition_matrix(links, website_index)

    results = pagerank(A)

    # [ 0.151  0.11355952  0.08725  0.10647619  0.07814286  0.07814286 0.0235  0.07105952
    # 0.15605952  0.13480952]
    print("Results:", results)
    print(sum(results))  # 1.0

    # [2, 0, 3, 5, 7, 4, 6, 9, 1, 8]
    print([item[0] for item in sorted(enumerate(results), key=lambda item: -item[1])])
