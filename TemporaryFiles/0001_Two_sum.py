# number-srd = 0001
# title-srd = Two Sum
# filename-srd = 0001_Two_sum.py
# difficulty-srd = easy
# language-srd = python
# tags-srd = ARRAY, HASHTABLE
# leetcodelink-srd = https://leetcode.com/problems/two-sum/
# acceptancerate-srd = 49.1%
# notes-srd = 
# end-srd = 

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(nums.__len__()):
            for j in range(nums.__len__()):
                if(i<j):
                    if((nums[i] +nums[j]) == target ):
                        return [i,j]
                        