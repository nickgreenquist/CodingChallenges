'''
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
def splitN(n):
    digits = []
    while n > 0:
        d = n % 10
        digits.insert(0, d)
        n = n // 10
    return digits

def isHappy(n):
    seen = set([n])
    while n != 1:
        digits = splitN(n)
        n = 0
        for d in digits:
            n += (d*d)
        if n in seen:
            return False
        seen.add(n)
    return True

print(isHappy(19))