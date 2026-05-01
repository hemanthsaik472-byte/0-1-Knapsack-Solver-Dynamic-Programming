def solve_fractional_knapsack(capacity, weights, values):
    """
    Solves the Fractional Knapsack problem using a Greedy approach.
    This approach allows items to be divided, making it ideal for scenarios
    where items are divisible (e.g., grains, liquids, or raw materials).
    
    Returns: (max_value, selected_items_details)
    """
    n = len(weights)
    # Create a list of items with their value-to-weight ratios
    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append({
            'id': i,
            'weight': weights[i],
            'value': values[i],
            'ratio': ratio
        })

    # Sort items based on ratio in descending order (Greedy choice)
    items.sort(key=lambda x: x['ratio'], reverse=True)

    total_value = 0.0
    current_capacity = capacity
    selected_items = []

    for item in items:
        if current_capacity <= 0:
            break
        
        if item['weight'] <= current_capacity:
            # If current capacity is enough, take the whole item
            current_capacity -= item['weight']
            total_value += item['value']
            selected_items.append({
                'id': item['id'],
                'fraction': 1.0,
                'weight_taken': item['weight'],
                'value_gained': item['value']
            })
        else:
            # Otherwise, take a fraction of the remaining capacity
            fraction = current_capacity / item['weight']
            value_gained = item['value'] * fraction
            total_value += value_gained
            selected_items.append({
                'id': item['id'],
                'fraction': fraction,
                'weight_taken': current_capacity,
                'value_gained': value_gained
            })
            current_capacity = 0 # Knapsack is full

    return total_value, selected_items
