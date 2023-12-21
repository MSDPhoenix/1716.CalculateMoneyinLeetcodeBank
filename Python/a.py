class Solution(object):
    def totalMoney(self, n):
        total = 0
        for x in range(n):
            total += 1 + x%7 + int(x/7)
        return total 