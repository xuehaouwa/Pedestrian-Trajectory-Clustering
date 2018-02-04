import cv2


class DrawTrajectory():
    def __init__(self, background_scene):
        self.background = cv2.imread(background_scene)
        self.trajectory_data = None
        self.clustering_label = None
        self.cluster_num = None
        # red, green, blue, yellow, cyan, magenta
        self.color = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 0, 255)]

    def draw_clusterd_trajectories(self, trajectory_data, clustering_label, cluster_num):
        self.trajectory_data = trajectory_data
        self.cluster_num = cluster_num
        self.clustering_label = clustering_label

        for cluster in range(self.cluster_num):
            for i in range(len(self.clustering_label)):
                if self.clustering_label[i] == cluster:
                    self.draw_single_trajectory(self.background, self.trajectory_data[i], self.color[cluster])

        cv2.imwrite('clustered.jpg', self.background)
        cv2.imshow('img', self.background)
        cv2.waitKey(0)

    @staticmethod
    def draw_single_trajectory(img, trajectory, color):
        for i in range(len(trajectory) - 1):
            cv2.line(img, (int(trajectory[i][0]), int(trajectory[i][1])), (int(trajectory[i+1][0]), int(trajectory[i+1][1])), color=color, thickness=2, lineType=cv2.LINE_4)
