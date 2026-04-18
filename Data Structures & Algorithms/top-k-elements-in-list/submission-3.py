class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number (first pass)
        # Store in a frequency table from 1 to len(input)
        # Append the results from the right of array

        results = []
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, counter in count.items():
            freq[counter].append(num)
        
        for i in reversed(range(len(freq) - 1)):
            for num in freq[i]:
                results.append(num)
                if len(results) == k:
                    return results

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