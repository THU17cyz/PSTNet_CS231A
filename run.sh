#!/bin/bash
python train-ntu.py --output-dir $1 --data-meta $2 --data-test-meta $3 --batch-size 28
