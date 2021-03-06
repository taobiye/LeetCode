#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 8, 2015
# Question: 189-Rotate-Array
# Link:     https://leetcode.com/problems/rotate-array/
# ==============================================================================
# Rotate an array of n elements to the right by k steps.
# 
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated 
# to [5,6,7,1,2,3,4].
# 
# Note:
# Try to come up as many solutions as you can, there are at least 3 different 
# ways to solve this problem.
# 
# [show hint]
# 
# Hint:
# Could you do it in-place with O(1) extra space?
# Related problem: Reverse Words in a String II
# ==============================================================================
# Method: In place with O(1) extra space
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        if n > 1 and  k > 0:
            nums[:] = nums[n-k:] + nums[:n-k]