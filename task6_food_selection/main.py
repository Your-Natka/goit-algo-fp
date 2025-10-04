from food_selection import greedy_algorithm, dynamic_programming

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

print("Жадібний алгоритм:")
greedy_result = greedy_algorithm(items, budget)
print(greedy_result)

print("\nДинамічне програмування:")
dp_result = dynamic_programming(items, budget)
print(dp_result)