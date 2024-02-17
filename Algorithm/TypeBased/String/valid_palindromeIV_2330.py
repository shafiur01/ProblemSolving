"""
You are given a 0-indexed string s consisting of only lowercase English letters. In one operation, you can change any character of s to any other character.
Return true if you can make s a palindrome after performing exactly one or two operations, or return false otherwise.

Example 1:

Input: s = "abcdba"
Output: true
Explanation: One way to make s a palindrome using 1 operation is:
- Change s[2] to 'd'. Now, s = "abddba".
One operation could be performed to make s a palindrome so return true.
Example 2:

Input: s = "aa"
Output: true
Explanation: One way to make s a palindrome using 2 operations is:
- Change s[0] to 'b'. Now, s = "ba".
- Change s[1] to 'b'. Now, s = "bb".
Two operations could be performed to make s a palindrome so return true.
Example 3:

Input: s = "abcdef"
Output: false
Explanation: It is not possible to make s a palindrome using one or two operations so return false.
"""


class Solution:
    def makePalindrome(self, s: str): # -> bool:
        l, r = 0, len(s)-1
        count = 0
        while l < r:
            if s[l] != s[r]:
                count += 1
                if count > 2:
                    return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    binarySearch = Solution()
    # notice the array is sorted
    string = "zbcfedcba"
    print(binarySearch.makePalindrome(string))