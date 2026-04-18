class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # One liner: Array[count] => list of nums
        # Outline
        # 1. 1st pass: count in a dict
        # 2. 2nd pass: count in an array as freq
        # 3. Iterate from right
        # 4. Return the result
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        results = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, counter in count.items():
            freq[counter].append(num)
        print(freq)
        for i in reversed(range(len(freq))):
            for num in freq[i]:
                results.append(num)
                if len(results) == k:
                    return results
        return results