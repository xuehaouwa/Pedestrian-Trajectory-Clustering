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
        pass

    @staticmethod
    def center_of_bounding_box(left, top, right, bottom):
        center_x = (left + right) / 2
        center_y = (top + bottom) / 2
        a_x = round(center_x, 4)
        a_y = round(center_y, 4)

        return [a_x, a_y]


DL = DataLoader('TownCentre-groundtruth.txt')

data = DL.read_from_txt()
print(data)
print(np.shape(data))
ped_num = DL.get_pedestrian_num()
print(ped_num)
# data = pd.read_csv('TownCentre-groundtruth.txt')
# data.columns = ['id', 'frame', 'headVaild', 'bodyVaild', 'headLeft', 'headTop', 'headRight', 'headBottom', 'bodyLeft', 'bodyTop', 'bodyRight', 'bodyBottom']
# a = data.as_matrix()


#
#
#
# def get_trajectories(data, person_num):
#
#     all_traj = []
#     for j in range(person_num):
#
#         traj = []
#         for i in range(len(data)):
#
#             if data[i][0] == j:
#                 traj.append(center_of_bounding_box(data[i][-4], data[i][-3], data[i][-2], data[i][-1]))
#         all_traj.append(traj)
#
#     return all_traj
#
#
# data = get_trajectories(a, 231)
