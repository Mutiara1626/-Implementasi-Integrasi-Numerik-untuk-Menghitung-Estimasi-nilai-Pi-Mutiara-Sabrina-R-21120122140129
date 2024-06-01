import numpy as np
import time
import matplotlib.pyplot as plt

# Definisikan fungsi f(x)
def f(x):
    return 4 / (1 + x**2)

# Implementasi metode Simpson 1/3
def simpson_1_3(a, b, N):
    if N % 2 != 0:
        raise ValueError("N harus genap.")
    h = (b - a) / N
    integral = f(a) + f(b)
    
    for i in range(1, N, 2):
        integral += 4 * f(a + i * h)
    
    for i in range(2, N, 2):
        integral += 2 * f(a + i * h)
    
    integral *= h / 3
    return integral

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Fungsi untuk menguji integrasi dengan berbagai nilai N
def test_integration(N_values):
    a = 0
    b = 1
    results = []

    for N in N_values:
        start_time = time.time()
        integral = simpson_1_3(a, b, N)
        end_time = time.time()
        
        # Hitung galat RMS
        error_rms = np.sqrt((integral - pi_ref)**2)
        # Ukur waktu eksekusi
        exec_time = end_time - start_time

        # Simpan hasil dalam list
        results.append((N, integral, error_rms, exec_time))
    
    return results

# Variasi nilai N yang akan diuji
N_values = [10, 100, 1000, 10000]

# Menjalankan pengujian
results = test_integration(N_values)

# Menampilkan hasil pengujian
for res in results:
    print(f"N = {res[0]:5}, Integral = {res[1]:.15f}, RMS Error = {res[2]:.15e}, Execution Time = {res[3]:.6f} seconds")

# Ekstrak data untuk grafik
N_values, integrals, errors, exec_times = zip(*results)

# Plot grafik
plt.figure(figsize=(18, 6))

# Plot galat RMS
plt.subplot(1, 3, 1)
plt.plot(N_values, errors, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('RMS Error')
plt.title('RMS Error vs N')
plt.grid(True)

# Plot waktu eksekusi
plt.subplot(1, 3, 2)
plt.plot(N_values, exec_times, marker='o')
plt.xscale('log')
plt.xlabel('N')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs N')
plt.grid(True)

# Plot hasil integral
plt.subplot(1, 3, 3)
plt.plot(N_values, integrals, marker='o')
plt.xscale('log')
plt.axhline(y=pi_ref, color='r', linestyle='--', label='Reference Pi')
plt.xlabel('N')
plt.ylabel('Integral Value')
plt.title('Integral Value vs N')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
