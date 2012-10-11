#!/usr/bin/python
#
# Bismillahi-r-Rahmani-r-Rahim
# Create an RTE dataset

import os
#import nltk
#from nltk.tokenize import sent_tokenizer
from nltk import word_tokenize, tokenize
from nltk.tag import pos_tag
#from entailment.NGramOverlap import NGramOverlap
#from save_dataset import save
from csv import DictWriter
import nltk

data_dir = '/home/daoud/Data/rte'

output_path = '../output/'

pos_threshold = 0.578
neg_threshold = 0.4
#rte = NGramOverlap(3, pos_threshold)
#max_pairs = 200000
max_pairs = 10

ne_tagger = nltk.data.load('chunkers/maxent_ne_chunker/english_ace_binary.pickle')

def valid_sentence(text):
    if len(text) < 30:
        return False
    if len(text) > 500:
        return False
    if text.count('"') % 2 != 0:
        return False
    if text.count('\n') > 1:
        return False
    return True

def get_entities(sentence):
    tags = pos_tag(word_tokenize(sentence))
    parse = ne_tagger.parse(tags)
    entities = set([x[0] for x in parse.pos() if x[-1] == 'NE'])
    return entities

def process_documents(path):
    num_positive = 0
    num_negative = 0
    
    subdirs = os.listdir(path)
    subdirs.sort()
    output_file = open('pairs.csv','w')
    fieldnames = ["path", "text", "hypothesis", "entails"]
    output = DictWriter(output_file, fieldnames)
    for s in subdirs:
        new_path = os.path.join(path,s)
        files = os.listdir(new_path)
        files.sort()
        for f in files:
            file_path = os.path.join(new_path,f)
            print file_path
            file_ = open(file_path)
            headline = file_.readline()[:-1]
            body = file_.read()
            sentences = tokenize.sent_tokenize(body)
            old_entities = sentence_entities = get_entities(sentences[0])
            if valid_sentence(headline) and valid_sentence(sentences[0]):
                headline_entities = get_entities(headline)
                if len(headline_entities & sentence_entities) > 0:
                    print "-- Entailing --"
                    print sentences[0]
                    print headline
                    print
                    output.writerow({"path":file_path,
                                     "text":headline,
                                     "hypothesis":sentences[0],
                                     "entails":1})
                    num_positive += 1
            if num_positive >= max_pairs and num_negative >= max_pairs:
                output_file.close()
                return
            if num_positive < num_negative:
                continue
            for i in range(1, len(sentences) - 1):
                text = sentences[i]
                hypothesis = sentences[i + 1]
                text_entities = old_entities
                old_entities = hypothesis_entities = get_entities(hypothesis)
                if not valid_sentence(text) or not valid_sentence(hypothesis):
                    continue
                if len(hypothesis_entities & text_entities) > 0:
                    print "-- Non entailing --"
                    print text
                    print hypothesis
                    output.writerow({"path":file_path,
                                     "text":text,
                                     "hypothesis":hypothesis,
                                     "entails":0})
                    num_negative += 1
                    if num_positive < num_negative:
                        break

    output_file.close()

def get_files(path):
    result = []
    subdirs = os.listdir(path)
    subdirs.sort()
    for s in subdirs:
        new_path = os.path.join(path,s)
        files = os.listdir(new_path)
        files.sort()
        for f in files:
            result.append(os.path.join(new_path, f))
    return result

if __name__ == "__main__":
    global data_dir
    print get_files(data_dir)[:100]
    process_documents(data_dir)
