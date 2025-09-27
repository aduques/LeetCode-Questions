from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # learning from similar questions that involves arrays and sets
        # use a set to store the seen numbers
        # use sort() to sort the numbers, and iterate through the list
        # backwards

        # if the set has not seen the number, then add to set, otherwise
        # skip past it (it is a duplicate) ... or not skip since sets cannot
        # have duplicates anyways

        # add into set until you have k unique values, so keep track of this
        # by incrementing count, and keep the loop going until count = k

        # the list should only have


        ## READ THE QUESTION WRONG, IT IS LOOKING FOR K FREQUENT

        # instead, use a HASHMAP to store the unique numbers and their count
        # then sort them by frequency

        count = {}

        for num in nums:
            if num in nums:
                count[num] = 1 + count.get(num, 0)

        # create a list of lists where the length of the lists is the size
        # of nums
        # we want a list of lists instead of a singular array because it is
        # possible for numbers to have the same frequency
        # we have exactly len(nums) lists in the frequency list for the case that
        # a number has a frequency of len(nums)
        frequency = [[] for i in range(len(nums) + 1)]

        for num,count in count.items():
            frequency[count].append(num)
        
        res = []

        # iterate through frequency backwards and taking the k most frequent
        # continue taking from the highest frequency count until it is empty,
        # and then check the previous list if it contains any
        # continue this until k numbers have been chosen
        for i in range(len(frequency)-1,0,-1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        #SUMMARY OF WHAT HAS BEEN DONE: Use a HASHMAP/ HASHSET to count the
        # frequencies of the numbers in the list
        # Create a LIST OF LISTS to store the numbers based on their frequencies
        # Each frequency is a list because it is possible for multiple numbers to have
        # the same frequency
        # Iterate through the frequency list and append the k frequent numbers
        # stop looping through when len(res) = k
        # if the frequency list has been went through, go check the next highest frequency list
        # and add the numbers there until len(res) = k


solution = Solution()
case1 = [1,2,2,3,3,3]
k = 2
print('Output: ', solution.topKFrequent(case1, 2))