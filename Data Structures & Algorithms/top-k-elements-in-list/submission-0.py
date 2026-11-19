from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #given nums arr and int k. 
        #ret list of k most frequent elements

        #store the number and their respective freq


        dicti = defaultdict(int)
        #iterate through nums; if Y -> inc freq 
        #else add the element to the dict
        #sort the dictionary items using a lambda func with the expression being the frequency and sorting in descending order
        #ret a list of the number only by slicing the k items of the sorted items

        for i in nums:
            dicti[i] += 1 #O(N)

        sorted_items = sorted(dicti.items(), key=lambda x: x[1], reverse=True) #O(N log N)
        

        return [num for num,freq in sorted_items[:k]] #O(k)

        


        





