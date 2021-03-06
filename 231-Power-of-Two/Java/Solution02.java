// ==============================================================================
// Author:   Tao Li (taoli@ucsd.edu)
// Date:     Jul 7, 2015
// Question: 231-Power-of-Two
// Link:     https://leetcode.com/problems/power-of-two/
// ==============================================================================
// Given an integer, write a function to determine if it is a power of two.
// ==============================================================================
// Method: loop
// ==============================================================================

public class Solution02 {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) return false;
        while (n >= 2) {
            if (n % 2 == 1) return false;
            n /= 2;
        }
        return true;
    }
}