import random
from collections import deque

import mesa
import matplotlib.pyplot as plt
import pandas as pd


class StudentAgent(mesa.Agent):
    """
    Agen mahasiswa.
    """

    def __init__(self, unique_id, model, arrival_time):
        super().__init__(unique_id, model)
        self.arrival_time = arrival_time
        self.urgency_level = random.choices([1, 2, 3], weights=[0.50, 0.35, 0.15])[0]
        self.waiting_time = 0
        self.patience_limit = random.randint(20, 45)
        self.service_time_needed = self.generate_service_time()
        self.status = "waiting"
        self.start_service_time = None
        self.end_service_time = None
        self.assigned_counselor_id = None

    def generate_service_time(self):
        if self.urgency_level == 1:
            return random.randint(10, 15)
        elif self.urgency_level == 2:
            return random.randint(15, 20)
        return random.randint(20, 30)

    def step(self):
        pass


class CounselorAgent(mesa.Agent):
    """
    Agen konselor.
    """

    def __init__(self, unique_id, model, counselor_id, service_speed_factor=1.0):
        super().__init__(unique_id, model)
        self.counselor_id = counselor_id
        self.service_speed_factor = service_speed_factor
        self.status = "idle"
        self.current_student = None
        self.remaining_service_time = 0
        self.students_served = 0
        self.busy_time = 0
        self.idle_time = 0

    def assign_student(self, student):
        adjusted_service_time = max(
            1,
            round(student.service_time_needed * self.service_speed_factor)
        )

        self.current_student = student
        self.remaining_service_time = adjusted_service_time
        self.status = "busy"

        student.status = "in_service"
        student.start_service_time = self.model.current_step
        student.assigned_counselor_id = self.counselor_id

        print(
            f"User-{student.unique_id} mulai dilayani oleh {self.counselor_id} "
            f"pada menit {self.model.format_time(student.start_service_time)} "
            f"(tunggu: {student.waiting_time:.2f})"
        )

    def release_student(self):
        student = self.current_student
        if student is None:
            return

        student.status = "done"
        student.end_service_time = self.model.current_step
        total_time_in_system = student.end_service_time - student.arrival_time

        print(
            f"User-{student.unique_id} selesai pada menit "
            f"{self.model.format_time(student.end_service_time)} "
            f"(total: {total_time_in_system:.2f})\n"
        )

        self.current_student = None
        self.remaining_service_time = 0
        self.status = "idle"
        self.students_served += 1

        self.model.total_served += 1
        self.model.completed_students.append(student)
        self.model.served_waiting_times.append(student.waiting_time)
        self.model.system_times.append(total_time_in_system)

    def step(self):
        if self.status == "busy":
            self.remaining_service_time -= 1
            self.busy_time += 1

            if self.remaining_service_time <= 0:
                self.release_student()
        else:
            self.idle_time += 1


class CounselingQueueModel(mesa.Model):
    """
    Model sistem antrian layanan konseling mahasiswa.
    """

    def __init__(
        self,
        num_counselors=2,
        max_steps=480,
        base_arrival_prob=0.35,
        queue_policy="FIFO",   # FIFO atau PRIORITY
        random_seed=42,
        use_decimal_log_time=True
    ):
        super().__init__()
        random.seed(random_seed)

        self.num_counselors = num_counselors
        self.max_steps = max_steps
        self.base_arrival_prob = base_arrival_prob
        self.queue_policy = queue_policy.upper()
        self.use_decimal_log_time = use_decimal_log_time

        self.current_step = 0
        self.running = True

        # Scheduler
        try:
            from mesa.time import BaseScheduler
            self.schedule = BaseScheduler(self)
        except Exception:
            self.schedule = mesa.time.BaseScheduler(self)

        # ID agen
        self.next_agent_id = 0

        # Antrian
        self.waiting_queue = deque()

        # Statistik utama
        self.total_arrivals = 0
        self.total_served = 0
        self.total_dropout = 0

        self.completed_students = []
        self.dropped_students = []
        self.served_waiting_times = []
        self.system_times = []
        self.queue_length_history = []
        self.all_students = []

        # Cache pseudo-decimal time supaya konsisten
        self.time_noise_cache = {}

        # Buat counselor
        self.counselors = []
        for idx in range(num_counselors):
            speed_factor = random.uniform(0.9, 1.1)
            counselor = CounselorAgent(
                unique_id=self.get_next_id(),
                model=self,
                counselor_id=f"K{idx+1}",
                service_speed_factor=speed_factor
            )
            self.counselors.append(counselor)
            self.schedule.add(counselor)

        self.datacollector = mesa.DataCollector(
            model_reporters={
                "step": lambda m: m.current_step,
                "queue_length": lambda m: len(m.waiting_queue),
                "total_arrivals": lambda m: m.total_arrivals,
                "total_served": lambda m: m.total_served,
                "total_dropout": lambda m: m.total_dropout,
                "avg_waiting_time": lambda m: m.get_average_waiting_time(),
                "avg_system_time": lambda m: m.get_average_system_time(),
                "avg_queue_length": lambda m: m.get_average_queue_length(),
                "utilization": lambda m: m.get_utilization(),
                "service_level": lambda m: m.get_service_level(),
                "dropout_rate": lambda m: m.get_dropout_rate(),
                "arrival_probability": lambda m: m.get_arrival_probability(),
            }
        )

    def get_next_id(self):
        self.next_agent_id += 1
        return self.next_agent_id

    def format_time(self, t):
        """
        Untuk menampilkan waktu seperti 6.49, 10.56, dst.
        Ini hanya mempercantik log, logika simulasi tetap diskrit.
        """
        if not self.use_decimal_log_time:
            return f"{float(t):.2f}"

        if t not in self.time_noise_cache:
            self.time_noise_cache[t] = random.uniform(0.01, 0.99)

        displayed_time = t + self.time_noise_cache[t]
        return f"{displayed_time:.2f}"

    def get_arrival_probability(self):
        """
        Pola jam sibuk sederhana.
        """
        if 120 <= self.current_step < 240:
            return min(1.0, self.base_arrival_prob + 0.10)
        if 240 <= self.current_step < 360:
            return min(1.0, self.base_arrival_prob + 0.05)
        return self.base_arrival_prob

    def generate_new_students(self):
        """
        Menghasilkan 0, 1, atau 2 mahasiswa per step.
        """
        arrival_prob = self.get_arrival_probability()

        num_new = 0
        if random.random() < arrival_prob:
            num_new += 1
        if random.random() < arrival_prob * 0.20:
            num_new += 1

        for _ in range(num_new):
            student = StudentAgent(
                unique_id=self.get_next_id(),
                model=self,
                arrival_time=self.current_step
            )
            self.total_arrivals += 1
            self.all_students.append(student)
            self.waiting_queue.append(student)
            self.schedule.add(student)

            print(
                f"User-{student.unique_id} datang pada menit "
                f"{self.format_time(student.arrival_time)}"
            )

    def sort_priority_queue(self):
        if self.queue_policy == "PRIORITY" and len(self.waiting_queue) > 1:
            sorted_students = sorted(
                list(self.waiting_queue),
                key=lambda s: (-s.urgency_level, s.arrival_time)
            )
            self.waiting_queue = deque(sorted_students)

    def assign_students_to_counselors(self):
        self.sort_priority_queue()

        for counselor in self.counselors:
            if counselor.status == "idle" and self.waiting_queue:
                next_student = self.waiting_queue.popleft()
                counselor.assign_student(next_student)

    def update_waiting_students(self):
        survivors = deque()

        while self.waiting_queue:
            student = self.waiting_queue.popleft()
            student.waiting_time += 1

            if student.waiting_time > student.patience_limit:
                student.status = "dropout"
                self.total_dropout += 1
                self.dropped_students.append(student)

                try:
                    self.schedule.remove(student)
                except Exception:
                    pass

                print(
                    f"User-{student.unique_id} keluar pada menit "
                    f"{self.format_time(self.current_step)} "
                    f"(menunggu terlalu lama: {student.waiting_time:.2f})"
                )
            else:
                survivors.append(student)

        self.waiting_queue = survivors

    def cleanup_finished_students(self):
        to_remove = []
        for agent in list(self.schedule.agents):
            if isinstance(agent, StudentAgent) and agent.status in {"done", "dropout"}:
                to_remove.append(agent)

        for agent in to_remove:
            try:
                self.schedule.remove(agent)
            except Exception:
                pass

    def step(self):
        if not self.running:
            return

        # 1. Mahasiswa datang
        self.generate_new_students()

        # 2. Assign awal
        self.assign_students_to_counselors()

        # 3. Step semua agen
        self.schedule.step()

        # 4. Update waiting queue
        self.update_waiting_students()

        # 5. Assign lagi jika ada counselor idle
        self.assign_students_to_counselors()

        # 6. Bersihkan agent selesai/dropout
        self.cleanup_finished_students()

        # 7. Simpan statistik
        self.queue_length_history.append(len(self.waiting_queue))
        self.datacollector.collect(self)

        self.current_step += 1

        if self.current_step >= self.max_steps:
            self.running = False

    def run_model(self):
        while self.running:
            self.step()

    def get_average_waiting_time(self):
        if not self.served_waiting_times:
            return 0.0
        return sum(self.served_waiting_times) / len(self.served_waiting_times)

    def get_average_system_time(self):
        if not self.system_times:
            return 0.0
        return sum(self.system_times) / len(self.system_times)

    def get_average_queue_length(self):
        if not self.queue_length_history:
            return 0.0
        return sum(self.queue_length_history) / len(self.queue_length_history)

    def get_utilization(self):
        total_busy = sum(c.busy_time for c in self.counselors)
        total_available = self.num_counselors * max(1, self.current_step)
        return total_busy / total_available

    def get_service_level(self):
        if self.total_arrivals == 0:
            return 0.0
        return self.total_served / self.total_arrivals

    def get_dropout_rate(self):
        if self.total_arrivals == 0:
            return 0.0
        return self.total_dropout / self.total_arrivals

    def get_summary(self):
        return {
            "Jumlah Konselor": self.num_counselors,
            "Kebijakan Antrian": self.queue_policy,
            "Total Mahasiswa Datang": self.total_arrivals,
            "Total Mahasiswa Terlayani": self.total_served,
            "Total Mahasiswa Dropout": self.total_dropout,
            "Rata-rata Waktu Tunggu": round(self.get_average_waiting_time(), 2),
            "Rata-rata Waktu dalam Sistem": round(self.get_average_system_time(), 2),
            "Rata-rata Panjang Antrian": round(self.get_average_queue_length(), 2),
            "Utilisasi Konselor": round(self.get_utilization(), 4),
            "Service Level": round(self.get_service_level(), 4),
            "Dropout Rate": round(self.get_dropout_rate(), 4),
        }

    def print_summary(self):
        summary = self.get_summary()

        print("\n===== HASIL SIMULASI =====")
        for key, value in summary.items():
            if key in {"Utilisasi Konselor", "Service Level", "Dropout Rate"}:
                print(f"{key:30s}: {value:.2%}")
            else:
                print(f"{key:30s}: {value}")

        print("\n===== KINERJA PER KONSELOR =====")
        for c in self.counselors:
            util = c.busy_time / max(1, self.current_step)
            print(
                f"{c.counselor_id} | served={c.students_served:3d} | "
                f"busy_time={c.busy_time:3d} | utilization={util:.2%}"
            )

    def results_dataframe(self):
        return self.datacollector.get_model_vars_dataframe()


def plot_results(df, title_suffix=""):
    plt.figure(figsize=(10, 5))
    plt.plot(df["step"], df["queue_length"])
    plt.title(f"Panjang Antrian per Waktu {title_suffix}")
    plt.xlabel("Step (menit)")
    plt.ylabel("Jumlah Mahasiswa dalam Antrian")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(df["step"], df["avg_waiting_time"])
    plt.title(f"Rata-rata Waktu Tunggu Kumulatif {title_suffix}")
    plt.xlabel("Step (menit)")
    plt.ylabel("Waktu Tunggu (menit)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(df["step"], df["utilization"])
    plt.title(f"Utilisasi Konselor {title_suffix}")
    plt.xlabel("Step (menit)")
    plt.ylabel("Utilisasi")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    model = CounselingQueueModel(
        num_counselors=2,
        max_steps=60,              # coba 480 kalau mau simulasi 8 jam
        base_arrival_prob=0.35,
        queue_policy="FIFO",       # ganti jadi "PRIORITY" kalau mau
        random_seed=42,
        use_decimal_log_time=True
    )

    model.run_model()
    model.print_summary()

    df_results = model.results_dataframe()

    print("\n5 baris terakhir hasil simulasi:")
    print(df_results.tail())

    # Simpan hasil ke CSV
    df_results.to_csv("hasil_simulasi_konseling.csv", index=False)

    # Plot grafik
    plot_results(df_results, title_suffix=f"({model.queue_policy})")