from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = [i for i in nums if i != val]
        k = len(nums) - len(new)
        for i in range(k):
            new.append("_")
        return(k, new)
    
temp = Solution()
print(temp.removeElement([3,2,2,3], 3))