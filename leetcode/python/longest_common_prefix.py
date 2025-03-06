from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
    
if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    solution = Solution()
    print(f"'{solution.longestCommonPrefix(strs)}'")
    strs = ["dog","racecar","car"]
    solution = Solution()
    print(f"'{solution.longestCommonPrefix(strs)}'")