import numpy as np
import time
from matplotlib import pyplot as plt

def func_py(x: list[float], N: int) -> list[float]:
    """
    Calculate function values for passed array of arguments
    """
    return [1 - ((t - N/2) / (N/2))**2 if 0 <= t <= N else None for t in x]

def tabulate_py(N: int, n: int) -> tuple[list[float], list[float]]:
    x = [t for t in range(n+1)]
    y = func_py(x, N)
    return x, y

def tabulate_np(N: int, n: int) -> tuple[np.ndarray, np.ndarray]:
    x = np.linspace(0, N, n)
    y = 1 - ((x - N/2) / (N/2))**2
    return x, y

def test_tabulation(f, N, n):
    start_time = time.time()
    x, y = f(N, n)
    end_time = time.time()
    return end_time - start_time

def main():
    N = 11
    n = 1000
    
    # Заміряємо час виконання для звичайного Python та NumPy
    time_py = test_tabulation(tabulate_py, N, n)
    time_np = test_tabulation(tabulate_np, N, n)
    print("Час виконання для звичайного Python:", time_py)
    print("Час виконання для NumPy:", time_np)
    
    # Побудова графіку порівняння
    fig, ax = plt.subplots()
    ax.bar(['Python', 'NumPy'], [time_py, time_np])
    ax.set_ylabel('Час виконання (сек)')
    ax.set_title('Порівняння часу виконання для звичайного Python та NumPy')
    plt.show()

if __name__ == '__main__':
    main()
