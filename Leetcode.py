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


# A array of strings of pranthasis is given.
# the array is valid if all the opening bracket is closed with a close bracket.
# the closing bracket should be of the same type as that of the opening baracket.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # stacks to store all the brackets                     
        opening_br = set(["(","[","{"])# getting all types of opening bracket.
        br_relationship = {
            ")":"(","}":"{","]":"["
        }# showing the relationship of all the closing bracket and closing bracket
    
        for i in s : #uing a for loop to itterate through the aray
            if i in opening_br :
                stack.append(i)
            elif stack and stack[-1] == br_relationship[i] :#if stack is not empty and if the lass element in the stack and the closing bracket maches then pop the set of brackets 
                stack.pop()
            else:
                return False

        if stack:
            return False 
        else :
            return True



