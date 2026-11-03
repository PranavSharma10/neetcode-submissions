# start parsing the string, if the first bracket is a closed bracket return false
# as soon as you encounter the first open bracket, append its close bracket into a list and start looking for the last string in the list, by moving further in the loop
# if a new open bracket turns up, add its closed bracket in the list and start looking for that, if another bracket is encountered and not the last one, returrn false
# if the match is found pop the element in the list and look for the last element in the list
# in the end once we parse the complete string and our list is not empty, return false else true

class Solution:
    def isValid(self, s: str) -> bool:
        pPairs = {"{":"}", "(":")", "[":"]"}
        pList = []
        for string in s:
            if string in pPairs:
                pList.append(pPairs[string])
            else:
                if not pList or pList[-1] != string:
                    return False
                pList.pop()
        return len(pList) == 0 
            