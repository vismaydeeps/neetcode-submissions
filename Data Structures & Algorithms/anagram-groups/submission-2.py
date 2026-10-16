class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #approach 1:
        # create a default dict
        #loop through the string array, create a hash key using the difference trick by using ord -> this will create same list for similar items
        # convert this hash key into a tuple so its immuatable and can be used as a key in the default dict
        # append the original string to the matching anagram
        #return the values of the dict


        groups = defaultdict(list)

        for s in strs:
            #using this as the hash key
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            groups[key].append(s)
        return list(groups.values())


