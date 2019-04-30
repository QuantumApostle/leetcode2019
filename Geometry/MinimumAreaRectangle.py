# LC 939
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set()
        for p in points:
            x, y = p
            points_set.add((x, y))
        n = len(points)
        result = float("inf")
        for i in range(n-1):
            x_0, y_0 = points[i]
            for j in range(i+1, n):
                x_1, y_1 = points[j]
                if x_0 == x_1 or y_0 == y_1:
                    continue
                if (x_1, y_0) in points_set and (x_0, y_1) in points_set:
                    result = min(result, abs((x_0-x_1)*(y_0-y_1)))
        return 0 if result == float("inf") else result