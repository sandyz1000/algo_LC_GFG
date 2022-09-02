from __future__ import print_function

from nltk.corpus import brown, stopwords
from nltk.cluster.util import cosine_distance
from operator import itemgetter
import numpy as np


def sentence_similarity(sent1, sent2, stopwords=None):
    """
    NLTK implements cosine_distance, which is 1 - cosine_similarity. The concept of distance is
    opposite to similarity. Two identical vectors are located at 0 distance and are 100% similar.
    """
    if stopwords is None:
        stopwords = []

    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1

    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences, stopwords=None):
    # Create an empty similarity matrix
    S = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue

            S[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    # normalize the matrix row-wise
    for idx in range(len(S)):
        S[idx] /= S[idx].sum()

    return S


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


def textrank(sentences, top_n=5, stopwords=None):
    """
    sentences = a list of sentences [[w11, w12, ...], [w21, w22, ...], ...]
    top_n = how may sentences the summary should contain
    stopwords = a list of stopwords
    """
    S = build_similarity_matrix(sentences, stop_words)
    sentence_ranks = pagerank(S)

    # Sort the sentence ranks
    ranked_sentence_indexes = [item[0] for item in
                               sorted(enumerate(sentence_ranks), key=lambda item: -item[1])]
    selected_sentences = sorted(ranked_sentence_indexes[:top_n])
    summary = itemgetter(*SELECTED_SENTENCES)(sentences)
    return summary


if __name__ == '__main__':

    # One out of 5 words differ => 0.8 similarity
    print(sentence_similarity("This is a good sentence".split(), "This is a bad sentence".split()))

    # One out of 2 non-stop words differ => 0.5 similarity
    print(sentence_similarity("This is a good sentence".split(), "This is a bad sentence".split(),
                              stopwords.words('english')))

    # 0 out of 2 non-stop words differ => 1 similarity (identical sentences)
    print(sentence_similarity("This is a good sentence".split(), "This is a good sentence".split(),
                              stopwords.words('english')))

    # Completely different sentences=> 0.0
    print(sentence_similarity("This is a good sentence".split(),
                              "I want to go to the market".split(),
                              stopwords.words('english')))

    # Get a text from the Brown Corpus
    sentences = brown.sents('ca01')

    print(sentences)
    # [[u'The', u'Fulton', u'County', u'Grand', u'Jury', u'said', u'Friday', u'an',
    # u'investigation', u'of', u"Atlanta's", u'recent', u'primary', u'election', u'produced',
    # u'``', u'no', u'evidence', u"''", u'that', u'any', u'irregularities', u'took', u'place',
    # u'.'], [u'The', u'jury', u'further', u'said', u'in', u'term-end', u'presentments', u'that',
    #  u'the', u'City', u'Executive', u'Committee', u',', u'which', u'had', u'over-all',
    # u'charge', u'of', u'the', u'election', u',', u'``', u'deserves', u'the', u'praise', u'and',
    #  u'thanks', u'of', u'the', u'City', u'of', u'Atlanta', u"''", u'for', u'the', u'manner',
    # u'in', u'which', u'the', u'election', u'was', u'conducted', u'.'], ...]

    print(len(sentences))  # 98

    # get the english list of stopwords
    stop_words = stopwords.words('english')

    S = build_similarity_matrix(sentences, stop_words)
    print(S)

    sentence_ranks = pagerank(S)

    print(sentence_ranks)

    # Get the sentences ordered by rank
    ranked_sentence_indexes = [item[0] for item in
                               sorted(enumerate(sentence_ranks), key=lambda item: -item[1])]
    print(ranked_sentence_indexes)

    # Suppose we want the 5 most import sentences
    SUMMARY_SIZE = 5
    SELECTED_SENTENCES = sorted(ranked_sentence_indexes[:SUMMARY_SIZE])
    print(SELECTED_SENTENCES)

    # Fetch the most important sentences
    summary = itemgetter(*SELECTED_SENTENCES)(sentences)

    # Print the actual summary
    for sentence in summary:
        print(' '.join(sentence))

    for idx, sentence in enumerate(textrank(sentences, stopwords=stopwords.words('english'))):
        print("%s. %s" % ((idx + 1), ' '.join(sentence)))
