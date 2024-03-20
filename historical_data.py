import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Завантаження даних з файлів CSV у масиви NumPy
tsla_data = pd.read_csv("TSLA Historical Data.csv")
nvda_data = pd.read_csv("NVDA Historical Data.csv")
amzn_data = pd.read_csv("AMZN Historical Data.csv")

# Витягуємо ціни закриття з кожного набору даних
tsla_prices = tsla_data["Price"].values
nvda_prices = nvda_data["Price"].values
amzn_prices = amzn_data["Price"].values

# Побудова графіків для кожного активу на окремому subplot
plt.figure(figsize=(12, 8))

# Графік для TSLA
plt.subplot(3, 1, 1)
plt.plot(tsla_prices, color='blue')
plt.title('Ціни TSLA')
plt.xlabel('Час')
plt.ylabel('Ціна')

# Графік для NVDA
plt.subplot(3, 1, 2)
plt.plot(nvda_prices, color='green')
plt.title('Ціни NVDA')
plt.xlabel('Час')
plt.ylabel('Ціна')

# Графік для AMZN
plt.subplot(3, 1, 3)
plt.plot(amzn_prices, color='red')
plt.title('Ціни AMZN')
plt.xlabel('Час')
plt.ylabel('Ціна')

# Відображення графіків
plt.tight_layout()
plt.show()
