# Dynamic Programming Pattern

Dynamic programming is a powerful technique used to solve complex problems by breaking them down into simpler subproblems. It is particularly useful for optimization problems where the solution can be constructed from solutions to smaller subproblems.

## Key Concepts

1. **Overlapping Subproblems**: Dynamic programming is applicable when the problem can be broken down into smaller, overlapping subproblems that can be solved independently.

2. **Optimal Substructure**: A problem exhibits optimal substructure if an optimal solution to the problem can be constructed from optimal solutions of its subproblems.

## Techniques

- **Memoization**: This technique involves storing the results of expensive function calls and reusing them when the same inputs occur again. It is a top-down approach.

- **Tabulation**: This technique involves building a table in a bottom-up manner, filling in the table based on previously computed values. It is an iterative approach.

## Common Dynamic Programming Problems

- Fibonacci Sequence
- Coin Change Problem
- Longest Common Subsequence
- 0/1 Knapsack Problem
- Edit Distance

## Example

### Fibonacci Sequence (Memoization)

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

### Fibonacci Sequence (Tabulation)

```python
def fibonacci(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]
```

## Conclusion

Dynamic programming is a crucial technique in algorithm design that can significantly reduce the time complexity of problems that exhibit overlapping subproblems and optimal substructure. Understanding and mastering this pattern can greatly enhance your problem-solving skills in competitive programming and technical interviews.

## LeetCode Problems

| Problem | Difficulty | 