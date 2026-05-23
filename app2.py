import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime, timedelta
import time

st.set_page_config(page_title="Counseling Queue Simulation", layout="wide")

# ==============================
# LOGIN SYSTEM
# ==============================

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("Login Dashboard")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "12345":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Wrong username or password")

    st.stop()

# ==============================
# TIME FORMAT
# ==============================

START_TIME = datetime.strptime("08:00", "%H:%M")

def convert_to_clock(minutes):
    real_time = START_TIME + timedelta(minutes=int(minutes))
    return real_time.strftime("%H:%M")

# ==============================
# MODEL SIMULATION
# ==============================

class CounselingQueueSimulation:
    def __init__(self, dataset, cbt_power=0.5, counselors=1):
        self.dataset = dataset.copy()
        self.cbt_power = cbt_power
        self.counselors = counselors

    def apply_cbt(self, stress, resilience):
        reduction = resilience * self.cbt_power
        return max(0, round(stress - reduction, 2))

    def calculate_service_time(self, stress):
        base_time = 20
        stress_effect = stress * 35
        return round(base_time + stress_effect)

    def run(self):
        counselor_available_time = [0] * self.counselors

        arrival_minutes = []
        service_time = []
        service_begin_minutes = []
        service_end_minutes = []
        waiting_time = []
        counselor_idle_time = []
        counselor_used = []
        stress_after_cbt = []

        for i in range(len(self.dataset)):
            if i == 0:
                arrival = 0
            else:
                arrival = arrival_minutes[i - 1] + self.dataset.loc[i, "Interarrival Time"]

            duration = self.calculate_service_time(
                self.dataset.loc[i, "Stress Before CBT"]
            )

            selected_counselor = counselor_available_time.index(
                min(counselor_available_time)
            )

            begin = max(arrival, counselor_available_time[selected_counselor])
            end = begin + duration
            wait = begin - arrival
            idle = max(0, arrival - counselor_available_time[selected_counselor])

            counselor_available_time[selected_counselor] = end

            stress_after = self.apply_cbt(
                self.dataset.loc[i, "Stress Before CBT"],
                self.dataset.loc[i, "Resilience"]
            )

            arrival_minutes.append(arrival)
            service_time.append(duration)
            service_begin_minutes.append(begin)
            service_end_minutes.append(end)
            waiting_time.append(wait)
            counselor_idle_time.append(idle)
            counselor_used.append(selected_counselor + 1)
            stress_after_cbt.append(stress_after)

        self.dataset["Arrival Time"] = [convert_to_clock(x) for x in arrival_minutes]
        self.dataset["Service Begins"] = [convert_to_clock(x) for x in service_begin_minutes]
        self.dataset["Service Ends"] = [convert_to_clock(x) for x in service_end_minutes]

        self.dataset["Arrival Minutes"] = arrival_minutes
        self.dataset["Service Time"] = service_time
        self.dataset["Service Begin Minutes"] = service_begin_minutes
        self.dataset["Service End Minutes"] = service_end_minutes
        self.dataset["Waiting Time"] = waiting_time
        self.dataset["Counselor Idle Time"] = counselor_idle_time
        self.dataset["Counselor"] = counselor_used
        self.dataset["Stress After CBT"] = stress_after_cbt

        return self.dataset

# ==============================
# DATASET GENERATOR
# ==============================

def generate_dataset(total_students):
    return pd.DataFrame({
        "Student": range(1, total_students + 1),
        "Interarrival Time": np.random.randint(15, 75, total_students),
        "Stress Before CBT": np.round(np.random.uniform(0.50, 0.95, total_students), 2),
        "Resilience": np.round(np.random.uniform(0.20, 0.55, total_students), 2)
    })

# ==============================
# PDF EXPORT
# ==============================

def create_pdf(summary_df):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Counseling Queue Simulation Report", ln=True, align="C")

    pdf.ln(10)
    pdf.set_font("Arial", size=11)

    for _, row in summary_df.iterrows():
        pdf.cell(200, 8, txt=f"{row['Indicator']}: {row['Value']}", ln=True)

    return pdf.output(dest="S").encode("latin-1")

# ==============================
# SIDEBAR
# ==============================

st.sidebar.title("Simulation Settings")

total_students = st.sidebar.slider("Number of Students", 10, 200, 20)
cbt_power = st.sidebar.slider("CBT Power", 0.10, 1.00, 0.50)
counselors = st.sidebar.slider("Number of Counselors", 1, 10, 1)
monte_carlo_runs = st.sidebar.slider("Monte Carlo Runs", 10, 500, 100)

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

generate_button = st.sidebar.button("Generate Simulation")

# ==============================
# DASHBOARD
# ==============================

st.title("Counseling Queue Simulation Dashboard")
st.write(
    "Dynamic simulation model for student counseling queue "
    "with CBT-based stress reduction."
)

if generate_button or uploaded_file is not None:

    # ==============================
    # IMPORT CSV OR GENERATE DATASET
    # ==============================

    if uploaded_file is not None:
        dataset = pd.read_csv(uploaded_file)

        required_columns = [
            "Student",
            "Interarrival Time",
            "Stress Before CBT",
            "Resilience"
        ]

        missing_columns = [
            col for col in required_columns
            if col not in dataset.columns
        ]

        if missing_columns:
            st.error(f"Missing columns in CSV: {missing_columns}")
            st.stop()

        dataset = dataset[required_columns]
        st.success("CSV dataset imported successfully")

    else:
        dataset = generate_dataset(total_students)

    # ==============================
    # RUN SIMULATION
    # ==============================

    model = CounselingQueueSimulation(
        dataset=dataset,
        cbt_power=cbt_power,
        counselors=counselors
    )

    result = model.run()

    # ==============================
    # REALTIME QUEUE ANIMATION
    # ==============================

    st.subheader("Realtime Queue Animation")

    progress = st.progress(0)
    status_text = st.empty()

    for i in range(len(result)):
        progress.progress((i + 1) / len(result))
        status_text.write(
            f"Student {result.loc[i, 'Student']} processed by Counselor "
            f"{result.loc[i, 'Counselor']} from "
            f"{result.loc[i, 'Service Begins']} to "
            f"{result.loc[i, 'Service Ends']}"
        )
        time.sleep(0.03)

    st.success("Simulation completed")

    # ==============================
    # SUMMARY
    # ==============================

    avg_waiting = round(result["Waiting Time"].mean(), 2)
    avg_service = round(result["Service Time"].mean(), 2)
    avg_idle = round(result["Counselor Idle Time"].mean(), 2)
    probability_wait = round((result["Waiting Time"] > 0).mean(), 2)
    avg_stress_before = round(result["Stress Before CBT"].mean(), 2)
    avg_stress_after = round(result["Stress After CBT"].mean(), 2)
    avg_stress_reduction = round(avg_stress_before - avg_stress_after, 2)

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Waiting Time", f"{avg_waiting} minutes")
    col2.metric("Average Service Time", f"{avg_service} minutes")
    col3.metric("Probability of Waiting", probability_wait)

    col4, col5, col6 = st.columns(3)

    col4.metric("Stress Before CBT", avg_stress_before)
    col5.metric("Stress After CBT", avg_stress_after)
    col6.metric("Stress Reduction", avg_stress_reduction)

    summary_df = pd.DataFrame({
        "Indicator": [
            "Average Waiting Time",
            "Average Service Time",
            "Average Counselor Idle Time",
            "Probability of Waiting",
            "Average Stress Before CBT",
            "Average Stress After CBT",
            "Average Stress Reduction",
            "Number of Counselors"
        ],
        "Value": [
            avg_waiting,
            avg_service,
            avg_idle,
            probability_wait,
            avg_stress_before,
            avg_stress_after,
            avg_stress_reduction,
            counselors
        ]
    })

    display_columns = [
        "Student",
        "Interarrival Time",
        "Arrival Time",
        "Service Time",
        "Service Begins",
        "Service Ends",
        "Waiting Time",
        "Counselor Idle Time",
        "Counselor",
        "Stress Before CBT",
        "Stress After CBT",
        "Resilience"
    ]

    # ==============================
    # TABLES
    # ==============================

    st.subheader("Input Dataset")
    st.dataframe(dataset)

    st.subheader("Simulation Result")
    st.dataframe(result[display_columns])

    st.subheader("Simulation Summary")
    st.dataframe(summary_df)

    # ==============================
    # EXPORT CSV
    # ==============================

    csv_data = result[display_columns].to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Simulation Result as CSV",
        data=csv_data,
        file_name="counseling_simulation_result.csv",
        mime="text/csv"
    )

    # ==============================
    # EXPORT PDF
    # ==============================

    pdf_data = create_pdf(summary_df)

    st.download_button(
        label="Download Simulation Summary as PDF",
        data=pdf_data,
        file_name="counseling_simulation_report.pdf",
        mime="application/pdf"
    )

    # ==============================
    # VISUALIZATION 1
    # ==============================

    st.subheader("Stress Before and After CBT")

    fig1, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(
        result["Student"],
        result["Stress Before CBT"],
        marker="o",
        label="Before CBT"
    )

    ax1.plot(
        result["Student"],
        result["Stress After CBT"],
        marker="s",
        label="After CBT"
    )

    ax1.set_xlabel("Student")
    ax1.set_ylabel("Stress Level")
    ax1.set_ylim(0, 1)
    ax1.legend()
    ax1.grid(True)

    st.pyplot(fig1)

    # ==============================
    # VISUALIZATION 2
    # ==============================

    st.subheader("Waiting Time")

    fig2, ax2 = plt.subplots(figsize=(10, 5))

    ax2.bar(
        result["Student"],
        result["Waiting Time"]
    )

    ax2.set_xlabel("Student")
    ax2.set_ylabel("Waiting Time (Minutes)")
    ax2.grid(axis="y")

    st.pyplot(fig2)

    # ==============================
    # VISUALIZATION 3
    # ==============================

    st.subheader("Counselor Workload")

    workload = result.groupby("Counselor")["Service Time"].sum()

    fig3, ax3 = plt.subplots(figsize=(10, 5))

    ax3.bar(
        workload.index,
        workload.values
    )

    ax3.set_xlabel("Counselor")
    ax3.set_ylabel("Total Service Time")
    ax3.set_title("Counselor Workload")
    ax3.grid(axis="y")

    st.pyplot(fig3)

    # ==============================
    # MONTE CARLO SIMULATION
    # ==============================

    st.subheader("Monte Carlo Simulation")

    monte_carlo_results = []

    for _ in range(monte_carlo_runs):
        mc_dataset = generate_dataset(len(dataset))

        mc_model = CounselingQueueSimulation(
            dataset=mc_dataset,
            cbt_power=cbt_power,
            counselors=counselors
        )

        mc_result = mc_model.run()

        monte_carlo_results.append({
            "Average Waiting Time": mc_result["Waiting Time"].mean(),
            "Probability of Waiting": (mc_result["Waiting Time"] > 0).mean(),
            "Average Service Time": mc_result["Service Time"].mean()
        })

    mc_df = pd.DataFrame(monte_carlo_results)

    st.dataframe(mc_df.describe())

    fig4, ax4 = plt.subplots(figsize=(10, 5))

    ax4.hist(
        mc_df["Average Waiting Time"],
        bins=20
    )

    ax4.set_title("Monte Carlo Distribution of Average Waiting Time")
    ax4.set_xlabel("Average Waiting Time")
    ax4.set_ylabel("Frequency")

    st.pyplot(fig4)

    # ==============================
    # AI RECOMMENDATION
    # ==============================

    st.subheader("AI Recommendation for Counselor Load")

    if avg_waiting > 20 or probability_wait > 0.60:
        recommended_counselors = counselors + 1
        st.warning(
            f"The system is overloaded. "
            f"Recommended number of counselors: {recommended_counselors}"
        )

    elif avg_waiting < 5 and probability_wait < 0.30:
        st.success(
            "The current number of counselors is sufficient. "
            "The queue condition is stable."
        )

    else:
        st.info(
            "The system is moderately busy. "
            "Current counselor allocation is acceptable."
        )

else:
    st.info("Click 'Generate Simulation' or upload a CSV dataset from the sidebar.")