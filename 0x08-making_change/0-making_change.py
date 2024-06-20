#!/usr/bin/python3
"""
Module for making change using dynamic programming
"""


def makeChange(coins, total):
    """
    Function to determine the fewest number
    of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    dp = [-1] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != -1:
                if dp[i] == -1:
                    dp[i] = dp[i - coin] + 1
                else:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total]
