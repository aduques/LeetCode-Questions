from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use hash map to store seen numbers, if encounter seen, return true

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
    
    def isAnagram(self, s: str, t: str) -> bool:
        # An anagram is a string that contains the exact same 
        # characters as another string, but the order of the characters can be different.

        # sort the string and compare

        return ''.join(sorted(s)) == ''.join(sorted(t))
    

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # in order to solve this in one pass, we want to find the difference
        # of the target and the current number
        # then with the difference, we want to check if the difference exists
        # in the list

        # dictionary to store indices
        indices = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in indices:
                # return the index i and the index of the diff
                return [indices[diff], i]
            # if not found store the index and num pair into the dictionary,
            # so that it can be searched for in other iterations
            indices[num] = i
        
        return [0,0]
    

solution = Solution()
case1 = [1,2,3,3]
s = "racecar"
t = "carrace"
case2 = [3,4,5,6]
target = 7

print('Output: ', solution.hasDuplicate(case1))
print('Output:', solution.isAnagram(s,t))
print('Output:', solution.twoSum(case2, 7))