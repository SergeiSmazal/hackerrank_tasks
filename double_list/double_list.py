class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        Option 1:
        new_nums = []
        new_nums2 = []

        for j in range(0, len(nums)):
            new_nums.append(nums[j])
            new_nums2.append(nums[j])

        return new_nums + new_nums2
        """

        """
        Option 2:
        new_nums = new_nums2 = [a for a in nums]

        return new_nums + new_nums2
        """

        """
        Option 3:
        return nums + nums
        """

        return nums + nums
    
print(Solution().getConcatenation([1, 2, 1]))