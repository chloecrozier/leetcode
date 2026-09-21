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

        for rect in rects:
            # print(rect)
            for x in range(rect[0], rect[2] + 1):
                # print("\t", (x, rect[1]), (x, rect[3]))
                # edges
                if (x, rect[1]) in edges:
                    edges[(x, rect[1])][0] += 1
                else:
                    edges[(x, rect[1])] = [1, 0]
                if (x, rect[3]) in edges:
                    edges[(x, rect[3])][0] += 1
                else:
                    edges[(x, rect[3])] = [1, 0]

                # corners
                if x == rect[0] or x == rect[2]:
                    if (x, rect[1]) in edges:
                        edges[(x, rect[1])][1] += 1
                    else:
                        edges[(x, rect[1])] = [0, 1]
                    if (x, rect[3]) in edges:
                        edges[(x, rect[3])][1] += 1
                    else:
                        edges[(x, rect[3])] = [0, 1]
                

            for y in range(rect[1] + 1, rect[3]):
                # print("\t\t", (rect[0], y), (rect[2], y))
                # edges
                if (rect[0], y) in edges:
                    edges[(rect[0], y)][0] += 1
                else:
                    edges[(rect[0], y)] = [1, 0]
                if (rect[2], y) in edges:
                    edges[(rect[2], y)][0] += 1
                else:
                    edges[(rect[2], y)] = [1, 0]

                # corners
                if y == rect[1] or y == rect[3]:
                    if (rect[0], y) in edges:
                        edges[(rect[0], y)][1] += 1
                    else:
                        edges[(rect[0], y)] = [0, 1]
                    if (rect[2], y) in edges:
                        edges[(rect[2], y)][1] += 1
                    else:
                        edges[(rect[2], y)] = [0, 1]
            
            # get the outer rectanlges boundaries
            if minX > rect[0]:
                minX = rect[0]
            if maxX < rect[2]:
                maxX = rect[2]
            if minY > rect[1]:
                minY = rect[1]
            if maxY < rect[3]:
                maxY = rect[3]

        # print(minX, minY, "\t", maxX, maxY)

        # find inner overlaps
        for key, val in edges.items():
            # print(key, val)
            if key[0] > minX and key[0] < maxX:
                if key[1] > minY and key[1] < maxY:
                    if val[0] == 1:
                        return False
                    if val[1] >= 0:
                        # print("\t\t\t", key, val)
                        if val[0] > val[1] + 1:
                            return False

        # find outer gaps
        for key, val in edges.items():
            if key[0] == minX or key[0] == maxX:
                if key[1] > minY and key[1] < maxY:
                    # print("\t\t\t", key, val)
                    # if there is a gap on the left or right edges
                    if val[1] == 1:
                        return False
                else:
                    # if a corner, corner is not unique
                    if val[1] > 1:
                        return False
            if key[1] == minY or key[1] == maxY:
                if key[0] > minX and key[0] < maxX:
                    # print("\t\t\t", key, val)
                    # if there is a gap on the top or bottom edges
                    if val[1] == 1:
                        return False
                else:
                    # if a corner, corner is not unique
                    # print("\t\t\t\t\t\t\t", key, val)
                    if val[1] > 1:
                        return False

            # print("\t", key, val)

        
        return True
