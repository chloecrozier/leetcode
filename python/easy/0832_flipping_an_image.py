# https://leetcode.com/problems/flipping-an-image/description/
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        l = len(image[0])
        for i in range(len(image)):
            for j in range((l // 2)):
                image[i][j], image[i][l - j - 1] = image[i][l - j - 1], image[i][j]
                image[i][j] ^= 1
                image[i][l - j - 1] ^= 1
            if l % 2:
                image[i][l // 2] ^= 1
        return image
