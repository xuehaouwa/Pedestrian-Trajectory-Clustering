# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:02:27 2018

@author: 21992674
"""

from clustering.clustering import Clustering
from data.process_data import DataLoader
import numpy as np
from utils.drawing import DrawTrajectory
import time
from clustering.dtw_distance import DtwCluster


def file2matrix(filename):
    data = np.loadtxt(filename, dtype=int)
    data = np.reshape(data, [-1, 3])
    return data


def get_coord_from_txt(filename, ped_ID):
    data = file2matrix(filename)
    coord = []
    for i in range(len(data)):
        coord.append([data[i][0], data[i][1]])
    coord = np.reshape(coord, [-1, 2])
    return coord


def select_trajectory(data, frame_num):
    if len(data) >= frame_num:
        return True
    else:
        return False


def get_all_trajectory(total_pedestrian_num):
    data = []

    for i in range(total_pedestrian_num):
        filename = './Annotation/' + str(i + 1).zfill(6) + '.txt'
        ped_ID = i + 1
        data.append(get_coord_from_txt(filename, ped_ID))

    return data


def traj_length(data, length):
    out = []

    for i in range(len(data)):
        if select_trajectory(data[i], length):
            out.append(data[i])

    return out


data_NYGC = get_all_trajectory(12684)
data = traj_length(data_NYGC, 40)

cluster = Clustering()

start_time = time.time()
clustering = DtwCluster(data[0: 3800])

clustering.cal_dis_matrix()

clusters = clustering.clustering_k(6)

print(time.time() - start_time)

drawer = DrawTrajectory('000000.jpg')
drawer.draw_clusterd_trajectories(data[0: 3800], clusters, 6)
