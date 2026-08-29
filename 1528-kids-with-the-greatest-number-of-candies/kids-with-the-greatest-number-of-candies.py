class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        mx=max(candies)
        for i in candies:
            if i+extraCandies >=mx:
                result.append(True)
            else:
                result.append(False)
        return result

        