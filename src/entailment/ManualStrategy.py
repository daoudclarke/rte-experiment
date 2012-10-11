# Bismillahi-r-Rahmani-r-Rahim
#
# 'Strategy' for RTE that takes manual input

line = "--------------------------------------------------------------------------------"

class ManualStrategy:
    def train(self, pairs):
        pairs = [x[:2] for x in pairs]
        self.judge(pairs)

    
    def judge(self, pairs):
        for t, h in pairs:
            print line
            print "TEXT"
            print line
            print t
            print line
            print "HYPOTHESIS"
            print line
            print h
            print line
            v = ''
            while v.lower() not in ['t','f']:
                print "Input 't' or 'f':"
                v = raw_input('> ')
            entailment = {'t':True, 'f':False}[v]
            print entailment
        
