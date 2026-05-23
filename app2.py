import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
from fpdf import FPDF
from datetime import datetime, timedelta
import time
import io

# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="CounselingQ · Simulation",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# GLOBAL CSS — Premium dark theme
# ==============================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;600&display=swap');

:root {
    --bg:      #0d0f14;
    --surface: #13161e;
    --panel:   #181c27;
    --border:  #252a38;
    --accent:  #4f9cf9;
    --accent2: #a78bfa;
    --success: #34d399;
    --warning: #fbbf24;
    --danger:  #f87171;
    --text:    #e8eaf0;
    --muted:   #6b7280;
    --serif:   'DM Serif Display', Georgia, serif;
    --sans:    'DM Sans', sans-serif;
    --mono:    'JetBrains Mono', monospace;
}

.stApp { background: var(--bg); font-family: var(--sans); color: var(--text); }

[data-testid="stSidebar"] { background: var(--surface) !important; border-right: 1px solid var(--border); }
[data-testid="stSidebar"] * { color: var(--text) !important; }
[data-testid="stSidebar"] .stSlider > div > div > div { background: var(--accent) !important; }
[data-testid="stSidebar"] .stSlider > div > div { background: var(--border) !important; }

h1, h2, h3 { font-family: var(--serif) !important; letter-spacing: -0.02em; color: var(--text) !important; }

.hero-block { padding: 2.5rem 0 1.5rem; border-bottom: 1px solid var(--border); margin-bottom: 2rem; }
.hero-block h1 {
    font-family: var(--serif) !important;
    font-size: 3rem !important;
    background: linear-gradient(135deg, #e8eaf0 0%, #4f9cf9 60%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 0.25rem !important;
    line-height: 1.1;
}
.hero-block p { color: var(--muted); font-size: 1.05rem; margin: 0; font-weight: 300; }

.metric-card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.3rem 1.5rem;
    text-align: center;
    transition: border-color .2s, transform .15s;
    position: relative; overflow: hidden;
}
.metric-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; }
.metric-card.blue::before   { background: linear-gradient(90deg, #4f9cf9, #93c5fd); }
.metric-card.purple::before { background: linear-gradient(90deg, #a78bfa, #c4b5fd); }
.metric-card.green::before  { background: linear-gradient(90deg, #34d399, #6ee7b7); }
.metric-card.yellow::before { background: linear-gradient(90deg, #fbbf24, #fde68a); }
.metric-card.red::before    { background: linear-gradient(90deg, #f87171, #fca5a5); }
.metric-card:hover { border-color: var(--accent); transform: translateY(-2px); }
.metric-label { font-size: 0.73rem; font-weight: 600; text-transform: uppercase; letter-spacing: .1em; color: var(--muted); margin-bottom: .5rem; }
.metric-value { font-family: var(--mono); font-size: 2rem; font-weight: 600; color: var(--text); line-height: 1; }
.metric-sub   { font-size: 0.75rem; color: var(--muted); margin-top: .4rem; }

.section-header { display: flex; align-items: center; gap: .75rem; margin: 2rem 0 1rem; padding-bottom: .75rem; border-bottom: 1px solid var(--border); }
.section-header .icon { width: 36px; height: 36px; background: linear-gradient(135deg, #4f9cf9, #a78bfa); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1rem; }
.section-header h2 { font-family: var(--serif) !important; font-size: 1.5rem !important; margin: 0 !important; }

.badge { display: inline-block; padding: .2rem .65rem; border-radius: 20px; font-size: .73rem; font-weight: 600; letter-spacing: .05em; text-transform: uppercase; }
.badge-success { background: rgba(52,211,153,.15); color: #34d399; border: 1px solid rgba(52,211,153,.3); }

.ai-box { border-radius: 14px; padding: 1.4rem 1.6rem; display: flex; align-items: flex-start; gap: 1rem; margin-top: 1rem; }
.ai-box.warning { background: rgba(251,191,36,.08);  border: 1px solid rgba(251,191,36,.3); }
.ai-box.success { background: rgba(52,211,153,.08); border: 1px solid rgba(52,211,153,.3); }
.ai-box.info    { background: rgba(79,156,249,.08);  border: 1px solid rgba(79,156,249,.3); }
.ai-icon { font-size: 1.7rem; line-height: 1; }
.ai-text p { margin: 0; font-size: .95rem; line-height: 1.6; }
.ai-text strong { display: block; margin-bottom: .3rem; font-size: 1rem; }

.stProgress > div > div { background: linear-gradient(90deg, #4f9cf9, #a78bfa) !important; border-radius: 4px !important; }
.stProgress > div { background: #252a38 !important; border-radius: 4px !important; }

.stDataFrame { background: var(--panel) !important; border-radius: 12px !important; border: 1px solid var(--border) !important; }
.stDataFrame thead th { background: var(--surface) !important; color: var(--accent) !important; font-family: var(--mono) !important; font-size: .78rem !important; }
.stDataFrame tbody td { font-family: var(--mono) !important; font-size: .8rem !important; }

.stButton > button, .stDownloadButton > button {
    background: linear-gradient(135deg, #4f9cf9, #a78bfa) !important;
    color: #fff !important; border: none !important; border-radius: 10px !important;
    font-weight: 600 !important; padding: .55rem 1.4rem !important;
    font-family: var(--sans) !important; letter-spacing: .02em;
    transition: opacity .2s, transform .15s !important;
}
.stButton > button:hover, .stDownloadButton > button:hover { opacity: .88 !important; transform: translateY(-1px) !important; }

input[type="text"], input[type="password"] {
    background: var(--surface) !important; color: var(--text) !important;
    border: 1px solid var(--border) !important; border-radius: 8px !important;
}

.sidebar-logo { font-family: var(--serif); font-size: 1.4rem; color: var(--text);
    padding: .5rem 0 1rem; border-bottom: 1px solid var(--border); margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

# ==============================
# MATPLOTLIB DARK THEME
# ==============================

BG      = "#0d0f14"
SURFACE = "#181c27"
BORDER  = "#252a38"
ACCENT  = "#4f9cf9"
ACCENT2 = "#a78bfa"
SUCCESS = "#34d399"
WARNING = "#fbbf24"
DANGER  = "#f87171"
MUTED   = "#6b7280"
TEXT    = "#e8eaf0"

def apply_dark_style(ax, fig):
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(BG)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.xaxis.label.set_color(MUTED)
    ax.yaxis.label.set_color(MUTED)
    ax.title.set_color(TEXT)
    for spine in ax.spines.values():
        spine.set_edgecolor(BORDER)
    ax.grid(color=BORDER, linewidth=0.6)

def styled_fig(ncols=1, nrows=1, figsize=(10, 4)):
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    fig.patch.set_facecolor(SURFACE)
    if isinstance(axes, np.ndarray):
        for ax in axes.flat:
            apply_dark_style(ax, fig)
    else:
        apply_dark_style(axes, fig)
    fig.tight_layout(pad=2.0)
    return fig, axes

# ==============================
# TIME FORMAT
# ==============================

START_TIME = datetime.strptime("08:00", "%H:%M")

def convert_to_clock(minutes):
    real_time = START_TIME + timedelta(minutes=int(minutes))
    return real_time.strftime("%H:%M")

# ==============================
# SIMULATION MODEL
# ==============================

class CounselingQueueSimulation:
    def __init__(self, dataset, cbt_power=0.5, counselors=1):
        self.dataset   = dataset.copy().reset_index(drop=True)
        self.cbt_power = cbt_power
        self.counselors = counselors

    def apply_cbt(self, stress, resilience):
        return max(0.0, round(stress - resilience * self.cbt_power, 4))

    def calculate_service_time(self, stress):
        return round(20 + stress * 35)

    def run(self):
        n = len(self.dataset)
        counselor_available = [0.0] * self.counselors

        arrival_mins = np.zeros(n)
        svc_time     = np.zeros(n, dtype=int)
        svc_begin    = np.zeros(n)
        svc_end      = np.zeros(n)
        wait_time    = np.zeros(n)
        idle_time    = np.zeros(n)
        c_used       = np.zeros(n, dtype=int)
        stress_after = np.zeros(n)

        for i in range(n):
            arrival = 0.0 if i == 0 else arrival_mins[i-1] + self.dataset.loc[i, "Interarrival Time"]
            duration = self.calculate_service_time(self.dataset.loc[i, "Stress Before CBT"])
            sel   = int(np.argmin(counselor_available))
            begin = max(arrival, counselor_available[sel])
            end   = begin + duration

            counselor_available[sel] = end
            arrival_mins[i]  = arrival
            svc_time[i]      = duration
            svc_begin[i]     = begin
            svc_end[i]       = end
            wait_time[i]     = begin - arrival
            idle_time[i]     = max(0.0, arrival - (counselor_available[sel] - duration))
            c_used[i]        = sel + 1
            stress_after[i]  = self.apply_cbt(
                self.dataset.loc[i, "Stress Before CBT"],
                self.dataset.loc[i, "Resilience"]
            )

        out = self.dataset.copy()
        out["Arrival Time"]          = [convert_to_clock(x) for x in arrival_mins]
        out["Service Begins"]        = [convert_to_clock(x) for x in svc_begin]
        out["Service Ends"]          = [convert_to_clock(x) for x in svc_end]
        out["Arrival Minutes"]       = arrival_mins
        out["Service Time"]          = svc_time
        out["Service Begin Minutes"] = svc_begin
        out["Service End Minutes"]   = svc_end
        out["Waiting Time"]          = wait_time
        out["Counselor Idle Time"]   = idle_time
        out["Counselor"]             = c_used
        out["Stress After CBT"]      = stress_after
        return out

# ==============================
# DATASET GENERATOR
# ==============================

def generate_dataset(n):
    rng = np.random.default_rng()
    return pd.DataFrame({
        "Student":           range(1, n + 1),
        "Interarrival Time": rng.integers(10, 60, n).astype(int),
        "Stress Before CBT": np.round(rng.uniform(0.40, 0.95, n), 3),
        "Resilience":        np.round(rng.uniform(0.15, 0.60, n), 3),
    })

# ==============================
# PDF EXPORT
# ==============================

def create_pdf(summary_df, avg_waiting, counselors, probability_wait):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "B", 20)
    pdf.set_text_color(50, 100, 200)
    pdf.cell(0, 14, "CounselingQ Simulation Report", ln=True, align="C")

    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(107, 114, 128)
    pdf.cell(0, 8, f"Generated: {datetime.now().strftime('%A, %d %B %Y  %H:%M')}", ln=True, align="C")
    pdf.ln(8)

    pdf.set_font("Arial", "B", 13)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 10, "Simulation Summary", ln=True)
    pdf.ln(2)

    for _, row in summary_df.iterrows():
        pdf.set_font("Arial", "B", 10)
        pdf.set_text_color(90, 90, 90)
        pdf.cell(100, 8, str(row["Indicator"]) + ":")
        pdf.set_font("Arial", "", 10)
        pdf.set_text_color(30, 30, 30)
        pdf.cell(0, 8, str(row["Value"]), ln=True)

    pdf.ln(8)
    pdf.set_font("Arial", "B", 13)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 10, "AI Recommendation", ln=True)
    pdf.ln(2)
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(90, 90, 90)

    if avg_waiting > 20 or probability_wait > 0.60:
        msg = (f"System overloaded. Avg wait = {avg_waiting} min, P(wait) = {probability_wait:.1%}. "
               f"Recommended: increase counselors to {counselors + 1}.")
    elif avg_waiting < 5 and probability_wait < 0.30:
        msg = (f"System efficient. Avg wait = {avg_waiting} min, P(wait) = {probability_wait:.1%}. "
               f"Current staffing of {counselors} counselor(s) is well-calibrated.")
    else:
        msg = (f"System moderately busy. Avg wait = {avg_waiting} min, P(wait) = {probability_wait:.1%}. "
               "Monitor during peak periods.")

    pdf.multi_cell(0, 7, msg)

    try:
        return pdf.output(dest="S").encode("latin-1")
    except Exception:
        buf = io.BytesIO()
        pdf.output(buf)
        return buf.getvalue()

# ==============================
# UI HELPERS
# ==============================

def metric_card(label, value, sub="", color="blue"):
    return f"""
    <div class="metric-card {color}">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        {"<div class='metric-sub'>" + sub + "</div>" if sub else ""}
    </div>"""

def section_header(icon, title):
    st.markdown(f"""
    <div class="section-header">
        <div class="icon">{icon}</div>
        <h2>{title}</h2>
    </div>""", unsafe_allow_html=True)

# ==============================
# LOGIN
# ==============================

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown("""
    <div style="text-align:center;padding:3rem 0 1rem;">
        <div style="font-family:'DM Serif Display',serif;font-size:2.8rem;
             background:linear-gradient(135deg,#e8eaf0,#4f9cf9,#a78bfa);
             -webkit-background-clip:text;-webkit-text-fill-color:transparent;
             background-clip:text;line-height:1.1;">CounselingQ</div>
        <div style="color:#6b7280;font-size:1rem;margin-top:.4rem;">Queue Simulation &amp; CBT Analytics</div>
    </div>""", unsafe_allow_html=True)

    _, col_c, _ = st.columns([1, 1.1, 1])
    with col_c:
        st.markdown("""
        <div style="background:#181c27;border:1px solid #252a38;border-radius:20px;padding:2.5rem;">
        <h2 style="text-align:center;margin-bottom:1.5rem;">Sign In</h2>
        </div>""", unsafe_allow_html=True)
        username = st.text_input("Username", placeholder="admin")
        password = st.text_input("Password", type="password", placeholder="••••••")
        if st.button("Sign In →", use_container_width=True):
            if username == "admin" and password == "12345":
                st.session_state.login = True
                st.rerun()
            else:
                st.error("Invalid credentials. Try  admin / 12345")
        st.markdown('<div style="color:#6b7280;font-size:.78rem;text-align:center;margin-top:1rem;">Demo: admin / 12345</div>', unsafe_allow_html=True)
    st.stop()

# ==============================
# SIDEBAR
# ==============================

with st.sidebar:
    st.markdown('<div class="sidebar-logo">🧠 CounselingQ</div>', unsafe_allow_html=True)
    st.markdown("**Simulation Parameters**")
    total_students   = st.slider("Number of Students",  10, 2000,  50, step=10)
    cbt_power        = st.slider("CBT Effectiveness", 0.10, 1.00, 0.50, step=0.05)
    counselors       = st.slider("Counselors",           1,   20,    1)
    monte_carlo_runs = st.slider("Monte Carlo Runs",    10,  500,  100, step=10)
    st.divider()
    st.markdown("**Upload Dataset**")
    uploaded_file = st.file_uploader("CSV file", type=["csv"],
        help="Columns: Student, Interarrival Time, Stress Before CBT, Resilience")
    st.divider()
    generate_button = st.button("▶  Run Simulation", use_container_width=True)
    if st.button("🔓 Sign Out", use_container_width=True):
        st.session_state.login = False
        st.rerun()

# ==============================
# HERO
# ==============================

st.markdown("""
<div class="hero-block">
    <h1>Counseling Queue Simulation</h1>
    <p>Discrete-event simulation with CBT-based stress reduction &amp; Monte Carlo analysis</p>
</div>""", unsafe_allow_html=True)

# ==============================
# MAIN FLOW
# ==============================

if generate_button or uploaded_file is not None:

    # ── Dataset ──────────────────────────────────────────────────────────────
    if uploaded_file is not None:
        dataset = pd.read_csv(uploaded_file)
        required = ["Student", "Interarrival Time", "Stress Before CBT", "Resilience"]
        missing  = [c for c in required if c not in dataset.columns]
        if missing:
            st.error(f"Missing columns in CSV: {missing}")
            st.stop()
        dataset = dataset[required].reset_index(drop=True)
        st.success(f"✅  CSV imported — {len(dataset):,} students loaded")
    else:
        with st.spinner("Generating dataset…"):
            dataset = generate_dataset(total_students)

    n_students = len(dataset)

    # ── Run simulation ────────────────────────────────────────────────────────
    section_header("⚙️", "Running Simulation")

    progress_bar = st.progress(0)
    status       = st.empty()

    model  = CounselingQueueSimulation(dataset, cbt_power=cbt_power, counselors=counselors)
    result = model.run()

    batch = max(1, n_students // 80)
    for i in range(0, n_students, batch):
        idx = min(i, n_students - 1)
        progress_bar.progress((idx + 1) / n_students)
        if n_students <= 300 or i % (batch * 10) == 0:
            status.markdown(
                f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:.82rem;color:#6b7280;">'
                f'Processing {idx+1:,}/{n_students:,} · '
                f'Counselor {result.loc[idx,"Counselor"]} · '
                f'{result.loc[idx,"Service Begins"]} → {result.loc[idx,"Service Ends"]}'
                f'</span>', unsafe_allow_html=True)
        if n_students <= 300:
            time.sleep(0.01)

    progress_bar.progress(1.0)
    status.markdown(
        f'<span class="badge badge-success">✓ Complete — {n_students:,} students processed</span>',
        unsafe_allow_html=True)

    # ── Metrics ───────────────────────────────────────────────────────────────
    avg_waiting       = round(result["Waiting Time"].mean(), 2)
    avg_service       = round(result["Service Time"].mean(), 2)
    avg_idle          = round(result["Counselor Idle Time"].mean(), 2)
    probability_wait  = round((result["Waiting Time"] > 0).mean(), 4)
    avg_stress_before = round(result["Stress Before CBT"].mean(), 4)
    avg_stress_after  = round(result["Stress After CBT"].mean(), 4)
    avg_stress_red    = round(avg_stress_before - avg_stress_after, 4)
    max_waiting       = int(result["Waiting Time"].max())

    section_header("📊", "Key Performance Indicators")

    r1 = st.columns(4)
    with r1[0]: st.markdown(metric_card("Avg Wait Time",    f"{avg_waiting}",         "minutes",             "blue"),   unsafe_allow_html=True)
    with r1[1]: st.markdown(metric_card("Avg Service Time", f"{avg_service}",         "minutes",             "purple"), unsafe_allow_html=True)
    with r1[2]: st.markdown(metric_card("P(Waiting)",       f"{probability_wait:.1%}","of students wait",    "yellow"), unsafe_allow_html=True)
    with r1[3]: st.markdown(metric_card("Max Wait",         f"{max_waiting}",         "minutes",             "red"),    unsafe_allow_html=True)

    st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)

    r2 = st.columns(4)
    with r2[0]: st.markdown(metric_card("Stress Before CBT", f"{avg_stress_before:.3f}", "avg level",          "red"),   unsafe_allow_html=True)
    with r2[1]: st.markdown(metric_card("Stress After CBT",  f"{avg_stress_after:.3f}",  "avg level",          "green"), unsafe_allow_html=True)
    with r2[2]: st.markdown(metric_card("Stress Reduction",  f"{avg_stress_red:.3f}",    f"CBT × {cbt_power}", "green"), unsafe_allow_html=True)
    with r2[3]: st.markdown(metric_card("Counselors",        f"{counselors}",            "active",             "blue"),  unsafe_allow_html=True)

    summary_df = pd.DataFrame({
        "Indicator": [
            "Number of Students", "Number of Counselors",
            "Avg Waiting Time (min)", "Max Waiting Time (min)",
            "Avg Service Time (min)", "Avg Counselor Idle Time (min)",
            "Probability of Waiting", "Avg Stress Before CBT",
            "Avg Stress After CBT",  "Avg Stress Reduction", "CBT Power",
        ],
        "Value": [
            n_students, counselors,
            avg_waiting, max_waiting,
            avg_service, avg_idle,
            f"{probability_wait:.2%}", avg_stress_before,
            avg_stress_after, avg_stress_red, cbt_power,
        ]
    })

    # ── Visualizations (Matplotlib) ───────────────────────────────────────────
    section_header("📈", "Visualizations")

    students = result["Student"].values

    # Row 1
    vc1, vc2 = st.columns(2)

    with vc1:
        fig, ax = styled_fig(figsize=(7, 3.8))
        ax.plot(students, result["Stress Before CBT"], color=DANGER,  lw=1.8, label="Before CBT")
        ax.fill_between(students, result["Stress Before CBT"], alpha=0.10, color=DANGER)
        ax.plot(students, result["Stress After CBT"],  color=SUCCESS, lw=1.8, label="After CBT")
        ax.fill_between(students, result["Stress After CBT"],  alpha=0.10, color=SUCCESS)
        ax.set_ylim(0, 1.05)
        ax.set_xlabel("Student"); ax.set_ylabel("Stress Level")
        ax.set_title("Stress Level Before & After CBT", fontsize=11, pad=10)
        legend = ax.legend(facecolor=SURFACE, edgecolor=BORDER, labelcolor=TEXT, fontsize=9)
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    with vc2:
        # Downsample for large datasets in bar chart
        if n_students > 300:
            sample_idx = np.linspace(0, n_students-1, 300, dtype=int)
            s_x = students[sample_idx]
            s_y = result["Waiting Time"].values[sample_idx]
            note = f"(showing 300/{n_students:,} sampled)"
        else:
            s_x, s_y = students, result["Waiting Time"].values
            note = ""

        cmap = LinearSegmentedColormap.from_list("wt", [ACCENT, ACCENT2, DANGER])
        norm_vals = s_y / (s_y.max() + 1e-9)
        colors = [cmap(v) for v in norm_vals]

        fig, ax = styled_fig(figsize=(7, 3.8))
        ax.bar(s_x, s_y, color=colors, width=max(1, n_students // 300 * 0.9))
        ax.set_xlabel("Student"); ax.set_ylabel("Waiting Time (min)")
        ax.set_title(f"Waiting Time per Student {note}", fontsize=11, pad=10)
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    # Row 2
    vc3, vc4 = st.columns(2)

    with vc3:
        wl = result.groupby("Counselor")["Service Time"].sum()
        cmap2 = LinearSegmentedColormap.from_list("wl", [ACCENT, ACCENT2])
        bar_colors = [cmap2(i / max(1, len(wl)-1)) for i in range(len(wl))]
        fig, ax = styled_fig(figsize=(7, 3.8))
        bars = ax.bar([str(c) for c in wl.index], wl.values, color=bar_colors)
        for bar, val in zip(bars, wl.values):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + wl.values.max()*0.01,
                    f"{val:,}", ha="center", va="bottom", fontsize=8, color=MUTED)
        ax.set_xlabel("Counselor ID"); ax.set_ylabel("Total Service Time (min)")
        ax.set_title("Counselor Workload", fontsize=11, pad=10)
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    with vc4:
        reduction = (result["Stress Before CBT"] - result["Stress After CBT"]).values
        fig, ax = styled_fig(figsize=(7, 3.8))
        ax.hist(reduction, bins=30, color=SUCCESS, alpha=0.75, edgecolor=BG, linewidth=0.4)
        ax.axvline(reduction.mean(), color=WARNING, lw=1.5, linestyle="--",
                   label=f"Mean: {reduction.mean():.3f}")
        ax.set_xlabel("Stress Reduction"); ax.set_ylabel("Frequency")
        ax.set_title("Stress Reduction Distribution", fontsize=11, pad=10)
        legend = ax.legend(facecolor=SURFACE, edgecolor=BORDER, labelcolor=TEXT, fontsize=9)
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    # ── Tables ────────────────────────────────────────────────────────────────
    section_header("📋", "Data Tables")

    DISPLAY_COLS = [
        "Student", "Interarrival Time", "Arrival Time", "Service Time",
        "Service Begins", "Service Ends", "Waiting Time",
        "Counselor Idle Time", "Counselor",
        "Stress Before CBT", "Stress After CBT", "Resilience"
    ]

    tab1, tab2, tab3 = st.tabs(["📥 Input Dataset", "📤 Simulation Result", "📑 Summary"])
    with tab1: st.dataframe(dataset, use_container_width=True, height=380)
    with tab2: st.dataframe(result[DISPLAY_COLS], use_container_width=True, height=380)
    with tab3: st.dataframe(summary_df, use_container_width=True)

    # ── Export ────────────────────────────────────────────────────────────────
    section_header("💾", "Export")

    ec1, ec2 = st.columns(2)
    csv_data = result[DISPLAY_COLS].to_csv(index=False).encode("utf-8")
    with ec1:
        st.download_button("⬇  Download Result CSV", data=csv_data,
            file_name=f"counseling_simulation_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv", use_container_width=True)

    pdf_data = create_pdf(summary_df, avg_waiting, counselors, probability_wait)
    with ec2:
        st.download_button("⬇  Download Summary PDF", data=pdf_data,
            file_name=f"counseling_report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
            mime="application/pdf", use_container_width=True)

    # ── Monte Carlo ───────────────────────────────────────────────────────────
    section_header("🎲", "Monte Carlo Analysis")

    mc_n = min(n_students, 200)
    with st.spinner(f"Running {monte_carlo_runs} Monte Carlo iterations…"):
        mc_results = []
        for _ in range(monte_carlo_runs):
            mc_ds  = generate_dataset(mc_n)
            mc_res = CounselingQueueSimulation(mc_ds, cbt_power=cbt_power, counselors=counselors).run()
            mc_results.append({
                "Avg Wait (min)":       round(mc_res["Waiting Time"].mean(), 2),
                "P(Waiting)":           round((mc_res["Waiting Time"] > 0).mean(), 4),
                "Avg Service (min)":    round(mc_res["Service Time"].mean(), 2),
                "Avg Stress Reduction": round((mc_res["Stress Before CBT"] - mc_res["Stress After CBT"]).mean(), 4),
            })

    mc_df = pd.DataFrame(mc_results)

    if n_students > 200:
        st.info(f"ℹ️  Monte Carlo uses {mc_n} students/iteration (capped for speed). "
                f"Main simulation ran {n_students:,} students.")

    mc1, mc2 = st.columns(2)

    with mc1:
        st.markdown("**Descriptive Statistics**")
        st.dataframe(mc_df.describe().round(3), use_container_width=True)

    with mc2:
        wait_vals = mc_df["Avg Wait (min)"].values
        fig, ax = styled_fig(figsize=(7, 3.8))
        ax.hist(wait_vals, bins=25, color=ACCENT, alpha=0.8, edgecolor=BG, linewidth=0.4)
        ax.axvline(wait_vals.mean(), color=WARNING, lw=1.8, linestyle="--",
                   label=f"Mean: {wait_vals.mean():.2f} min")
        ax.set_xlabel("Average Waiting Time (min)"); ax.set_ylabel("Frequency")
        ax.set_title("Monte Carlo: Distribution of Avg Waiting Time", fontsize=11, pad=10)
        legend = ax.legend(facecolor=SURFACE, edgecolor=BORDER, labelcolor=TEXT, fontsize=9)
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    # Scatter: service vs wait
    fig, ax = styled_fig(figsize=(10, 4))
    sc = ax.scatter(mc_df["Avg Service (min)"], mc_df["Avg Wait (min)"],
                    c=mc_df["P(Waiting)"], cmap=LinearSegmentedColormap.from_list("pw", [SUCCESS, ACCENT, DANGER]),
                    alpha=0.7, s=40, edgecolors="none")
    cbar = fig.colorbar(sc, ax=ax)
    cbar.ax.yaxis.set_tick_params(color=MUTED, labelcolor=MUTED)
    cbar.set_label("P(Waiting)", color=MUTED, fontsize=9)
    ax.set_xlabel("Avg Service Time (min)"); ax.set_ylabel("Avg Wait Time (min)")
    ax.set_title("Monte Carlo: Service Time vs. Wait Time", fontsize=11, pad=10)
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    # ── AI Recommendation ─────────────────────────────────────────────────────
    section_header("🤖", "AI Recommendation")

    if avg_waiting > 20 or probability_wait > 0.60:
        sc, icon, ttl = "warning", "⚠️", "System Overloaded"
        body = (f"Average waiting time is <strong>{avg_waiting} min</strong> and "
                f"{probability_wait:.1%} of students must wait. "
                f"Consider increasing counselors to <strong>{counselors + 1}</strong>.")
    elif avg_waiting < 5 and probability_wait < 0.30:
        sc, icon, ttl = "success", "✅", "System Efficient"
        body = (f"Excellent performance — only {probability_wait:.1%} of students wait, "
                f"avg <strong>{avg_waiting} min</strong>. "
                f"Current <strong>{counselors}</strong> counselor(s) is well-calibrated.")
    else:
        sc, icon, ttl = "info", "ℹ️", "System Moderately Busy"
        body = (f"Moderate load — avg wait <strong>{avg_waiting} min</strong>, "
                f"P(wait) = {probability_wait:.1%}. Monitor during peak periods.")

    st.markdown(f"""
    <div class="ai-box {sc}">
        <div class="ai-icon">{icon}</div>
        <div class="ai-text"><strong>{ttl}</strong><p>{body}</p></div>
    </div>""", unsafe_allow_html=True)
    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)

else:
    st.markdown("""
    <div style="text-align:center;padding:5rem 2rem;color:#6b7280;">
        <div style="font-size:3rem;margin-bottom:1rem;">🧠</div>
        <div style="font-family:'DM Serif Display',serif;font-size:1.8rem;color:#e8eaf0;margin-bottom:.75rem;">Ready to Simulate</div>
        <div style="font-size:1rem;max-width:500px;margin:0 auto;line-height:1.7;">
            Configure parameters in the sidebar, then click
            <strong style="color:#4f9cf9;">▶ Run Simulation</strong> or upload a CSV dataset.
        </div>
        <div style="margin-top:2.5rem;display:flex;justify-content:center;gap:2rem;flex-wrap:wrap;">
            <div style="background:#181c27;border:1px solid #252a38;border-radius:12px;padding:1.2rem 1.8rem;min-width:160px;">
                <div style="font-size:1.5rem;">👥</div>
                <div style="font-size:.8rem;margin-top:.4rem;text-transform:uppercase;letter-spacing:.08em;color:#4f9cf9;">Up to 2,000 students</div>
            </div>
            <div style="background:#181c27;border:1px solid #252a38;border-radius:12px;padding:1.2rem 1.8rem;min-width:160px;">
                <div style="font-size:1.5rem;">🎲</div>
                <div style="font-size:.8rem;margin-top:.4rem;text-transform:uppercase;letter-spacing:.08em;color:#a78bfa;">Monte Carlo analysis</div>
            </div>
            <div style="background:#181c27;border:1px solid #252a38;border-radius:12px;padding:1.2rem 1.8rem;min-width:160px;">
                <div style="font-size:1.5rem;">🧘</div>
                <div style="font-size:.8rem;margin-top:.4rem;text-transform:uppercase;letter-spacing:.08em;color:#34d399;">CBT stress reduction</div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)