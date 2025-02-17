import matplotlib.pyplot as plt

# Thread counts
threads = [1, 2, 3, 4, 5, 6, 7, 8, 16]

# Execution times (Replace with your actual times)
execution_times = [543.08, 274.839, 261.011, 181.381, 178.170, 141.543, 143.910, 136.779, 131.324] 

# Compute speedup
speedup = [execution_times[0] / t for t in execution_times]

# Plot graph
plt.figure(figsize=(8,6))
plt.plot(threads, speedup, marker='o', linestyle='-', label='Measured Speedup')
plt.plot(threads, threads, linestyle='--', color='gray', label='Ideal Speedup')

plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.title("Speedup vs. Number of Threads")
plt.legend()
plt.grid()
plt.show()
