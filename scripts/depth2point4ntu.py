import os
import numpy as np
import argparse
from matplotlib.image import imread
from glob import glob
import argparse
parser = argparse.ArgumentParser(description='Depth to Point Cloud')

parser.add_argument('--input', default='/atlas/u/yzcong/datasets/ntu/nturgb+d_depth_masked', type=str)
parser.add_argument('--output', default='/atlas/u/yzcong/datasets/ntu/video_fixed', type=str)
parser.add_argument('-n', '--action', type=int, default=1)

args = parser.parse_args()


W = 512
H = 424

'''
def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

mkdir(args.output)
'''

xx, yy = np.meshgrid(np.arange(W), np.arange(H))
focal = 280

def single_proc(video_path):
    
    video_name = video_path.split('/')[-1]
    print(f'start {video_name}')
    if os.path.exists(os.path.join(args.output, video_name + '.npz')):
        print("skip")
        return

    point_clouds = []
    for img_name in sorted(os.listdir(video_path)):
        img_path = os.path.join(video_path, img_name)
        img = imread(img_path) # (H, W)

        depth_min = img[img > 0].min()
        depth_map = img

        x = xx[depth_map > 0]
        y = yy[depth_map > 0]
        z = depth_map[depth_map > 0]
        x = (x - W / 2) / focal * z
        y = (y - H / 2) / focal * z

        points = np.stack([x, y, z], axis=-1)
        point_clouds.append(points)

    np.savez_compressed(os.path.join(args.output, video_name + '.npz'), data=point_clouds)


import multiprocessing
pool = multiprocessing.Pool(8)

pool.map(single_proc, sorted(glob('%s/S%03d*'%(args.input, args.action))))
