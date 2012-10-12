#!/usr/bin/python
#
# Bismillahi-r-Rahmani-r-Rahim
# Create an RTE dataset

import os
import sys
from csv import DictWriter

import nltk
from nltk import word_tokenize, tokenize
from nltk.tag import pos_tag

data_dir = '/home/daoud/Data/rte'
output_path = '../output/'

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

def process_documents(file_paths, output_file):
    num_positive = 0
    num_negative = 0
    
    fieldnames = ["path", "text", "hypothesis", "entails"]
    output = DictWriter(output_file, fieldnames)
    for file_path in file_paths:
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
                                 "text":sentences[0],
                                 "hypothesis":headline,
                                 "entails":1})
                num_positive += 1
        if num_positive >= max_pairs and num_negative >= max_pairs:
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
    if len(sys.argv) == 3:
        num_procs = int(sys.argv[1])
        proc_num = int(sys.argv[2])
    else:
        num_procs = 1
        proc_num = 1

    print "Number of procedures: ", num_procs
    print "Running procedure number: ", proc_num
    output_file_name = os.path.join(output_path, 'pairs%i.csv' % proc_num)
    print "Output file: ", output_file_name

    output_file = open(output_file_name,'w')
    files = get_files(data_dir)
    files_to_process = [files[i] for i in range(proc_num, len(files), num_procs)]
    process_documents(files_to_process, output_file)
    output_file.close()
