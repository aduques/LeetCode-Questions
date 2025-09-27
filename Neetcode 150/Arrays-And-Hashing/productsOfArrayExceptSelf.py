from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # the numbers itself can the keys, and we can add the rest of the numbers
        # as the values
        # then, we can go through each of the values and calculate the product


        # SAME PROCESS AS FOR TOP K FREQUENCY

        seen = {}

        # make the current number as the key, then add the other values as values
        for i in range(len(nums)):
            seen[nums[i]] = []
            for j in range(len(nums)):
                # do not add the number itself into its own values
                if i != j:
                    seen[nums[i]].append(nums[j])
        
        res = []

        # use a loop to iterate through the keys in the seen map
        # get the product of the values in the current num's values
        # append the product to the result list
        for num in nums:
            product = 1
            for num in seen[num]:
                product *= num
            res.append(product)
        
        return res

        # SUMMARY: (n^2) run time because of the nested loop
        # in order to be able to add the current value as the key, and the other
        # values as its value, a NESTED LOOP was used. All the other values
        # was added and the current value was skipped over when iterated again

        # Another nested loop is used to iterate through the HASHMAP. The outer loop
        # is to select the key, and the inner loop gets the product of the key's values.
        # The product is added to the result list

        # run time would be (n^2 + n^2)

solution = Solution()
case1 = [1,2,4,6]

print('Output: ', solution.productExceptSelf(case1))