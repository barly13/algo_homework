from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    dp = [[1] * (i + 1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, len(dp[i]) - 1):
            dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j] - 1

    return dp
