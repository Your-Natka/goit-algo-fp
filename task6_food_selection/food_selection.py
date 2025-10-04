def greedy_algorithm(items, budget):
    """
    Жадібний алгоритм: вибирає страви, максимізуючи співвідношення калорій до вартості
    """
    # Сортуємо страви за калорії/вартість у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories']/x[1]['cost'], reverse=True)
    result = {}
    total_cost = 0

    for name, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            result[name] = 1
            total_cost += info['cost']
    return result


def dynamic_programming(items, budget):
    """
    Динамічне програмування: обчислює оптимальний набір страв для максимізації калорійності
    """
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0]*(budget+1) for _ in range(n+1)]

    for i in range(1, n+1):
        name, info = item_list[i-1]
        cost = info['cost']
        calories = info['calories']
        for b in range(budget+1):
            if cost <= b:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b-cost] + calories)
            else:
                dp[i][b] = dp[i-1][b]

    # Відновлення обраних страв
    res = {}
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i-1][b]:
            name, info = item_list[i-1]
            res[name] = 1
            b -= info['cost']
    return res