class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=0
        for n in nums:
            if n != val:
                nums[k]=n
                k+=1
        return k