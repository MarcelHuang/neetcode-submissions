class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            results.append(sorted_count[i][0])
        return results