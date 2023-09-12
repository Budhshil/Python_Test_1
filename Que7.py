def longest_common_subsequence(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create a 2D DP table to store the lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The value in the bottom-right cell of the DP table is the length of LCS
    return dp[m][n]

# Example usage:
s1 = "AGGTAB"
s2 = "GXTXAYB"
result = longest_common_subsequence(s1, s2)
print(result)
