
# def fib(n):
#     return 1 if n == 0 or n == 1 else fib(n-1) + fib(n-2)

# def fib(n, cache=None):
#     if n == 0 or n == 1: return 1
#     if cache is None: cache = {}
#     if n in cache: return cache[n]

#     result = fib(n-1, cache) + fib(n-2, cache)
#     cache[n] = result
#     return result

from inspect import signature
from typing import Any

# class memoize(dict):
#     def __init__(self, func):
#         self.func = func 
#         self.signature = signature(func)
    
#     def __missing__(self, key):
#         (arg, kwarg) = key
#         self[key] = val = self.func(*arg, **dict(kwarg))
#         return val

#     def __call__(self, *args, **kwds):
#         key = self.signature.bind(*args, **kwds)
#         return self[key.args, frozenset(key.kwargs.items())]
    
# @memoize
# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(40))


def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1 ) for _ in range(n+1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max( dp[i-1][w], values[i-1] + dp[i-1][w-weights[i-1]] )
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]


weights = [4, 3, 1]
values = [4, 3, 1.5]
capacity = 4

result = knapsack(weights, values, capacity)
print(result)
