from typing import List




class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums = [1, 1, 22, 3, 4, 5, 6, 6, 7, 7, 8]
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i]
                # Incrementing insertIndex count by 1
                insertIndex = insertIndex + 1
        return insertIndex
        
