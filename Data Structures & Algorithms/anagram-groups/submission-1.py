class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_dict = defaultdict(list)

        for s in strs:

            count = [0] * 26
            for i in s:
                count[ord(i) - ord('a')] += 1

            key = tuple(count)
            anag_dict[key].append(s)

        return list(anag_dict.values())