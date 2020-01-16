# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter, longest, hs = 0, 0, []
        for i in s:
            hs.append(i)
            counter = counter + 1
            if hs.count(i) > 1:
                start = hs.index(i) + 1
                counter = counter - start
                s = s[start:len(s)]
                hs.clear()
                hs = hs + list(s[0:counter-1])
                hs.append(i)
            if len(hs) > longest:
                longest = len(hs)

        return longest


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))