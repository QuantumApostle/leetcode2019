# LC 593
import math


class Solution:
    def validSquare(self, p1, p2, p3, p4):
        distance_table = [[0.0] * 4 for i in range(4)]
        points = [p1, p2, p3, p4]
        for i in range(len(points)):
            for j in range(len(points)):
                distance_table[i][j] = self.get_distance(points[i], points[j])

        diagonal_points = [0]
        adj_points = []
        norm_factor = min(distance_table[0][1:])
        if norm_factor == 0:
            return False
        for i in range(1, 4):
            ratio = distance_table[0][i] / norm_factor
            if ratio == 1:
                adj_points.append(i)
            elif int(ratio * 1000) == int(math.sqrt(2) * 1000):
                diagonal_points.append(i)
            else:
                return False

        if len(diagonal_points) != 2 or len(adj_points) != 2:
            return False
        for i in [0, 1]:
            if distance_table[diagonal_points[1]][adj_points[i]] != norm_factor:
                return False

        return True

    def get_distance(self, p, q):
        return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

    def print_table(self, a):
        for l in a:
            print(l)
        print("\n")


if __name__ == "__main__":
    result = Solution().validSquare([0.0, 1.0], [-1.0, 0.0], [1.0, 0.0], [0.0, -1.0])
    print(result)
