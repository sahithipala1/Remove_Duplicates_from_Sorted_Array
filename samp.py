from typing import List

nums = [1, 1, 2, 2, 2, 3, 4, 5]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print("sum of the two number")
        answer = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and (i < j) and (nums[i] + nums[j]) == target:
                    answer.append(i)
                    answer.append(j)
        
        return answer
