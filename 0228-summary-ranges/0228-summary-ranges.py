class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        array = []
        start = nums[0]
        end = nums[0]
        print(start)
        print(end)
        for i in nums[1:]:
            if(i == end+1):
                end = i
            else:
                if(start == end):
                    array.append(str(start))
                    print(array)
                else:
                    array.append(str(start)+"->"+str(end))
                start = i
                end = i
        if(start==end):
            array.append(str(start))
        else:
            array.append(str(start)+"->"+str(end))
        return array
                    
        