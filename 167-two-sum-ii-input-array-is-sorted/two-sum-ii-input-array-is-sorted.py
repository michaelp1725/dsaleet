class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        l = 0
        r = length - 1
        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum == target:
                return [l + 1, r + 1]  
            elif curr_sum < target:
                l += 1
            else:
                r -= 1
            
        
        
# 1 3 4 5 7 10 12 16 18 trying to get 14
        
        
        
 # 1 3 6 7 10 13 15        
        
        
        
        
        
        
        
        #hard coded
        
        #l = length - 2
        #r = length - 1
        #sum = numbers[l] + numbers[r]
        #while sum != target:
            #if sum > target:
                #l -= 1
            #else:
                #l = r -2
                #r -= 1
        #return l + 1, r + 1


# 1 3 6 7 10 13 15 