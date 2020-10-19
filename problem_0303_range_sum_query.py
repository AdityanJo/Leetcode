class NumArray:

    def __init__(self, nums: List[int]):
        self.length=len(nums)
        if self.length==0:
            self.opt=[]
        else:
            self.opt=[nums[0]]
        for i in range(1,self.length):
            self.opt.append(nums[i]+self.opt[-1])

    def sumRange(self, i: int, j: int) -> int:
        if i==0 and j!=self.length-1:
            return self.opt[j]
        elif i==0 and j==self.length-1:
            return self.opt[-1]
        else:
            return self.opt[j]-self.opt[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
