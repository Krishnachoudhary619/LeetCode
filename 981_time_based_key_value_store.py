class TimeMap:

    def __init__(self):
        self.keyDict={}
        self.timeDict={}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        newT= self.timeDict.get(timestamp,[])
        newT.append((key,value))
        self.timeDict[timestamp]= newT
        
        newKeyData= self.keyDict.get(key,[])
        newKeyData.append(timestamp)
        newKeyData.sort()
        self.keyDict[key]=newKeyData
    
    def get(self, key: str, timestamp: int) -> str:
        keyData= self.keyDict.get(key,None)
        
        if(keyData==None):
            return ''
            
        # Find the timestamp which is <= given timestamp.

        l,r=0,len(keyData)-1
        ans=float('inf')
        while l<=r:
            mid=(l+r)//2
            if(keyData[mid]<=timestamp):
                ans=keyData[mid]
            if(keyData[mid]==timestamp):
                break
            
            elif keyData[mid]<timestamp:
                l=mid+1
            else:
                r=mid-1
        if(ans>timestamp):
            return ''
        for i in self.timeDict[ans]:
            if(key==i[0]):
                return i[1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)