#1 Palindrom Numbers 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse =  str(x)[::-1]
        if str(x) == reverse:
            return True
        else:
            return False
        

#2 Two sums 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap.keys():
                return [i,hashMap[diff]]
            else:
                hashMap[nums[i]] = i

#3 Contains Dublicates 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_1 = set(nums)
        if len(nums) != len(set_1):
            return True
        else:
            return False 
        
#4 Best Time To Buy and Sell Stocks 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 0
        max_profit = 0
        for i in range(len(prices)):
            if i == 0:
                min_price = prices[i]
            elif prices[i] < min_price:
                min_price = prices[i]
            elif (prices[i] - min_price > max_profit):
                max_profit = prices[i] - min_price 
        return max_profit
        
#5 Valid Anagrams 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            if sorted(s)==sorted(t):
                return True
            else:
                return False
            
# Valid Palendrome 

actual_string = []



