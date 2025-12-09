class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        # Sort by units per box (descending)
        boxTypes.sort(key=lambda x: -x[1])

        units = 0
        
        for boxes, units_per_box in boxTypes:
            if truckSize == 0:
                break

            # Take as many as possible
            take = min(truckSize, boxes)
            units += take * units_per_box
            truckSize -= take
        
        return units
