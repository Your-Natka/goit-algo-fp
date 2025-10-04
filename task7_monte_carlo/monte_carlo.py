import random
from collections import Counter

def simulate_dice_rolls(num_rolls=100000):
    """
    Симуляція кидків двох кубиків методом Монте-Карло
    """
    sums = []
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sums.append(dice1 + dice2)
    count = Counter(sums)
    
    # Обчислюємо ймовірності
    probabilities = {s: count[s]/num_rolls for s in range(2, 13)}
    return probabilities