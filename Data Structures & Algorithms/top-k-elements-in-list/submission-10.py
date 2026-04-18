class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Intuition: Store the mapping of count => num and then iterate from the right
        results = []
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]  # occurences => [num1, num2]
        for num in nums:
            count[num] += 1
        # count == {1:1,2:2,3:3}
        for num, occurence in count.items():
            freq[occurence].append(num)
        # freq == [[1],[2],[3],[],[],[]]
        for i in reversed(range(len(freq))):  # 6, 5, 4, 3, 2, 1
            for num in freq[i]:
                results.append(num)
                if len(results) == k:
                    return results

    