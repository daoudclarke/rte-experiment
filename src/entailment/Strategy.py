# Bismillahi-r-Rahmani-r-Rahim
#
# Abstract class for textual entailment strategy


class NotImplementedError:
    pass

class Strategy:
    def train(self, pairs):
        raise NotImplementedError

    def judge(self, pair):
        raise NotImplementedError
        
    def __str__(self):
        return self.__class__.__name__
