#!/usr/bin/python
# Bismillahi-r-Rahmani-r-Rahim
#
# Manual analysis of RTE data

analysis_size = 10


from experiment import *
from ManualStrategy import ManualStrategy
import random

def analyse():
    data = get_pairs(train_path)
    positive = [x for x in data if x[2]]
    negative = [x for x in data if not x[2]]
    positive = random.sample(positive, analysis_size)
    negative = random.sample(negative, analysis_size)
    data = positive + negative
    random.shuffle(data)
    run(ManualStrategy(), data, [])

if __name__ == "__main__":
    analyse()
