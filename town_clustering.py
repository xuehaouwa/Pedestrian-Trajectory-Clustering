"""
2018.02.03

@author: Hao Xue
"""

from clustering.clustering import Clustering
from data.process_data import DataLoader
import numpy as np
from utils.drawing import DrawTrajectory
import time

def town_data():
    DL = DataLoader('./data/TownCentre-groundtruth.txt')
    data = DL.read_from_txt()
    print(np.shape(data))
    ped_num = DL.get_pedestrian_num()
    print(ped_num)
    all_trajectories = DL.get_trajectories()
    print(len(all_trajectories))

    traj = DL.traj_filter(40)

    return traj


town_trajectories = town_data()

cluster = Clustering()

start_time = time.time()
res = cluster.clusterSpectral(town_trajectories[0: 18], 2)


print(time.time()-start_time)

print(res)

drawer = DrawTrajectory('town_background.png')
drawer.draw_clusterd_trajectories(town_trajectories[0: 18], res, 2)


