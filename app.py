import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class CounselingQueueSimulation:
    def __init__(self, dataset, cbt_power=0.50):
        self.dataset = dataset.copy()
        self.cbt_power = cbt_power

    def apply_cbt(self, stress_level, resilience):
        reduction = resilience * self.cbt_power
        return max(0, round(stress_level - reduction, 2))

    def calculate_service_time(self, stress_level):
        base_time = 20
        stress_effect = stress_level * 35
        return round(base_time + stress_effect)

    def run(self):
        arrival_time = []
        service_time = []
        service_begins = []
        service_ends = []
        waiting_time = []
        idle_time = []
        stress_after_cbt = []

        for i in range(len(self.dataset)):
            if i == 0:
                arrival = 0
            else:
                arrival = arrival_time[i - 1] + self.dataset.loc[i, "Interarrival Time"]

            duration = self.calculate_service_time(self.dataset.loc[i, "Stress Before CBT"])

            if i == 0:
                begin = arrival
                idle = 0
            else:
                begin = max(arrival, service_ends[i - 1])
                idle = max(0, arrival - service_ends[i - 1])

            end = begin + duration
            wait = begin - arrival

            stress_after = self.apply_cbt(
                self.dataset.loc[i, "Stress Before CBT"],
                self.dataset.loc[i, "Resilience"]
            )

            arrival_time.append(arrival)
            service_time.append(duration)
            service_begins.append(begin)
            service_ends.append(end)
            waiting_time.append(wait)
            idle_time.append(idle)
            stress_after_cbt.append(stress_after)

        self.dataset["Arrival Time"] = arrival_time
        self.dataset["Service Time"] = service_time
        self.dataset["Service Begins"] = service_begins
        self.dataset["Service Ends"] = service_ends
        self.dataset["Waiting Time"] = waiting_time
        self.dataset["Counselor Idle Time"] = idle_time
        self.dataset["Stress After CBT"] = stress_after_cbt

        return self.dataset


def generate_dataset(total_students):
    return pd.DataFrame({
        "Student": range(1, total_students + 1),
        "Interarrival Time": np.random.randint(15, 75, total_students),
        "Stress Before CBT": np.round(np.random.uniform(0.50, 0.95, total_students), 2),
        "Resilience": np.round(np.random.uniform(0.20, 0.55, total_students), 2)
    })


st.title("Counseling Queue Simulation Dashboard")
st.write("Simulation of student counseling queue with CBT-based stress reduction.")

st.sidebar.header("Simulation Settings")

total_students = st.sidebar.slider("Number of Students", 10, 100, 20)
cbt_power = st.sidebar.slider("CBT Power", 0.10, 1.00, 0.50)
generate_button = st.sidebar.button("Generate Dataset")

if generate_button:
    dataset = generate_dataset(total_students)

    model = CounselingQueueSimulation(dataset, cbt_power)
    result = model.run()

    st.subheader("Generated Dataset")
    st.dataframe(dataset)

    st.subheader("Simulation Result")
    st.dataframe(result)

    st.subheader("Simulation Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Average Waiting Time",
        f"{round(result['Waiting Time'].mean(), 2)} minutes"
    )

    col2.metric(
        "Average Service Time",
        f"{round(result['Service Time'].mean(), 2)} minutes"
    )

    col3.metric(
        "Probability of Waiting",
        round((result["Waiting Time"] > 0).mean(), 2)
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Average Stress Before CBT",
        round(result["Stress Before CBT"].mean(), 2)
    )

    col5.metric(
        "Average Stress After CBT",
        round(result["Stress After CBT"].mean(), 2)
    )

    col6.metric(
        "Average Idle Time",
        f"{round(result['Counselor Idle Time'].mean(), 2)} minutes"
    )

    st.subheader("Stress Before and After CBT")

    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(result["Student"], result["Stress Before CBT"], marker="o", label="Before CBT")
    ax1.plot(result["Student"], result["Stress After CBT"], marker="s", label="After CBT")
    ax1.set_xlabel("Student")
    ax1.set_ylabel("Stress Level")
    ax1.set_ylim(0, 1)
    ax1.legend()
    ax1.grid(True)
    st.pyplot(fig1)

    st.subheader("Waiting Time")

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.bar(result["Student"], result["Waiting Time"])
    ax2.set_xlabel("Student")
    ax2.set_ylabel("Waiting Time (Minutes)")
    ax2.grid(axis="y")
    st.pyplot(fig2)

    st.subheader("Service Time Based on Stress Level")

    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.plot(result["Student"], result["Service Time"], marker="o")
    ax3.set_xlabel("Student")
    ax3.set_ylabel("Service Time (Minutes)")
    ax3.grid(True)
    st.pyplot(fig3)

else:
    st.info("Click 'Generate Dataset' to start the simulation.")