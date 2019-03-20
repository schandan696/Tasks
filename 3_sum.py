import sys
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        sortedList = sorted(A)
        lenOflist = len(A)
        mindiff = sys.maxint
        for i in range(len(sortedList)-2):
            j = i + 1
            k = lenOflist - 1
            while j < k:
                tempSum = sortedList[i] + sortedList[j] + sortedList[k]
                diff = abs(B - tempSum)
                if diff == 0:
                    return tempSum
                if diff < mindiff:
                    mindiff = diff
                    result = tempSum
                if tempSum <= B:
                    j += 1
                else:
                    k -= 1
        return result