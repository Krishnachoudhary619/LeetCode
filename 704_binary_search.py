from typing import List  # Import List from typing

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def reccursiveSearch(startIdx,endIdx ):
            idx=(endIdx+startIdx)//2
           
            if(target>nums[idx]):
                idx+=1
                if(endIdx<idx):
                    return -1
                return reccursiveSearch(idx,endIdx)
            elif target<nums[idx]:
                idx-=1
                if(startIdx>idx):
                    return -1
                return reccursiveSearch(startIdx,idx)
            else:
                return idx
        return reccursiveSearch(0,len(nums)-1)
        