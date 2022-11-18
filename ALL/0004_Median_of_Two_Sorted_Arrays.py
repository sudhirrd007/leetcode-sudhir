# number-srd = 0004
# title-srd = Median of Two Sorted Arrays
# filename-srd = 0004_Median_of_Two_Sorted_Arrays.py
# difficulty-srd = hard
# language-srd = python
# tags-srd = ARRAY, BINARYSEARCH, DIVIDEANDCONQUER
# leetcodelink-srd = https://leetcode.com/problems/two-sum/
# acceptancerate-srd = 49.1%
# notes-srd = 
# end-srd = 


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted((nums1 + nums2))
        length = arr.__len__() - 1

        ans = float(( arr[int(length/2)] + arr[int((length+1)/2)] ) / 2)

        return ans