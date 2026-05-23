import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
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

/* ── Root palette ── */
:root {
    --bg:        #0d0f14;
    --surface:   #13161e;
    --panel:     #181c27;
    --border:    #252a38;
    --accent:    #4f9cf9;
    --accent2:   #a78bfa;
    --success:   #34d399;
    --warning:   #fbbf24;
    --danger:    #f87171;
    --text:      #e8eaf0;
    --muted:     #6b7280;
    --serif:     'DM Serif Display', Georgia, serif;
    --sans:      'DM Sans', sans-serif;
    --mono:      'JetBrains Mono', monospace;
}

/* ── App background ── */
.stApp {
    background: var(--bg);
    font-family: var(--sans);
    color: var(--text);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] * { color: var(--text) !important; }
[data-testid="stSidebar"] .stSlider > div > div > div { background: var(--accent) !important; }
[data-testid="stSidebar"] .stSlider > div > div { background: var(--border) !important; }

/* ── Headings ── */
h1, h2, h3 { font-family: var(--serif) !important; letter-spacing: -0.02em; color: var(--text) !important; }

/* Main title block */
.hero-block {
    padding: 2.5rem 0 1.5rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 2rem;
}
.hero-block h1 {
    font-family: var(--serif) !important;
    font-size: 3rem !important;
    background: linear-gradient(135deg, #e8eaf0 0%, var(--accent) 60%, var(--accent2) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 0.25rem !important;
    line-height: 1.1;
}
.hero-block p {
    color: var(--muted);
    font-size: 1.05rem;
    margin: 0;
    font-weight: 300;
}

/* ── Metric cards ── */
.metric-card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.3rem 1.5rem;
    text-align: center;
    transition: border-color .2s, transform .15s;
    position: relative;
    overflow: hidden;
}
.metric-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
}
.metric-card.blue::before  { background: linear-gradient(90deg, var(--accent), #93c5fd); }
.metric-card.purple::before{ background: linear-gradient(90deg, var(--accent2), #c4b5fd); }
.metric-card.green::before { background: linear-gradient(90deg, var(--success), #6ee7b7); }
.metric-card.yellow::before{ background: linear-gradient(90deg, var(--warning), #fde68a); }
.metric-card.red::before   { background: linear-gradient(90deg, var(--danger), #fca5a5); }
.metric-card:hover { border-color: var(--accent); transform: translateY(-2px); }
.metric-label {
    font-size: 0.73rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: .1em;
    color: var(--muted);
    margin-bottom: .5rem;
}
.metric-value {
    font-family: var(--mono);
    font-size: 2rem;
    font-weight: 600;
    color: var(--text);
    line-height: 1;
}
.metric-sub {
    font-size: 0.75rem;
    color: var(--muted);
    margin-top: .4rem;
}

/* ── Section headers ── */
.section-header {
    display: flex;
    align-items: center;
    gap: .75rem;
    margin: 2rem 0 1rem;
    padding-bottom: .75rem;
    border-bottom: 1px solid var(--border);
}
.section-header .icon {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem;
}
.section-header h2 {
    font-family: var(--serif) !important;
    font-size: 1.5rem !important;
    margin: 0 !important;
}

/* ── Status badges ── */
.badge {
    display: inline-block;
    padding: .2rem .65rem;
    border-radius: 20px;
    font-size: .73rem;
    font-weight: 600;
    letter-spacing: .05em;
    text-transform: uppercase;
}
.badge-success { background: rgba(52,211,153,.15); color: var(--success); border: 1px solid rgba(52,211,153,.3); }
.badge-warning { background: rgba(251,191,36,.15); color: var(--warning); border: 1px solid rgba(251,191,36,.3); }
.badge-danger  { background: rgba(248,113,113,.15); color: var(--danger);  border: 1px solid rgba(248,113,113,.3); }
.badge-info    { background: rgba(79,156,249,.15);  color: var(--accent);  border: 1px solid rgba(79,156,249,.3); }

/* ── AI Recommendation box ── */
.ai-box {
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    margin-top: 1rem;
}
.ai-box.warning { background: rgba(251,191,36,.08); border: 1px solid rgba(251,191,36,.3); }
.ai-box.success { background: rgba(52,211,153,.08); border: 1px solid rgba(52,211,153,.3); }
.ai-box.info    { background: rgba(79,156,249,.08);  border: 1px solid rgba(79,156,249,.3); }
.ai-icon { font-size: 1.7rem; line-height: 1; }
.ai-text p { margin: 0; font-size: .95rem; line-height: 1.6; }
.ai-text strong { display: block; margin-bottom: .3rem; font-size: 1rem; }

/* ── Progress bar ── */
.stProgress > div > div { background: linear-gradient(90deg, var(--accent), var(--accent2)) !important; border-radius: 4px !important; }
.stProgress > div { background: var(--border) !important; border-radius: 4px !important; }

/* ── DataFrames ── */
.stDataFrame { background: var(--panel) !important; border-radius: 12px !important; border: 1px solid var(--border) !important; }
.stDataFrame thead th { background: var(--surface) !important; color: var(--accent) !important; font-family: var(--mono) !important; font-size: .78rem !important; }
.stDataFrame tbody td { font-family: var(--mono) !important; font-size: .8rem !important; }

/* ── Buttons ── */
.stButton > button, .stDownloadButton > button {
    background: linear-gradient(135deg, var(--accent), var(--accent2)) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: .55rem 1.4rem !important;
    font-family: var(--sans) !important;
    transition: opacity .2s, transform .15s !important;
    letter-spacing: .02em;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    opacity: .88 !important;
    transform: translateY(-1px) !important;
}

/* ── Login card ── */
.login-wrap {
    max-width: 420px;
    margin: 5rem auto 0;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 2.5rem;
}
.login-wrap h2 { text-align: center; margin-bottom: 1.5rem !important; }

/* Input overrides */
input[type="text"], input[type="password"] {
    background: var(--surface) !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
}
input[type="text"]:focus, input[type="password"]:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(79,156,249,.2) !important;
}

/* Alert overrides */
.stAlert { border-radius: 10px !important; }

/* Plotly charts */
.js-plotly-plot { border-radius: 12px !important; }

/* Sidebar title */
.sidebar-logo {
    font-family: var(--serif);
    font-size: 1.4rem;
    color: var(--text);
    padding: .5rem 0 1rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: .5rem;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# CHART THEME (Plotly)
# ==============================

CHART_THEME = dict(
    plot_bgcolor="rgba(19,22,30,0)",
    paper_bgcolor="rgba(19,22,30,0)",
    font=dict(family="DM Sans, sans-serif", color="#9ca3af", size=12),
    xaxis=dict(gridcolor="#252a38", linecolor="#252a38", zerolinecolor="#252a38"),
    yaxis=dict(gridcolor="#252a38", linecolor="#252a38", zerolinecolor="#252a38"),
    margin=dict(l=50, r=30, t=50, b=50),
)

ACCENT   = "#4f9cf9"
ACCENT2  = "#a78bfa"
SUCCESS  = "#34d399"
WARNING  = "#fbbf24"
DANGER   = "#f87171"

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
        self.dataset = dataset.copy().reset_index(drop=True)
        self.cbt_power = cbt_power
        self.counselors = counselors

    def apply_cbt(self, stress, resilience):
        reduction = resilience * self.cbt_power
        return max(0.0, round(stress - reduction, 4))

    def calculate_service_time(self, stress):
        base_time = 20
        stress_effect = stress * 35
        return round(base_time + stress_effect)

    def run(self):
        n = len(self.dataset)
        counselor_available = [0] * self.counselors

        arrival_mins    = np.zeros(n, dtype=float)
        svc_time        = np.zeros(n, dtype=int)
        svc_begin       = np.zeros(n, dtype=float)
        svc_end         = np.zeros(n, dtype=float)
        wait_time       = np.zeros(n, dtype=float)
        idle_time       = np.zeros(n, dtype=float)
        c_used          = np.zeros(n, dtype=int)
        stress_after    = np.zeros(n, dtype=float)

        for i in range(n):
            arrival = (0 if i == 0
                       else arrival_mins[i-1] + self.dataset.loc[i, "Interarrival Time"])

            duration = self.calculate_service_time(self.dataset.loc[i, "Stress Before CBT"])

            sel = int(np.argmin(counselor_available))
            begin = max(arrival, counselor_available[sel])
            end   = begin + duration
            wait  = begin - arrival
            idle  = max(0.0, arrival - counselor_available[sel])

            counselor_available[sel] = end

            arrival_mins[i]  = arrival
            svc_time[i]      = duration
            svc_begin[i]     = begin
            svc_end[i]       = end
            wait_time[i]     = wait
            idle_time[i]     = idle
            c_used[i]        = sel + 1
            stress_after[i]  = self.apply_cbt(
                self.dataset.loc[i, "Stress Before CBT"],
                self.dataset.loc[i, "Resilience"]
            )

        out = self.dataset.copy()
        out["Arrival Time"]        = [convert_to_clock(x) for x in arrival_mins]
        out["Service Begins"]      = [convert_to_clock(x) for x in svc_begin]
        out["Service Ends"]        = [convert_to_clock(x) for x in svc_end]
        out["Arrival Minutes"]     = arrival_mins
        out["Service Time"]        = svc_time
        out["Service Begin Minutes"] = svc_begin
        out["Service End Minutes"] = svc_end
        out["Waiting Time"]        = wait_time
        out["Counselor Idle Time"] = idle_time
        out["Counselor"]           = c_used
        out["Stress After CBT"]    = stress_after

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

    # Header
    pdf.set_fill_color(13, 15, 20)
    pdf.set_text_color(79, 156, 249)
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 14, "CounselingQ Simulation Report", ln=True, align="C")

    pdf.set_text_color(107, 114, 128)
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 8, f"Generated on {datetime.now().strftime('%A, %d %B %Y  %H:%M')}", ln=True, align="C")
    pdf.ln(6)

    pdf.set_draw_color(37, 42, 56)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(8)

    # Summary table
    pdf.set_font("Arial", "B", 13)
    pdf.set_text_color(232, 234, 240)
    pdf.cell(0, 10, "Simulation Summary", ln=True)
    pdf.ln(2)

    for _, row in summary_df.iterrows():
        pdf.set_font("Arial", "B", 10)
        pdf.set_text_color(107, 114, 128)
        pdf.cell(95, 8, str(row["Indicator"]) + ":")
        pdf.set_font("Arial", "", 10)
        pdf.set_text_color(232, 234, 240)
        pdf.cell(0, 8, str(row["Value"]), ln=True)

    pdf.ln(8)

    # Recommendation
    pdf.set_font("Arial", "B", 13)
    pdf.set_text_color(232, 234, 240)
    pdf.cell(0, 10, "AI Recommendation", ln=True)
    pdf.ln(2)
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(107, 114, 128)

    if avg_waiting > 20 or probability_wait > 0.60:
        msg = (f"System overloaded. Recommended counselors: {counselors + 1}. "
               "Consider adding staff to reduce waiting time and improve student experience.")
    elif avg_waiting < 5 and probability_wait < 0.30:
        msg = ("System is running efficiently. Current counselor count is sufficient. "
               "Queue condition is stable and students experience minimal wait time.")
    else:
        msg = ("System is moderately busy. Current allocation is acceptable, "
               "but monitoring is advised during peak hours.")

    pdf.multi_cell(0, 7, msg)

    try:
        return pdf.output(dest="S").encode("latin-1")
    except Exception:
        buf = io.BytesIO()
        pdf.output(buf)
        return buf.getvalue()

# ==============================
# HELPER: render metric card
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
# LOGIN SYSTEM
# ==============================

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown("""
    <div style="text-align:center; padding: 3rem 0 1rem;">
        <div style="font-family:'DM Serif Display',serif; font-size:2.8rem;
             background:linear-gradient(135deg,#e8eaf0,#4f9cf9,#a78bfa);
             -webkit-background-clip:text; -webkit-text-fill-color:transparent;
             background-clip:text; line-height:1.1;">
            CounselingQ
        </div>
        <div style="color:#6b7280; font-size:1rem; margin-top:.4rem;">
            Queue Simulation &amp; CBT Analytics
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_l, col_c, col_r = st.columns([1, 1.1, 1])
    with col_c:
        st.markdown('<div class="login-wrap">', unsafe_allow_html=True)
        st.markdown('<h2>Sign In</h2>', unsafe_allow_html=True)
        username = st.text_input("Username", placeholder="admin")
        password = st.text_input("Password", type="password", placeholder="••••••")
        if st.button("Sign In →", use_container_width=True):
            if username == "admin" and password == "12345":
                st.session_state.login = True
                st.rerun()
            else:
                st.error("Invalid credentials. Try admin / 12345")
        st.markdown('<div style="color:#6b7280;font-size:.78rem;text-align:center;margin-top:1rem;">Demo: admin / 12345</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ==============================
# SIDEBAR
# ==============================

with st.sidebar:
    st.markdown('<div class="sidebar-logo">🧠 CounselingQ</div>', unsafe_allow_html=True)

    st.markdown("**Simulation Parameters**")
    total_students    = st.slider("Number of Students",   10, 2000, 50, step=10)
    cbt_power         = st.slider("CBT Effectiveness",  0.10, 1.00, 0.50, step=0.05)
    counselors        = st.slider("Counselors",            1,   20,    1)
    monte_carlo_runs  = st.slider("Monte Carlo Runs",     10,  500,  100, step=10)

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
# HERO HEADER
# ==============================

st.markdown("""
<div class="hero-block">
    <h1>Counseling Queue Simulation</h1>
    <p>Dynamic discrete-event model with CBT-based stress reduction &amp; Monte Carlo analysis</p>
</div>
""", unsafe_allow_html=True)

# ==============================
# MAIN FLOW
# ==============================

if generate_button or uploaded_file is not None:

    # ── Load / generate dataset ──────────────────────────────────────────────
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

    # ── Run simulation ───────────────────────────────────────────────────────
    section_header("⚙️", "Running Simulation")

    progress_bar = st.progress(0)
    status       = st.empty()

    model  = CounselingQueueSimulation(dataset, cbt_power=cbt_power, counselors=counselors)
    result = model.run()

    # Animate progress (batch for large datasets)
    batch = max(1, n_students // 80)
    for i in range(0, n_students, batch):
        idx = min(i, n_students - 1)
        progress_bar.progress((idx + 1) / n_students)
        if n_students <= 200 or i % (batch * 10) == 0:
            status.markdown(
                f'<span style="font-family:var(--mono);font-size:.82rem;color:#6b7280;">'
                f'Processing student {idx+1:,}/{n_students:,} · '
                f'Counselor {result.loc[idx,"Counselor"]} · '
                f'{result.loc[idx,"Service Begins"]} → {result.loc[idx,"Service Ends"]}'
                f'</span>', unsafe_allow_html=True)
        if n_students <= 200:
            time.sleep(0.01)

    progress_bar.progress(1.0)
    status.markdown(
        f'<span class="badge badge-success">✓ Simulation complete — {n_students:,} students processed</span>',
        unsafe_allow_html=True)

    # ── Compute summary metrics ──────────────────────────────────────────────
    avg_waiting        = round(result["Waiting Time"].mean(), 2)
    avg_service        = round(result["Service Time"].mean(), 2)
    avg_idle           = round(result["Counselor Idle Time"].mean(), 2)
    probability_wait   = round((result["Waiting Time"] > 0).mean(), 4)
    avg_stress_before  = round(result["Stress Before CBT"].mean(), 4)
    avg_stress_after   = round(result["Stress After CBT"].mean(), 4)
    avg_stress_red     = round(avg_stress_before - avg_stress_after, 4)
    max_waiting        = int(result["Waiting Time"].max())
    util_pct           = round((1 - result["Counselor Idle Time"].sum() /
                                max(1, result["Service End Minutes"].max() * counselors)) * 100, 1)

    # ── Metric cards ─────────────────────────────────────────────────────────
    section_header("📊", "Key Performance Indicators")

    r1c1, r1c2, r1c3, r1c4 = st.columns(4)
    with r1c1: st.markdown(metric_card("Avg Wait Time",     f"{avg_waiting}",   "minutes",        "blue"),   unsafe_allow_html=True)
    with r1c2: st.markdown(metric_card("Avg Service Time",  f"{avg_service}",   "minutes",        "purple"), unsafe_allow_html=True)
    with r1c3: st.markdown(metric_card("P(Waiting)",        f"{probability_wait:.1%}", "of students wait", "yellow"), unsafe_allow_html=True)
    with r1c4: st.markdown(metric_card("Max Wait",          f"{max_waiting}",   "minutes",        "red"),    unsafe_allow_html=True)

    st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)

    r2c1, r2c2, r2c3, r2c4 = st.columns(4)
    with r2c1: st.markdown(metric_card("Stress Before CBT", f"{avg_stress_before:.3f}", "avg level",   "red"),    unsafe_allow_html=True)
    with r2c2: st.markdown(metric_card("Stress After CBT",  f"{avg_stress_after:.3f}",  "avg level",   "green"),  unsafe_allow_html=True)
    with r2c3: st.markdown(metric_card("Stress Reduction",  f"{avg_stress_red:.3f}",    f"CBT power {cbt_power}", "green"), unsafe_allow_html=True)
    with r2c4: st.markdown(metric_card("Counselors",        f"{counselors}",    "active",          "blue"),   unsafe_allow_html=True)

    # ── Summary DataFrame ─────────────────────────────────────────────────────
    summary_df = pd.DataFrame({
        "Indicator": [
            "Number of Students", "Number of Counselors",
            "Average Waiting Time (min)", "Max Waiting Time (min)",
            "Average Service Time (min)", "Average Counselor Idle Time (min)",
            "Probability of Waiting", "Average Stress Before CBT",
            "Average Stress After CBT", "Average Stress Reduction",
            "CBT Power",
        ],
        "Value": [
            n_students, counselors,
            avg_waiting, max_waiting,
            avg_service, avg_idle,
            f"{probability_wait:.2%}", avg_stress_before,
            avg_stress_after, avg_stress_red,
            cbt_power,
        ]
    })

    # ── Visualizations ───────────────────────────────────────────────────────
    section_header("📈", "Visualizations")

    # Chart 1 & 2 side-by-side
    vc1, vc2 = st.columns(2)

    with vc1:
        # Stress before/after — line with fill
        fig_stress = go.Figure()
        students = result["Student"]
        fig_stress.add_trace(go.Scatter(
            x=students, y=result["Stress Before CBT"],
            name="Before CBT", mode="lines",
            line=dict(color=DANGER, width=2),
            fill="tozeroy", fillcolor="rgba(248,113,113,.08)"
        ))
        fig_stress.add_trace(go.Scatter(
            x=students, y=result["Stress After CBT"],
            name="After CBT", mode="lines",
            line=dict(color=SUCCESS, width=2),
            fill="tozeroy", fillcolor="rgba(52,211,153,.08)"
        ))
        fig_stress.update_layout(
            title="Stress Level Before & After CBT",
            **CHART_THEME,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            yaxis=dict(**CHART_THEME["yaxis"], range=[0, 1.05])
        )
        st.plotly_chart(fig_stress, use_container_width=True)

    with vc2:
        # Waiting time bar
        fig_wait = go.Figure(go.Bar(
            x=students, y=result["Waiting Time"],
            marker=dict(
                color=result["Waiting Time"],
                colorscale=[[0, ACCENT], [0.5, ACCENT2], [1.0, DANGER]],
                showscale=True,
                colorbar=dict(title="min", tickfont=dict(color="#6b7280"))
            )
        ))
        fig_wait.update_layout(title="Waiting Time per Student", **CHART_THEME)
        st.plotly_chart(fig_wait, use_container_width=True)

    vc3, vc4 = st.columns(2)

    with vc3:
        # Counselor workload
        wl = result.groupby("Counselor")["Service Time"].sum().reset_index()
        fig_wl = go.Figure(go.Bar(
            x=wl["Counselor"].astype(str),
            y=wl["Service Time"],
            marker=dict(
                color=wl["Service Time"],
                colorscale=[[0, ACCENT], [1, ACCENT2]],
                showscale=False
            ),
            text=wl["Service Time"],
            textposition="outside",
            textfont=dict(color="#9ca3af", size=11)
        ))
        fig_wl.update_layout(
            title="Total Service Time by Counselor",
            xaxis_title="Counselor ID",
            yaxis_title="Total Minutes",
            **CHART_THEME
        )
        st.plotly_chart(fig_wl, use_container_width=True)

    with vc4:
        # Stress reduction distribution histogram
        reduction = result["Stress Before CBT"] - result["Stress After CBT"]
        fig_hist = go.Figure(go.Histogram(
            x=reduction, nbinsx=30,
            marker=dict(color=SUCCESS, opacity=0.75, line=dict(color=SUCCESS, width=0.5))
        ))
        fig_hist.update_layout(
            title="Stress Reduction Distribution",
            xaxis_title="Stress Reduction",
            yaxis_title="Frequency",
            **CHART_THEME
        )
        st.plotly_chart(fig_hist, use_container_width=True)

    # ── Tables ───────────────────────────────────────────────────────────────
    section_header("📋", "Data Tables")

    tab1, tab2, tab3 = st.tabs(["📥 Input Dataset", "📤 Simulation Result", "📑 Summary"])

    DISPLAY_COLS = [
        "Student", "Interarrival Time", "Arrival Time", "Service Time",
        "Service Begins", "Service Ends", "Waiting Time",
        "Counselor Idle Time", "Counselor",
        "Stress Before CBT", "Stress After CBT", "Resilience"
    ]

    with tab1:
        st.dataframe(dataset, use_container_width=True, height=380)

    with tab2:
        st.dataframe(result[DISPLAY_COLS], use_container_width=True, height=380)

    with tab3:
        st.dataframe(summary_df, use_container_width=True)

    # ── Export ───────────────────────────────────────────────────────────────
    section_header("💾", "Export")

    ec1, ec2 = st.columns(2)

    csv_data = result[DISPLAY_COLS].to_csv(index=False).encode("utf-8")
    with ec1:
        st.download_button(
            "⬇  Download Result CSV",
            data=csv_data,
            file_name=f"counseling_simulation_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv",
            use_container_width=True
        )

    pdf_data = create_pdf(summary_df, avg_waiting, counselors, probability_wait)
    with ec2:
        st.download_button(
            "⬇  Download Summary PDF",
            data=pdf_data,
            file_name=f"counseling_report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    # ── Monte Carlo ──────────────────────────────────────────────────────────
    section_header("🎲", "Monte Carlo Analysis")

    with st.spinner(f"Running {monte_carlo_runs} Monte Carlo iterations…"):
        mc_results = []
        # Use same-size sample as loaded dataset for fair comparison
        mc_n = min(n_students, 200)  # cap per-run at 200 for speed, note it
        for _ in range(monte_carlo_runs):
            mc_ds    = generate_dataset(mc_n)
            mc_model = CounselingQueueSimulation(mc_ds, cbt_power=cbt_power, counselors=counselors)
            mc_res   = mc_model.run()
            mc_results.append({
                "Avg Wait (min)":        round(mc_res["Waiting Time"].mean(), 2),
                "P(Waiting)":            round((mc_res["Waiting Time"] > 0).mean(), 4),
                "Avg Service (min)":     round(mc_res["Service Time"].mean(), 2),
                "Avg Stress Reduction":  round((mc_res["Stress Before CBT"] - mc_res["Stress After CBT"]).mean(), 4),
            })

    mc_df = pd.DataFrame(mc_results)

    if n_students > 200:
        st.info(f"ℹ️  Monte Carlo runs use {mc_n} students per iteration (capped for performance). "
                f"Your main simulation used the full {n_students:,} students.")

    mc1, mc2 = st.columns(2)

    with mc1:
        st.markdown("**Descriptive Statistics**")
        st.dataframe(mc_df.describe().round(3), use_container_width=True)

    with mc2:
        fig_mc = go.Figure()
        fig_mc.add_trace(go.Histogram(
            x=mc_df["Avg Wait (min)"], nbinsx=25,
            name="Avg Wait",
            marker=dict(color=ACCENT, opacity=0.8)
        ))
        fig_mc.add_vline(
            x=mc_df["Avg Wait (min)"].mean(),
            line_dash="dash", line_color=WARNING,
            annotation_text=f"Mean: {mc_df['Avg Wait (min)'].mean():.2f}",
            annotation_font_color=WARNING
        )
        fig_mc.update_layout(
            title="Monte Carlo: Distribution of Avg Waiting Time",
            xaxis_title="Average Waiting Time (min)",
            yaxis_title="Frequency",
            **CHART_THEME
        )
        st.plotly_chart(fig_mc, use_container_width=True)

    # Scatter: wait vs service
    fig_scatter = px.scatter(
        mc_df, x="Avg Service (min)", y="Avg Wait (min)",
        color="P(Waiting)",
        color_continuous_scale=[[0, SUCCESS], [0.5, ACCENT], [1, DANGER]],
        title="Monte Carlo: Service Time vs. Wait Time",
        labels={"Avg Service (min)": "Avg Service (min)", "Avg Wait (min)": "Avg Wait (min)"},
    )
    fig_scatter.update_layout(**CHART_THEME)
    fig_scatter.update_traces(marker=dict(size=6, opacity=0.75))
    st.plotly_chart(fig_scatter, use_container_width=True)

    # ── AI Recommendation ────────────────────────────────────────────────────
    section_header("🤖", "AI Recommendation")

    if avg_waiting > 20 or probability_wait > 0.60:
        status_class = "warning"
        icon = "⚠️"
        title_txt = "System Overloaded"
        body_txt = (f"Average waiting time is <strong>{avg_waiting} min</strong> and "
                    f"{probability_wait:.1%} of students must wait. "
                    f"Consider increasing counselors to <strong>{counselors + 1}</strong> "
                    f"to reduce queue pressure and improve student experience.")
    elif avg_waiting < 5 and probability_wait < 0.30:
        status_class = "success"
        icon = "✅"
        title_txt = "System Efficient"
        body_txt = (f"Excellent queue performance — only {probability_wait:.1%} of students wait, "
                    f"with an average of just <strong>{avg_waiting} min</strong>. "
                    f"Current staffing of <strong>{counselors}</strong> counselor(s) is well-calibrated.")
    else:
        status_class = "info"
        icon = "ℹ️"
        title_txt = "System Moderately Busy"
        body_txt = (f"The system is running at moderate load. "
                    f"Average wait is <strong>{avg_waiting} min</strong> with "
                    f"{probability_wait:.1%} probability of waiting. "
                    f"Current allocation is acceptable; monitor during peak periods.")

    st.markdown(f"""
    <div class="ai-box {status_class}">
        <div class="ai-icon">{icon}</div>
        <div class="ai-text">
            <strong>{title_txt}</strong>
            <p>{body_txt}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)

else:
    # ── Empty state ───────────────────────────────────────────────────────────
    st.markdown("""
    <div style="text-align:center; padding: 5rem 2rem; color:#6b7280;">
        <div style="font-size:3rem; margin-bottom:1rem;">🧠</div>
        <div style="font-family:'DM Serif Display',serif; font-size:1.8rem;
             color:#e8eaf0; margin-bottom:.75rem;">Ready to Simulate</div>
        <div style="font-size:1rem; max-width:500px; margin:0 auto; line-height:1.7;">
            Configure the parameters in the sidebar, then click
            <strong style="color:#4f9cf9;">▶ Run Simulation</strong> — or upload a CSV dataset.
        </div>
        <div style="margin-top:2.5rem; display:flex; justify-content:center; gap:2rem; flex-wrap:wrap;">
            <div style="background:#181c27; border:1px solid #252a38; border-radius:12px;
                 padding:1.2rem 1.8rem; min-width:160px;">
                <div style="font-size:1.5rem;">👥</div>
                <div style="font-size:.8rem; margin-top:.4rem; text-transform:uppercase;
                     letter-spacing:.08em; color:#4f9cf9;">Up to 2,000 students</div>
            </div>
            <div style="background:#181c27; border:1px solid #252a38; border-radius:12px;
                 padding:1.2rem 1.8rem; min-width:160px;">
                <div style="font-size:1.5rem;">🎲</div>
                <div style="font-size:.8rem; margin-top:.4rem; text-transform:uppercase;
                     letter-spacing:.08em; color:#a78bfa;">Monte Carlo analysis</div>
            </div>
            <div style="background:#181c27; border:1px solid #252a38; border-radius:12px;
                 padding:1.2rem 1.8rem; min-width:160px;">
                <div style="font-size:1.5rem;">🧘</div>
                <div style="font-size:.8rem; margin-top:.4rem; text-transform:uppercase;
                     letter-spacing:.08em; color:#34d399;">CBT stress reduction</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)