class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_dict = defaultdict(list)

        for i in strs:
            sorted_key = "".join(sorted(i))

            anag_dict[sorted_key].append(i)

        return list(anag_dict.values())