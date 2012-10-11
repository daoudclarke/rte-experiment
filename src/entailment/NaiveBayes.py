# Bismillahi-r-Rahman-r-Rahim
#
# Naive Bayes classifier

from collections import defaultdict
from math import log

class NaiveBayes:
    """Naive Bayes classifier.
    >>> n = NaiveBayes()
    >>> n.train([({'a': 2, 'b': 1}, True),({'c': 3,'d': 1}, False)])
    >>> n.classify([{'a': 1}, {'d': 3}])
    [True, False]
    """
    def __init__(self):
        self.model = defaultdict(float)

    def train(self, data):
        pos_freqs = defaultdict(int)
        neg_freqs = defaultdict(int)
        for features, classification in data:
            assert classification in [True,False]
            add_to = pos_freqs if classification else neg_freqs
            for f, v in features.items():
                add_to[f] += v
        all_features = set(pos_freqs.keys()) | set(neg_freqs.keys())
        for k in all_features:
            self.model[k] = log(pos_freqs[k] + 1) - log(neg_freqs[k] + 1)
        
        numPos = len([x for x in data if data[1]])
        numNeg = len(data) - numPos
        self.prior = log(numPos + 1) - log(numNeg + 1)

    def classify(self, data):
        results = []
        likelihood = self.prior
        for features in data:
            likelihood += sum([self.model[k] * v for k,v in features.items()])
            results.append(likelihood >= 0.0)
        return results

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
