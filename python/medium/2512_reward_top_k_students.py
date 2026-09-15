# https://leetcode.com/problems/reward-top-k-students/
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        goodWords = set(positive_feedback)
        badWords = set(negative_feedback)
        pq = []
        for i in range(len(report)):
            score = 0
            for w in report[i].split():
                if w in goodWords:
                    score += 3
                if w in badWords:
                    score -= 1
            heapq.heappush(pq, (-score, student_id[i]))
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        return res
