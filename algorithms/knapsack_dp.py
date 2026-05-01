def solve_01_knapsack(capacity, weights, values):
    """
    Solves the 0/1 Knapsack problem using Dynamic Programming.
    This approach ensures that items are either taken as a whole (1) or not at all (0).
    It is ideal for scenarios where items are indivisible (e.g., electronic gadgets, luxury items).
    
    Returns: (max_value, selected_items_indices)
    """
    n = len(weights)
    # Create a 2D array for DP table: dp[item_count][capacity]
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # Max of (including the current item, excluding the current item)
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                # Item is too heavy, cannot include it
                dp[i][w] = dp[i-1][w]

    # The bottom-right cell contains the maximum value
    max_value = dp[n][capacity]
    
    # Backtrack to find which items were selected
    selected_indices = []
    res = max_value
    w = capacity
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # If the value is different from the cell above, the item was included
        if res != dp[i-1][w]:
            selected_indices.append(i-1)
            res -= values[i-1]
            w -= weights[i-1]

    return max_value, selected_indices
