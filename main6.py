def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name = item_names[i - 1]
        cost = items[item_name]['cost']
        calories = items[item_name]['calories']
        for j in range(budget + 1):
            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(item_names[i - 1])
            j -= items[item_names[i - 1]]['cost']

    return selected_items, dp[n][budget]


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if budget >= details['cost']:
            selected_items.append(item)
            total_calories += details['calories']
            budget -= details['cost']

    return selected_items, total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_result, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", greedy_result)
print("Сумарна калорійність:", greedy_calories)

dp_result, dp_calories = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Обрані страви:", dp_result)
print("Сумарна калорійність:", dp_calories)