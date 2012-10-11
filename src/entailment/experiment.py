#!/usr/bin/python
# Bismillahi-r-Rahmani-r-Rahim

#train_path = r'/home/daoud/Downloads/rte/dev.xml'
train_path = r'/home/daoud/Data/rte-dataset/guardian-entailment.xml'
#test_path = r'/home/daoud/Downloads/rte/dev2.xml'
test_path = r'/home/daoud/git/discoexperiments/data/rte/rte1/development/dev2.xml'

import xml.dom.minidom as minidom

from LexicalStrategy import LexicalStrategy
from NaiveBayesStrategy import NaiveBayesStrategy
from NGramOverlap import NGramOverlap

import random

def get_text(pair, name):
    return pair.getElementsByTagName(name)[0].childNodes[0].nodeValue

def get_pairs(path):
    data = minidom.parse(path)
    r = []
    pairs = data.getElementsByTagName('pair')
    for p in pairs:
        t = get_text(p,'t')
        h = get_text(p,'h')
        r += [(t,h,p.getAttribute('value') == 'TRUE')]
    return r

def run(strategy, train_data, test_data):
    print "Strategy: ", str(strategy)
    #train_data = get_pairs(train_path)
    strategy.train(train_data)

    #test_data = get_pairs(test_path)
    test_data_no_judgments = [(x[0],x[1]) for x in test_data]
    correct = []
    confusion = [[0,0],[0,0]]
    judgments = strategy.judge(test_data_no_judgments)
    for i in range(len(test_data)):
        j = judgments[i]
        gold = test_data[i][2]
        confusion[j][gold] += 1
    print "Confusion:"
    print "[TN,FN]", confusion[0], "<-- Judged False"
    print "[FP,TP]", confusion[1], "<-- Judged True"
    c = confusion[0][0] + confusion[1][1]
    print "Accuracy: ", float(c)/len(test_data)
    print
    #print s.ents

    #return train

def run_naive_bayes():
    s = NaiveBayesStrategy()
    run(s, get_pairs(train_path), get_pairs(test_path))
    return s

if __name__ == '__main__':
    l = LexicalStrategy()
    strategies = [
        #NGramOverlap(2),
        #NGramOverlap(3),
        #NGramOverlap(4),
        NaiveBayesStrategy()]
    for s in strategies:
        train_data = get_pairs(train_path)
        test_data = get_pairs(test_path)
        #random.shuffle(train_data)
        #index = int(len(train_data)*.66)
        #d = run(s, train_data[:index],train_data[index:])
        d = run(s, train_data,test_data)
    
