class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda x:-x[1])
        totalUnits, i = 0, 0
        while truckSize > 0 and i < len(boxTypes):
            if truckSize >= boxTypes[i][0]:
                truckSize -= boxTypes[i][0]
                totalUnits += boxTypes[i][0] * boxTypes[i][1]
            else:
                totalUnits += truckSize * boxTypes[i][1]
                truckSize = 0
            i += 1
        return totalUnits
