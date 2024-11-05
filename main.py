def find_min_cost(money, days, cost):
    n = len(cost)
    min_cost = float('inf')

    current_sum = sum(cost[:days])
    min_cost = current_sum

    for i in range(1, n - days + 1):
        current_sum = current_sum - cost[i - 1] + cost[i + days - 1]
        if current_sum < min_cost:
            min_cost = current_sum

    if min_cost <= money:
        return f"money: {min_cost}" 
    
    for d in range(days - 1, 0, -1):
        current_sum = sum(cost[:d])
    if current_sum <= money:
        return f"days: {d}"
    
    for i in range(1, n-d + 1):
        current_sum = current_sum - cost[i - 1] + cost[i + d - 1]
        if current_sum <= money:
            return f"days: {d}"
         
    return "days: 0"
