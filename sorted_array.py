from typing import List

s = [1, 1, 2, 3, 4, 5, 3, 3]
print(s.sort())
print(len(s))
s.reverse()
print(s)
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#    assert nums[i] == expectedNums[i];
# }


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
