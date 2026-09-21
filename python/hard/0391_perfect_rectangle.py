# https://leetcode.com/problems/perfect-rectangle/description/
class Solution:
    def isRectangleCover(self, rects: list[list[int]]) -> bool:
        if len(rects) == 1:
            return True

        rectSet = set()
        for rect in rects:
            rectSet.add(tuple(rect))

        if len(rects) != len(rectSet):
            return False

        minX = rects[0][0]
        maxX = rects[0][2]
        minY = rects[0][1]
        maxY = rects[0][3]
        # general edges of the continuous rectangles
        edges = {}
        actualArea = 0

        for rect in rects:
            actualArea += (rect[2] - rect[0]) * (rect[3] - rect[1])
            # corners
            for x in range(rect[0], rect[2] + 1):
                if x == rect[0] or x == rect[2]:
                    if (x, rect[1]) in edges:
                        edges[(x, rect[1])] += 1
                    else:
                        edges[(x, rect[1])] = 1
                    if (x, rect[3]) in edges:
                        edges[(x, rect[3])] += 1
                    else:
                        edges[(x, rect[3])] = 1
                
            # corners
            for y in range(rect[1] + 1, rect[3]):
                if y == rect[1] or y == rect[3]:
                    if (rect[0], y) in edges:
                        edges[(rect[0], y)] += 1
                    else:
                        edges[(rect[0], y)] = 1
                    if (rect[2], y) in edges:
                        edges[(rect[2], y)] += 1
                    else:
                        edges[(rect[2], y)] = 1
            
            # get the outer rectanlges boundaries
            if minX > rect[0]:
                minX = rect[0]
            if maxX < rect[2]:
                maxX = rect[2]
            if minY > rect[1]:
                minY = rect[1]
            if maxY < rect[3]:
                maxY = rect[3]

        expectedArea = (maxX - minX) * (maxY - minY)
        if actualArea > expectedArea:
            return False

        # find inner overlaps
        for key, val in edges.items():
            if key[0] > minX and key[0] < maxX:
                if key[1] > minY and key[1] < maxY:
                    if val == 1:
                        return False

        # find outer gaps
        for key, val in edges.items():
            if key[0] == minX or key[0] == maxX:
                if key[1] > minY and key[1] < maxY:
                    # if there is a gap on the left or right edges
                    if val == 1:
                        return False
                else:
                    # if a corner, corner is not unique
                    if val > 1:
                        return False
            if key[1] == minY or key[1] == maxY:
                if key[0] > minX and key[0] < maxX:
                    # if there is a gap on the top or bottom edges
                    if val == 1:
                        return False
                else:
                    # if a corner, corner is not unique
                    if val > 1:
                        return False
        
        return True
