class Solution:
    def average(self, salary: List[int]) -> float:
        a = salary
        total = sum(a) - max(a) - min(a) # 全部加總-最大-最小
        N = len(a) - 2 # 因為扣掉最大值、最小值, 數目少2個
        return total / N

        # return ( sum(salary)-max(salary)-min(salary) ) / (len(salary)-2)