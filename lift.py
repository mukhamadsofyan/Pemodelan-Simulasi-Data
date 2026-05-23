import simpy
import random
import statistics

# =========================
# PARAMETER SIMULASI
# =========================
RANDOM_SEED = 42
JUMLAH_LIFT = 1                # bisa ubah jadi 2 untuk eksperimen
INTERVAL_KEDATANGAN = 5        # rata-rata waktu kedatangan (menit)
WAKTU_LAYANAN_MIN = 3          # waktu layanan minimum
WAKTU_LAYANAN_MAX = 6          # waktu layanan maksimum
SIMULASI_TIME = 100            # durasi simulasi

# =========================
# DATA PENYIMPANAN
# =========================
data_waktu_tunggu = []
data_waktu_layanan = []
data_total_waktu = []

# =========================
# PROSES PENGGUNA
# =========================
def pengguna(env, nama, lift):
    waktu_datang = env.now
    print(f"{nama} datang pada menit {waktu_datang:.2f}")
    
    with lift.request() as request:
        yield request
        
        waktu_mulai = env.now
        waktu_tunggu = waktu_mulai - waktu_datang
        data_waktu_tunggu.append(waktu_tunggu)
        
        print(f"{nama} mulai naik lift pada menit {waktu_mulai:.2f} (tunggu: {waktu_tunggu:.2f})")
        
        # waktu pelayanan random
        waktu_layanan = random.uniform(WAKTU_LAYANAN_MIN, WAKTU_LAYANAN_MAX)
        data_waktu_layanan.append(waktu_layanan)
        
        yield env.timeout(waktu_layanan)
        
        waktu_selesai = env.now
        total = waktu_selesai - waktu_datang
        data_total_waktu.append(total)
        
        print(f"{nama} selesai pada menit {waktu_selesai:.2f} (total: {total:.2f})\n")

# =========================
# GENERATOR PENGGUNA
# =========================
def generator_pengguna(env, lift):
    i = 0
    while True:
        waktu_antar = random.expovariate(1.0 / INTERVAL_KEDATANGAN)
        yield env.timeout(waktu_antar)
        
        i += 1
        env.process(pengguna(env, f"User-{i}", lift))

# =========================
# SIMULASI UTAMA
# =========================
def run_simulasi():
    print("=== SIMULASI DIMULAI ===\n")
    
    random.seed(RANDOM_SEED)
    env = simpy.Environment()
    lift = simpy.Resource(env, capacity=JUMLAH_LIFT)
    
    env.process(generator_pengguna(env, lift))
    env.run(until=SIMULASI_TIME)
    
    print("\n=== SIMULASI SELESAI ===\n")
    
    # =========================
    # STATISTIK HASIL
    # =========================
    print("Jumlah pengguna:", len(data_waktu_tunggu))
    
    print("\n--- WAKTU TUNGGU ---")
    print("Rata-rata:", statistics.mean(data_waktu_tunggu))
    print("Maksimum:", max(data_waktu_tunggu))
    print("Minimum:", min(data_waktu_tunggu))
    
    print("\n--- WAKTU LAYANAN ---")
    print("Rata-rata:", statistics.mean(data_waktu_layanan))
    
    print("\n--- TOTAL WAKTU DALAM SISTEM ---")
    print("Rata-rata:", statistics.mean(data_total_waktu))
    
    # estimasi utilisasi
    total_busy = sum(data_waktu_layanan)
    utilisasi = total_busy / (SIMULASI_TIME * JUMLAH_LIFT)
    
    print("\n--- UTILISASI LIFT ---")
    print("Utilisasi:", utilisasi)

# =========================
# JALANKAN
# =========================
run_simulasi()