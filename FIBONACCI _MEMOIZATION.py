#FIBONACCI_MEMOZIATION

print(">>> FIBONACCI_MEMOZIATION")
print("")#...space


def fibonacci_memoization(n, memo):
    if n <= 1:
        return n
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization (n - 2, memo)
        return memo[n]

n = 107
memo = {}
print("---The required result is:",fibonacci_memoization(n,memo))
