# Bismillahi-r-Rahmani-r-Rahim

import os
import csv

import save_dataset

def collate(path, output):
    fieldnames = ["path", "text", "hypothesis", "entails"]
    files = os.listdir(path)
    pairs = []
    for filename in files:
        if not filename.startswith('pairs'):
            continue
        full_path = os.path.join(path, filename)        
        print "Processing file: ", full_path
        f = open(full_path)
        reader = csv.DictReader(f, fieldnames)
        for row in reader:
            pairs.append( (row["text"],
                           row["hypothesis"],
                           [True, False][int(row["entails"])]) )
    save_dataset.save_pairs(pairs, output)

if __name__ == "__main__":
    collate('../output/', '../dataset/dataset.xml')
