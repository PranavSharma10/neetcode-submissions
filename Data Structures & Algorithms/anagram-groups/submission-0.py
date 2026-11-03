#parse every word in the list, sort them alphbetically,
# next, if that word is already in your dict add it in the list with that key
# if not create a new list and add it in there
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for string in strs:
            key = "".join(sorted(string))
            if key not in out:
                out[key] = []
            out[key].append(string)
        return list(out.values())

                
