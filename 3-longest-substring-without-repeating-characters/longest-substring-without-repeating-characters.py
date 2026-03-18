class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to store unique characters in current window
        charSet = set()

        # Left pointer of sliding window
        l = 0

        # Store maximum length found
        res = 0

        # Right pointer expands the window
        for r in range(len(s)):

            # If duplicate found, shrink window from left
            while s[r] in charSet:
                # Remove leftmost character from set
                charSet.remove(s[l])

                # Move left pointer forward
                l += 1

            # Add current character to set
            charSet.add(s[r])

            # Update max length
            # Window size = r - l + 1
            res = max(res, r - l + 1)

        return res