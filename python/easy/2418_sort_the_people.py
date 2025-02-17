# https://leetcode.com/problems/sort-the-people/description/
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        people = []
        for i in range(len(names)):
            people.append([names[i], heights[i]])
        
        people = sorted(people, key=lambda x: x[1], reverse=True)

        for name, height in people:
            res.append(name)

        return res
