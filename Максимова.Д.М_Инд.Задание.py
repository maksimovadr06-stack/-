import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

numm_np = np.random.randint(-10000, 10001, size=1000)

Series = pd.DataFrame(numm_np, columns=["Values"])

Series = Series.dropna()

duplicate = Series["Values"].duplicated().sum()
min_num = Series["Values"].min()
maxx_num = Series["Values"].max()
summ = Series["Values"].sum()
sr_NUM = Series["Values"].mean()
variant = Series["Values"].var(ddof=1)
sr = math.sqrt(variant)

print(f"Минимальное значение: {min_num}")
print(f"Повторки: {duplicate}")
print(f"Максимальное значение: {maxx_num}")
print(f"Сумма всех чисел: {summ}")
print(f"Среднеквадратическое отклонение: {sr:.4f}")

with open("данные.txt", "w", encoding="utf-8") as dann:
    dann.write(f"Минимальное значение: {min_num}\n")
    dann.write(f"Повторки: {duplicate}\n")
    dann.write(f"Максимальное значение: {maxx_num}\n")
    dann.write(f"Сумма всех чисел: {summ}\n")
    dann.write(f"Среднеквадратическое отклонение: {sr:.4f}\n")

plt.rcParams['figure.facecolor'] = '#fcf0f8'
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.gcf().set_facecolor("#fcf0f8")
plt.gca().set_facecolor("#ecaedb")
plt.plot(Series["Values"], color="#80005b", alpha=1, linewidth=0.5)
plt.title("Линейный график")

rounded = [round(x / 100) * 100 for x in Series["Values"]]

plt.subplot(1, 2, 2)
plt.gca().set_facecolor('#ffd4f3')
plt.hist(rounded, bins=30, color="#f0a1fa", edgecolor='#621d6b', alpha=1)
plt.title("Гистограммa")

sorted_asc = Series["Values"].sort_values(ascending=True).values
sorted_desc = Series["Values"].sort_values(ascending=False).values
plt.figure(figsize=(10, 6))
plt.plot(sorted_asc, label='по возрастанию', color='#e100ff', linewidth=1)
plt.plot(sorted_desc, label='по убыванию', color='#ff0066', linewidth=1)
plt.title("Dataframe")
plt.legend(loc='best')
plt.grid(True, linestyle='-', alpha=0.6)

plt.tight_layout()
plt.show()