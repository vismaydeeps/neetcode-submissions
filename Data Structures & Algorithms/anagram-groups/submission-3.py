class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #approach 1:  - Time O(N .K)
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



        #approach 2: Time -O(N . KlogK)
        # create the default dict
        # loop through the strings arr
        # sort the chars and use the sorted version as the key and append the string as the value
        # return the list of dict values

        #groups = defaultdict(list)

        #for s in strs:
            #groups["".join(sorted(s))].append(s)
        #return list(groups.values())


