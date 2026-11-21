class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # for i in range(len(nums)):
        #     multiplicand = 1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             multiplicand *= nums[j]
        #     output.append(multiplicand)

        # return output


        #approach 2:
        #check for the zero count as if 0 is there then the product can be zerod
        #first count the num of 0's; if >1 then ret all 0s; if =1 then just the position where the 0 is there product needs to be calculated; if no zero then just product of all elements by the num at each pos.

        zero_count = 0
        non_zero_product = 1

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                non_zero_product *= num

        n = len(nums)
        output = [0] * n

        if zero_count > 1:
            return output

        for i, num in enumerate(nums):
            if zero_count == 1:
                if num == 0:
                    output[i] = non_zero_product
            else:
                output[i] = non_zero_product // num

        return output