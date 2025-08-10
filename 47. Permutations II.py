from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False]*len(nums)

        def backtrack(path):
            print("step1:Calling backtrack with path:", path)  # fixed indentation here
            if len(path) == len(nums):
                print("step7:Base case reached with path:", path,"return")
                result.append(path[:])
                return 
        

            for i in range(len(nums)):
                if used[i]:
                    print(f"step2.0:{nums[i],i} used, skip to next")
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    print("step2.1:previous not used, skip to next i")
                    continue
                
                print(f"step3:use {nums[i],i} ")
                used[i] = True
                path.append(nums[i])
                print(f"step4:{path} appended, backtrack({path})\n")
                backtrack(path)
                print(f"step5.0:out backtrack(),path before: {path}")
                path.pop()
                print(f"step5.1:pop(),path after: {path}")
                print(f"step6:{nums[i],i} change to not used")
                used[i] = False
            
        backtrack([])
        return result



sol = Solution()
nums = [1,1,2]
result = sol.permuteUnique(nums)
print("All unique permutations:")
for perm in result:
    print(perm)
    
    
    
    
    
    
