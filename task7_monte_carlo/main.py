from monte_carlo import simulate_dice_rolls
import matplotlib.pyplot as plt

probabilities = simulate_dice_rolls(100000)

print("Ймовірності сум при киданні двох кубиків методом Монте-Карло:")
for s, p in sorted(probabilities.items()):
    print(f"{s}: {p:.4%}")

# Побудова графіка
sums = list(probabilities.keys())
probs = list(probabilities.values())

plt.bar(sums, probs, color='skyblue')
plt.xlabel("Сума кубиків")
plt.ylabel("Ймовірність")
plt.title("Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)")
plt.xticks(sums)
plt.grid(axis='y')
plt.show()