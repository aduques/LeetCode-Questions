from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # seems that sorting the nums list is allowed, so the plan is to
        # sort, then iterate, then count
        # if the current value is 1 higher than the recorded value
        # then increment the res

        res = 0
        rec = 0

        #for i in range(len(nums)):
            # difference between current and rec should be 1
        #    diff = nums[i] - rec
        #    if (diff == 1 and nums[i] != rec):
        #        res = res + 1
        #        rec = nums[i]
        
        # AFTER HINT, USE A HASH SET TO KEEP TRACK
        numSet = set(nums) # put the nums in the list into a set
        res = 0 # return value
        for num in numSet:
            if (num - 1) not in numSet: # the current number is the smallest in the sequence
                length = 1 # begin the sequence count
                while (num + length) in numSet: # increments the sequence count until not in it
                    # increment length, this incremented value will be checked to see if it is
                    # part of the set
                    # if not in the set, it means the sequence stops
                    length = length + 1
                # after each iteration, update the new max
                # initially I got this incorrect, because I was checking the max inside of the while loop
                # this is wrong because if the max is only calculated in the while loop
                # in the case of the sequence ends, it does not count the max after it ends, so
                # it will always be inaccurate. THEREFORE, max should be calculated after
                # sequence ends (outside of the while loop)
                res = max(res, length)
        return res
    
solution = Solution()
print('Output: ', solution.longestConsecutive([2,20,4,10,3,4,5]))
