class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs=[]
        def combine_helper(arr,num):
            if len(arr)==k:
                combs.append(arr)
            for i in range(num,n+1):
                combine_helper(arr+[i],i+1)
                
        combine_helper([],1)
        return combs
