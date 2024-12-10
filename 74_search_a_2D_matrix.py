from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def recurssiveSearch(leftIdx,rightIdx):
            mid= leftIdx+((rightIdx-leftIdx)//2)
            

            if(target>=matrix[mid][0] and target<=matrix[mid][len(matrix[mid])-1]):
                l,r,arr=0,len(matrix[mid])-1,matrix[mid]
                while(l<=r):
                    mid= l+((r-l)//2)

                    if(arr[mid]==target):
                        return True
                    elif (target>arr[mid]):
                        l=mid+1
                    else:
                        r=mid-1
                return False

                
            elif (target < matrix[mid][0]):
                rightIdx-=1
                if(rightIdx<leftIdx):
                    return False
                return recurssiveSearch(leftIdx,rightIdx)
            else:
                leftIdx+=1
                if(leftIdx>rightIdx):
                    return False
                return recurssiveSearch(leftIdx,rightIdx)

        return recurssiveSearch(0,len(matrix)-1)
                

        