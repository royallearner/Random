def knapsackdp(weights,  Values, Capacity):
    n = len(weights)
    dp = [[0 for _ in range(Capacity + 1)] for _ in range(n + 1)]

    # for i in range(1,len(weights)+1):
    #     for w in range(Capacity +1):
    #         if weights[i-1] <= w:
    #             dp[i][w] = max(dp[i-1][w], Values[i-1] + dp[i-1][w-weights[i-1]])
    for i in range(1, n + 1):
        for w in range(Capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + Values[i - 1])
                
            else:
                dp[i][w] = dp[i - 1][w]


    return dp[n][Capacity]

Values = [20, 25, 40]
weights = [25, 20, 30]
print(knapsackdp(weights,Values,50))