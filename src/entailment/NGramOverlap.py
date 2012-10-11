# Bismillahi-r-Rahmani-r-Rahim
#
# Strategy which just looks at overlap of n grams



from LexicalStrategy import LexicalStrategy


class NGramOverlap(LexicalStrategy):
    def __init__(self, n, threshold = None):
        self.n = n
        LexicalStrategy.__init__(self, threshold)

    def __str__(self):
        return self.__class__.__name__ + '(%d)' % self.n

    def tokens(self, t):
        """ Create ngrams
        >>> n = NGramOverlap(2)
        >>> s = n.tokens('abcd')
        >>> l = list(s)
        >>> l.sort()
        >>> l
        ['ab', 'bc', 'cd']
        """
        r = set()
        for i in range(len(t) - self.n + 1):
            r.add(t[i:i+self.n])
        return r

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

        
