class Solution:
    def findClosestElements(self, arr, k, x):
        # binary search to find the closest
        left, right, closest = 0, len(arr) - 1, 0
        if x <= arr[0]:
            closest = left
        elif x >= arr[-1]:
            closest = right
        else:
            while arr[left] <= x <= arr[right]:
                mid = int((left + right) / 2)
                if arr[mid] == x:
                    closest = mid
                    break
                else:
                    if x < arr[mid]:
                        right = mid
                    else:
                        left = mid
                if left + 1 == right:
                    if x - arr[left] <= arr[right] - x:
                        closest = left
                    else:
                        closest = right
                    break
        result = [arr[closest]]
        left = closest - 1
        right = closest + 1
        k -= 1
        while 0 <= left and right <= len(arr) - 1 and k > 0:
            if x - arr[left] <= arr[right] - x:
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
            k -= 1
        if k > 0:
            if 0 <= left:
                while k:
                    result.append(arr[left])
                    left -= 1
                    k -= 1
            else:
                while k:
                    result.append(arr[right])
                    right += 1
                    k -= 1
        return sorted(result)


if __name__ == "__main__":
    arr = [1, 2, 4]
    k = 1
    x = 3
    print(Solution().findClosestElements(arr, k, x))
