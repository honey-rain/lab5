import numpy as np
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

def test_tabulation(f, N, n, axis):
    x, y = f(N, n)
    axis.plot(x, y)
    axis.grid()

def main():
    N = 11
    n = 1000
    fig, (ax1, ax2) = plt.subplots(2, 1)
    test_tabulation(tabulate_py, N, n, ax1)
    test_tabulation(tabulate_np, N, n, ax2)
    plt.show()

if __name__ == '__main__':
    main()
