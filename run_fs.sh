#!/bin/sh
python train-ntu.py --output-dir $1 --linprobe --resume $2 --few-shot --data-test-meta data/50_few_shot_depth_support_val_ann.txt --data-meta data/few_shot_depth_support_ann.txt --epochs 300