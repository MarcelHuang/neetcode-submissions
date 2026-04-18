class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Force
        # Count the frequency of each number
        results = []
        count = {}  # num => freq
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        k_most_frequent = sorted(count, key=count.get, reverse=True)[:k]
        


















































        count = collections.defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] += 1
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res