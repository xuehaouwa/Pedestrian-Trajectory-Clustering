# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:09:28 2018

@author: 21992674

use edit distance for clustering
"""

import numpy as np
from sklearn.cluster import SpectralClustering, KMeans
import edit_distance



class Cluster():
    def __init__(self, data):

        self.data = data
        self.similarity_matrix = None


    def cal_similarity_matrix(self):
        self.similarity_matrix = np.zeros((len(self.data), len(self.data)))

        for i1, r1 in enumerate(self.data):
            for i2, r2 in enumerate(self.data):
                self.similarity_matrix[i1][i2] = edit_distance.edit_distance(r1, r2)
                

    def clustering_k(self, num_clusters):

        # eigen_values, eigen_vectors = np.linalg.eigh(self.similarity_matrix)
        #
        # clusters = KMeans(n_clusters=num_clusters, init='k-means++').fit_predict()

        clusters = SpectralClustering(n_clusters=num_clusters).fit(self.similarity_matrix)

        return clusters.labels_

