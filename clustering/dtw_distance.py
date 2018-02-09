from dtw import dtw
from numpy.linalg import norm
import numpy as np
from sklearn.cluster import SpectralClustering


def custom_norm(x, y):
    temp = np.array([x, y])

    return norm(temp)


class DtwCluster():
    def __init__(self, data):
        self.data = data
        self.data_len = len(data)
        self.dtw_distance_matrix = np.zeros((self.data_len, self.data_len))

    def cal_dis_matrix(self):

        for i in range(self.data_len):
            for j in range(self.data_len):
                self.dtw_distance_matrix[i][j] = self.cal_dtw_distance(self.data[i], self.data[j])

    def clustering_k(self, num_clusters):

        # eigen_values, eigen_vectors = np.linalg.eigh(self.similarity_matrix)
        #
        # clusters = KMeans(n_clusters=num_clusters, init='k-means++').fit_predict()

        # clusters = SpectralClustering(n_clusters=num_clusters).fit(self.dtw_distance_matrix)

        clusters = SpectralClustering(n_clusters=num_clusters, affinity='precomputed').fit(self.dtw_distance_matrix)

        return clusters.labels_

    @staticmethod
    def cal_dtw_distance(t1, t2):
        dist, cost, acc, path = dtw(t1, t2, dist=custom_norm)

        return dist
