class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequenceSet = set(nums)
        longest = 0
        
        for num in sequenceSet: 
            if num - 1 not in sequenceSet:
                current = num
                counter = 0
                while current in sequenceSet:
                    counter += 1
                    current += 1
                longest = max(longest, counter)
        return(longest)

