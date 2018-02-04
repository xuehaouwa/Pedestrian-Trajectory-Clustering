"""
2018.02.03

@author: Hao Xue
"""

from clustering.clustering import Clustering
from data.process_data import DataLoader
import numpy as np


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

res = cluster.clusterSpectral(town_trajectories[0: 8], 2)

print(res)
