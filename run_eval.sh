#!/bin/bash
python train-ntu.py --output-dir output/50fs_support --eval --resume /atlas/u/yzcong/pst/output/50fs/model_15.pth --data-test-meta data/50_few_shot_depth_val_ann.txt --data-meta data/few_shot_depth_support_ann.txt --batch-size 28
