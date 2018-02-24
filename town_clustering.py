"""
2018.02.03

@author: Hao Xue
"""

from clustering.clustering import Clustering
from data.process_data import DataLoader
import numpy as np
from utils.drawing import DrawTrajectory
from clustering.dtw_distance import DtwCluster
import time
from clustering.similarity import Cluster
from clustering.editdistance_clustering import Cluster

detect_radius = 100
similarity_threashold = 0.5


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

# cluster = Clustering()
#
# start_time = time.time()
# res = cluster.clusterSpectral(town_trajectories[0: 184], 6)
#
# print(time.time() - start_time)
#
# print(res)
#
# drawer = DrawTrajectory('town_background.png')
# drawer.draw_clusterd_trajectories(town_trajectories[0: 184], res, 6)


# similarity method

# clustering = Cluster(detect_radius, similarity_threashold, town_trajectories[0: 184])
#
# clustering.cal_similarity_matrix()
#
# clusters = clustering.clustering_k(6)


# dtw distance method

#clustering = DtwCluster(town_trajectories[0: 184])
#
#clustering.cal_dis_matrix()
#
#clusters = clustering.clustering_k(6)
#
#drawer = DrawTrajectory('town_background.png')
#drawer.draw_clusterd_trajectories(town_trajectories[0: 184], clusters, 6)

clustering = Cluster(town_trajectories[0: 184])

clustering.cal_dis_matrix()

clusters = clustering.clustering_k(6)

drawer = DrawTrajectory('town_background.png')
drawer.draw_clusterd_trajectories(town_trajectories[0: 184], clusters, 6)
