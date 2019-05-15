import heapq


class Solution:
    def kClosest(self, points, K):
        tmp = []
        for p in points:
            dist = pow(p[0], 2) + pow(p[1], 2)
            heapq.heappush(tmp, [dist, p])
        return [x[1] for x in heapq.nsmallest(K, tmp)]


if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    print(Solution().kClosest(points, k))
