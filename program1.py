import simpy
import random
import numpy as np
import matplotlib.pyplot as plt

# ==============================
# FUNGSI SIMULASI
# ==============================
def run_simulation(name, num_servers, arrival_rate, service_rate, sim_time, seed=42):
    print(f"\n===== SKENARIO: {name} =====")

    random.seed(seed)

    waiting_times = []
    service_times = []
    server_busy_time = 0

    def customer(env, name, server):
        nonlocal server_busy_time
        arrival_time = env.now

        print(f"{name} datang pada menit {arrival_time:.2f}")

        with server.request() as request:
            yield request

            wait = env.now - arrival_time
            waiting_times.append(wait)

            print(f"{name} mulai dilayani pada menit {env.now:.2f} (tunggu: {wait:.2f})")

            service_time = random.expovariate(service_rate)
            service_times.append(service_time)
            server_busy_time += service_time

            yield env.timeout(service_time)

            total_time = env.now - arrival_time
            print(f"{name} selesai pada menit {env.now:.2f} (total: {total_time:.2f})\n")

    def arrival_process(env, server):
        i = 0
        while True:
            interarrival = random.expovariate(arrival_rate)
            yield env.timeout(interarrival)
            i += 1
            env.process(customer(env, f"User-{i}", server))

    # Setup
    env = simpy.Environment()
    server = simpy.Resource(env, capacity=num_servers)

    env.process(arrival_process(env, server))
    env.run(until=sim_time)

    # Statistik
    avg_wait = np.mean(waiting_times) if waiting_times else 0
    avg_service = np.mean(service_times) if service_times else 0
    utilization = server_busy_time / (sim_time * num_servers)

    print("=== HASIL ===")
    print(f"Rata-rata waktu tunggu : {avg_wait:.2f} menit")
    print(f"Rata-rata waktu layanan: {avg_service:.2f} menit")
    print(f"Utilisasi server       : {utilization:.2f}")

    return avg_wait, avg_service, utilization


# ==============================
# PARAMETER
# ==============================
SIM_TIME = 100

# ==============================
# Menjalankan 2 SKENARIO
# ==============================
normal = run_simulation("Normal", 2, 1/5, 1/4, SIM_TIME)
ramai = run_simulation("Ramai", 2, 1/3, 1/4, SIM_TIME)

# ==============================
# GRAFIK PERBANDINGAN
# ==============================
labels = ["Normal", "Ramai"]

waiting = [normal[0], ramai[0]]
util = [normal[2], ramai[2]]

# Grafik waktu tunggu
plt.figure()
plt.bar(labels, waiting)
plt.title("Perbandingan Waktu Tunggu (Normal vs Ramai)")
plt.xlabel("Skenario")
plt.ylabel("Rata-rata Waktu Tunggu (menit)")
plt.show()

# Grafik utilisasi
plt.figure()
plt.bar(labels, util)
plt.title("Perbandingan Utilisasi Server (Normal vs Ramai)")
plt.xlabel("Skenario")
plt.ylabel("Utilisasi")
plt.show()