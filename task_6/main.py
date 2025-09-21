items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# -----------------------------
# Greedy algorithm
# -----------------------------
def greedy_algorithm(items, budget):
    # Calculate "calories per unit cost"
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"]/x[1]["cost"], reverse=True)
    
    total_cost = 0
    selected_items = []
    
    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(name)
            total_cost += info["cost"]
    
    return selected_items

# -----------------------------
# Dynamic programming
# -----------------------------
def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(items)
    
    # dp[i][w] = max calories using first i items with budget w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        cost = items[names[i-1]]["cost"]
        calories = items[names[i-1]]["calories"]
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]
    
    # Restore selected items
    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(names[i-1])
            w -= items[names[i-1]]["cost"]
    
    return selected_items[::-1]  # reverse for convenience


print("Greedy algorithm:", greedy_algorithm(items, budget))
print("Dynamic programming:", dynamic_programming(items, budget))