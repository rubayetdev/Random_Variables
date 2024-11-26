import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Binomial Distribution Parameters
n = 10  # Number of trials
p_values = [0.2, 0.5, 0.8]  # Varying probability of success
k = np.arange(0, n + 1)  # Possible outcomes

# Plotting
plt.figure(figsize=(8, 6))
for p in p_values:
    plt.stem(k, binom.pmf(k, n, p), label=f"$n={n}$, $p={p}$", basefmt=" ", linefmt="-", markerfmt="o")

plt.title("Binomial Distribution")
plt.xlabel("k")
plt.ylabel("PMF")
plt.legend()
plt.grid(True)
plt.show()
