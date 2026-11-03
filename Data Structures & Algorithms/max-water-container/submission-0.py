# two pointers one at start and one at end
# create a variable for max area which maximum area of all seen, initially 0
# multiply first and last, get the area and compare with max area if greater than it update value in that variable
# compare left and right, whichever is smaller, increment it respectively, until left<right
# in the end output max area
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areaMax = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            areaMax = max(areaMax, area)
            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
        return areaMax
