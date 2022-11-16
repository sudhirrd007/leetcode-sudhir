# number = 0001
# fileName = 0001_Two_sum.py
# difficulty = easy
# language = python
# leetcodeLink = https://leetcode.com/problems/two-sum/
# tags = ARRAY, HASHTABLE
# end = 

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(nums.__len__()):
            for j in range(nums.__len__()):
                if(i<j):
                    if((nums[i] +nums[j]) == target ):
                        return [i,j]
                        