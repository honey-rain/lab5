import numpy as np

def f(x, N):
    return 1 - ((x - N/2) / (N/2))**2

def main():
    N_values = np.arange(0, 12)  # Значення N від 0 до 11
    x_values = np.linspace(0, 11, 100)  # Від 0 до 11 з кроком 0.01

    for N in N_values:
        y_values = f(x_values, N)
        print(f"N = {N}:")
        print("x\t|\tf(x)")
        print("-------------------")
        for x, y in zip(x_values, y_values):
            print(f"{x:.2f}\t|\t{y:.4f}")
        print("\n")

if __name__ == "__main__":
    main()
