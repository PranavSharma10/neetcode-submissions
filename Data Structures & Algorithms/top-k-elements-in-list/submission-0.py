# First create a dict which keeps the mapping of number in the list against its frequency in the list
# parse through each number in the list, if new create a new mapping
# if not add 1 to the existing kv pair 
# in the end make a list of all values and sort, return the top k vals in the list
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyDict = {}
        for num in nums:
            frequencyDict[num] = frequencyDict.get(num, 0) + 1
        sortedNums = sorted(frequencyDict, key = frequencyDict.get, reverse = True)
        return sortedNums[:k]
