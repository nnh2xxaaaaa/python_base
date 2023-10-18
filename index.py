from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the string with the minimum length in the list
        min_len = min(len(s) for s in strs)

        print('min_len',min_len)

        # Initialize the longest common prefix
        common_prefix = ""

        for i in range(min_len):
            # Get the character at the current position for the first string
            char = strs[0][i]

            # Check if this character is common to all strings
            if all(s[i] == char for s in strs):
                common_prefix += char
            else:
                break

        print(f'common_prefix',common_prefix)

        return common_prefix

solution = Solution()
solution.longestCommonPrefix(["flower","flow","flight"])