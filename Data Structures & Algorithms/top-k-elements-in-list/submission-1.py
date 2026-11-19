from collections import defaultdict, Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #given nums arr and int k. 
        #ret list of k most frequent elements

        #store the number and their respective freq


        # dicti = defaultdict(int)
        # #iterate through nums; if Y -> inc freq 
        # #else add the element to the dict
        # #sort the dictionary items using a lambda func with the expression being the frequency and sorting in descending order
        # #ret a list of the number only by slicing the k items of the sorted items

        # for i in nums:
        #     dicti[i] += 1 #O(N)

        # sorted_items = sorted(dicti.items(), key=lambda x: x[1], reverse=True) #O(N log N)
        

        # return [num for num,freq in sorted_items[:k]] #O(k)


        #approach 2 : min heap
        #create a freq_map[alt to dicti in approach1]
        #iterate through the freq_map and push elements with freq first to a heap of len k cuz heap sorts tuples by the first element.
        #by using a min heap, only the elements with higher freq get to stay in the heap and the smaller freq gets popped as when a bigger element enters the min heap
        #ret a list of the numbers by iterating through the minheap
        freq_map = Counter(nums) #num : freq O(N)
        #maintaing a heap of size k - O(N log K)
        min_heap = []
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq,num))
            if len(min_heap) > k:
                heapq.heappop(min_heap) #O(log K) - evicting the smallest freq

        return [num for freq, num in min_heap]





        


        





