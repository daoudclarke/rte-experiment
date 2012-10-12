#!/bin/bash
#

# ===========================================
# Parameters for Sun Grid Engine submition
# ============================================

# Name of job
#$ -N RteDataset

# Shell to use
#$ -S /bin/bash

# All paths relative to current working directory
#$ -cwd

# List of queues
#$ -q serial.q

# Define parallel environment for 3 cores
#$ -pe openmp 3-

# Send mail to. (Comma separated list)
#$ -M dc34

# When: [b]eginning, [e]nd, [a]borted and reschedules, [s]uspended, [n]one
#$ -m beas

# Validation level (e = reject on all problems)
#$ -w e

# Merge stdout and stderr streams: yes/no
#$ -j yes


python dataset.py 3 0 &
python dataset.py 3 1 &
python dataset.py 3 2 &
wait
