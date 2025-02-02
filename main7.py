import random
import matplotlib.pyplot as plt


def roll_dice(count_rolls):
    results = {i: 0 for i in range(2, 13)}
    for _ in range(count_rolls):
        dice_sum = random.randint(1, 6) + random.randint(1, 6)
        results[dice_sum] += 1
    return {key: value / count_rolls * 100 for key, value in results.items()}

theoretical_probabilities = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78}

count_rolls = 100000
probabilities = roll_dice(count_rolls)

plt.figure(figsize=(10, 6))
plt.bar(probabilities.keys(), probabilities.values(), width=0.4, label='Монте-Карло', alpha=0.7)
plt.bar(theoretical_probabilities.keys(), theoretical_probabilities.values(), width=0.4, label='Табличні', alpha=0.7)
plt.xlabel("Сума")
plt.ylabel("Ймовірність (%)")
plt.title(f"Ймовірності сум при {count_rolls} кидках")
plt.xticks(range(2, 13))
plt.legend()
plt.show()
