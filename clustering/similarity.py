import math
import numpy as np
from sklearn.cluster import SpectralClustering, KMeans




class Cluster():
    def __init__(self, detect_radius, similarity_threashold, data):
        self.detect_radius = detect_radius
        self.similarity_threashold = similarity_threashold
        self.data = data
        self.similarity_matrix = None

    def is_closed(self, p1, p2):
        """

        :param p1: point 1
        :param p2: point 2
        :return:
        """
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) < self.detect_radius

    def cal_similarity(self, r1, r2):
        count = 0.0

        for i in range(len(r1)):
            is_closed_flag = False
            for j in range(len(r2)):
                if self.is_closed(r1[i], r2[j]):
                    is_closed_flag = True

            if is_closed_flag:
                count += 1.0

        return count / len(r1)

    def cal_similarity_matrix(self):
        self.similarity_matrix = np.zeros((len(self.data), len(self.data)))

        for i1, r1 in enumerate(self.data):
            for i2, r2 in enumerate(self.data):
                self.similarity_matrix[i1][i2] = self.cal_similarity(r1, r2)

    def clustering(self):
        clusters = [0] * len(self.similarity_matrix)
        i = 1
        for x, row in enumerate(self.similarity_matrix):
            for y, item in enumerate(row):
                if item >= self.similarity_threashold and self.similarity_matrix[y][x] >= self.similarity_threashold:
                    if clusters[x] != 0:
                        clusters[y] = clusters[x]
                    else:
                        clusters[y] = clusters[x] = i
                        i = i + 1
        return clusters

    def clustering_k(self, num_clusters):

        # eigen_values, eigen_vectors = np.linalg.eigh(self.similarity_matrix)
        #
        # clusters = KMeans(n_clusters=num_clusters, init='k-means++').fit_predict()

        clusters = SpectralClustering(n_clusters=num_clusters).fit(self.similarity_matrix)

        return clusters.labels_

