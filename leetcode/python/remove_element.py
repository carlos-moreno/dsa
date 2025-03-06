from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeElement([3, 2, 2, 3], 3))
    print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
