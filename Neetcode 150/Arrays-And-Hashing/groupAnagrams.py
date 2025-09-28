from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a dictionary to store the matching strings
        # the point of anagrams is that each matching pair of
        # words contains the same letters, and doesn't care about
        # the order of the letters

        # in order to be able to compare the strings, we can use
        # a sort() to sort the letters alphabetically, so that we can
        # just check if the sorted words are equivalent

        # since we want to find the anagrams for each word in the list
        # (we want a sublist for each word), each of the words will
        # be a key in the result dictionary

        # the plan is to iterate through the list once and update the dictionary

        res = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))
            #if (sorted_string in res):
            #    res[sorted_string].append(string)
            #else:
            #    res[sorted_string] = []
            # this was missing, always add the current string to its own sublist
            # ALSO WRONG, because you are adding to its sublist twice
            # res[sorted_string].append(string)

            # only need to check if not in the list
            if (sorted_string not in res):
                res[sorted_string] = []
            res[sorted_string].append(string)

        
        # incorrect because 
        # TypeError: Your output was <class 'dict'>, but the expected return type is List[List[str]].
        # return res
        return list(res.values())


solution = Solution()
case1 = ["act","pots","tops","cat","stop","hat"]

print('Output: ', solution.groupAnagrams(case1))