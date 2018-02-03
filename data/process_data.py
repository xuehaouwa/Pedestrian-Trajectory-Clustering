# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:33:57 2017

@author: Hao Xue
"""

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
import pandas as pd


class DataLoader():
    def __init__(self, data_path):
        self.data_path = data_path
        self.raw_data = None
        self.data_matrix = None
        self.pedestrian_num = None
        self.all_trajectories = []
        self.trajectories = []

    def read_from_txt(self):
        self.raw_data = pd.read_csv(self.data_path)
        self.raw_data.columns = ['id', 'frame', 'headVaild', 'bodyVaild', 'headLeft', 'headTop', 'headRight',
                                 'headBottom', 'bodyLeft', 'bodyTop', 'bodyRight', 'bodyBottom']

        self.data_matrix = self.raw_data.as_matrix()

        return self.data_matrix

    def get_pedestrian_num(self):
        self.pedestrian_num = np.size(np.unique(self.data_matrix[:, 0]))

        return self.pedestrian_num

    def get_trajectories(self):

        for i in range(self.pedestrian_num):
            temp_traj = []

            for j in range(len(self.data_matrix)):

                if self.data_matrix[j][0] == i:
                    temp_traj.append(self.center_of_bounding_box(self.data_matrix[j][-4], self.data_matrix[j][-3],
                                                                 self.data_matrix[j][-2], self.data_matrix[j][-1]))

            self.all_trajectories.append(temp_traj)

        return self.all_trajectories
    
    def traj_filter(self, length_threshold):
        
        for i in range(len(self.all_trajectories)):
            if len(self.all_trajectories[i]) >= length_threshold:
                self.trajectories.append(self.all_trajectories[i])
                
        return self.trajectories
    
    @staticmethod
    def center_of_bounding_box(left, top, right, bottom):
        center_x = (left + right) / 2
        center_y = (top + bottom) / 2
        a_x = round(center_x, 4)
        a_y = round(center_y, 4)

        return [a_x, a_y]


DL = DataLoader('TownCentre-groundtruth.txt')

data = DL.read_from_txt()
#print(data)
print(np.shape(data))
ped_num = DL.get_pedestrian_num()
print(ped_num)

all_trajectories = DL.get_trajectories()


#print(all_trajectories)
print(len(all_trajectories))

traj = DL.traj_filter(40)



