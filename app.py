import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import io

# ══════════════════════════════════════════════
# PAGE CONFIG
# ══════════════════════════════════════════════

st.set_page_config(
    page_title="CounselingQ · Simulation System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ══════════════════════════════════════════════
# DESIGN SYSTEM — Academic Precision Theme
# Inspired by scientific journals + Swiss design
# Fonts: Playfair Display (headers) + Source Serif 4 (body) + IBM Plex Mono (data)
# ══════════════════════════════════════════════

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Source+Serif+4:wght@300;400;600&family=IBM+Plex+Mono:wght@400;500;600&family=Outfit:wght@300;400;500;600&display=swap');

/* ─── Reset & Root ─── */
*, *::before, *::after { box-sizing: border-box; }

:root {
    --ink:        #0f1923;
    --ink-2:      #1e2d3d;
    --ink-3:      #2d4157;
    --slate:      #4a6080;
    --slate-2:    #6b849e;
    --fog:        #8fa3b8;
    --mist:       #b8c8d8;
    --cloud:      #dce8f0;
    --paper:      #f0f5f9;
    --white:      #fafcfe;

    --royal:      #1a3a6b;
    --royal-2:    #2454a4;
    --azure:      #3b7dd8;
    --sky:        #5b9be8;

    --teal:       #0d7377;
    --teal-2:     #14919b;
    --mint:       #22c9be;

    --gold:       #b8860b;
    --amber:      #d4a017;
    --sun:        #f0c040;

    --crimson:    #8b1a2e;
    --rose:       #c0392b;
    --blush:      #e74c5e;

    --emerald:    #1a6b3a;
    --leaf:       #27ae60;
    --sage:       #52c97f;

    --ff-display: 'Playfair Display', Georgia, serif;
    --ff-body:    'Source Serif 4', Georgia, serif;
    --ff-ui:      'Outfit', system-ui, sans-serif;
    --ff-mono:    'IBM Plex Mono', 'Courier New', monospace;

    --radius:     6px;
    --radius-lg:  12px;
    --radius-xl:  18px;

    --shadow-sm:  0 1px 3px rgba(15,25,35,.08), 0 1px 2px rgba(15,25,35,.06);
    --shadow:     0 4px 16px rgba(15,25,35,.10), 0 2px 6px rgba(15,25,35,.07);
    --shadow-lg:  0 12px 40px rgba(15,25,35,.14), 0 4px 12px rgba(15,25,35,.09);
}

/* ─── App Shell ─── */
.stApp {
    background: var(--paper);
    font-family: var(--ff-ui);
    color: var(--ink);
}

/* ─── Sidebar ─── */
[data-testid="stSidebar"] {
    background: var(--ink) !important;
    border-right: none !important;
}
[data-testid="stSidebar"] > div:first-child {
    padding-top: 0 !important;
}
[data-testid="stSidebar"] * {
    color: var(--cloud) !important;
}
[data-testid="stSidebar"] .stSlider > div > div {
    background: var(--ink-3) !important;
}
[data-testid="stSidebar"] .stSlider > div > div > div {
    background: var(--azure) !important;
}
[data-testid="stSidebar"] label {
    color: var(--mist) !important;
    font-family: var(--ff-ui) !important;
    font-size: .78rem !important;
    font-weight: 500 !important;
    text-transform: uppercase;
    letter-spacing: .06em;
}
[data-testid="stSidebar"] .stMarkdown p {
    color: var(--fog) !important;
    font-size: .8rem !important;
}
[data-testid="stSidebar"] hr {
    border-color: var(--ink-3) !important;
}

/* ─── Headings ─── */
h1, h2, h3, h4 {
    font-family: var(--ff-display) !important;
    color: var(--ink) !important;
    letter-spacing: -0.01em;
}

/* ─── Progress bar ─── */
.stProgress > div {
    background: var(--cloud) !important;
    border-radius: 2px !important;
    height: 4px !important;
}
.stProgress > div > div {
    background: linear-gradient(90deg, var(--royal-2), var(--azure)) !important;
    border-radius: 2px !important;
}

/* ─── Buttons ─── */
.stButton > button {
    background: var(--royal) !important;
    color: var(--white) !important;
    border: none !important;
    border-radius: var(--radius) !important;
    font-family: var(--ff-ui) !important;
    font-weight: 600 !important;
    font-size: .82rem !important;
    letter-spacing: .04em !important;
    padding: .55rem 1.2rem !important;
    transition: all .2s !important;
    box-shadow: var(--shadow-sm) !important;
}
.stButton > button:hover {
    background: var(--royal-2) !important;
    box-shadow: var(--shadow) !important;
    transform: translateY(-1px) !important;
}
.stDownloadButton > button {
    background: transparent !important;
    color: var(--royal-2) !important;
    border: 1.5px solid var(--royal-2) !important;
    border-radius: var(--radius) !important;
    font-family: var(--ff-ui) !important;
    font-weight: 600 !important;
    font-size: .82rem !important;
    letter-spacing: .04em !important;
    padding: .5rem 1.2rem !important;
    transition: all .2s !important;
}
.stDownloadButton > button:hover {
    background: var(--royal) !important;
    color: var(--white) !important;
    transform: translateY(-1px) !important;
}

/* ─── DataFrames ─── */
.stDataFrame {
    border: 1px solid var(--cloud) !important;
    border-radius: var(--radius) !important;
    overflow: hidden !important;
    box-shadow: var(--shadow-sm) !important;
}
.stDataFrame thead th {
    background: var(--ink) !important;
    color: var(--cloud) !important;
    font-family: var(--ff-mono) !important;
    font-size: .72rem !important;
    letter-spacing: .04em !important;
    text-transform: uppercase !important;
    padding: .5rem .75rem !important;
}
.stDataFrame tbody tr:nth-child(even) td {
    background: var(--paper) !important;
}
.stDataFrame tbody td {
    font-family: var(--ff-mono) !important;
    font-size: .79rem !important;
    color: var(--ink-2) !important;
    padding: .4rem .75rem !important;
}

/* ─── Tabs ─── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 2px solid var(--cloud) !important;
    gap: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: var(--ff-ui) !important;
    font-size: .8rem !important;
    font-weight: 500 !important;
    color: var(--slate) !important;
    padding: .6rem 1.2rem !important;
    border-bottom: 2px solid transparent !important;
    margin-bottom: -2px !important;
}
.stTabs [aria-selected="true"] {
    color: var(--royal-2) !important;
    border-bottom-color: var(--royal-2) !important;
    font-weight: 600 !important;
}

/* ─── Input ─── */
input {
    font-family: var(--ff-ui) !important;
    border: 1.5px solid var(--cloud) !important;
    border-radius: var(--radius) !important;
    color: var(--ink) !important;
}
input:focus {
    border-color: var(--azure) !important;
    box-shadow: 0 0 0 3px rgba(59,125,216,.15) !important;
}

/* ─── Alert ─── */
.stAlert { border-radius: var(--radius) !important; }

/* ─── Spinner ─── */
.stSpinner > div { border-top-color: var(--azure) !important; }

/* ══════════════════════════════════════
   CUSTOM COMPONENTS
══════════════════════════════════════ */

/* Masthead */
.masthead {
    background: var(--ink);
    margin: -1rem -1rem 0;
    padding: 0 2.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 3px solid var(--royal-2);
    position: relative;
    overflow: hidden;
}
.masthead::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(
        90deg,
        transparent,
        transparent 60px,
        rgba(255,255,255,.015) 60px,
        rgba(255,255,255,.015) 61px
    );
}
.masthead-left { display: flex; align-items: center; gap: 1.2rem; padding: 1.4rem 0; }
.masthead-logo {
    width: 46px; height: 46px;
    background: linear-gradient(135deg, var(--royal-2), var(--azure));
    border-radius: var(--radius);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem;
    flex-shrink: 0;
    box-shadow: 0 4px 12px rgba(36,84,164,.4);
}
.masthead-brand {
    font-family: var(--ff-display);
    font-size: 1.35rem;
    font-weight: 700;
    color: #fff;
    letter-spacing: -.01em;
    line-height: 1.1;
}
.masthead-sub {
    font-family: var(--ff-ui);
    font-size: .68rem;
    color: var(--fog);
    text-transform: uppercase;
    letter-spacing: .1em;
    margin-top: .15rem;
}
.masthead-badge {
    font-family: var(--ff-mono);
    font-size: .65rem;
    font-weight: 600;
    letter-spacing: .08em;
    text-transform: uppercase;
    padding: .25rem .7rem;
    border: 1px solid rgba(255,255,255,.15);
    border-radius: 20px;
    color: var(--fog);
    white-space: nowrap;
}

/* Page hero */
.page-hero {
    padding: 2.5rem 0 2rem;
    border-bottom: 1px solid var(--cloud);
    margin-bottom: 2rem;
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
}
.hero-eyebrow {
    font-family: var(--ff-mono);
    font-size: .65rem;
    font-weight: 600;
    color: var(--azure);
    text-transform: uppercase;
    letter-spacing: .14em;
    margin-bottom: .5rem;
}
.hero-h1 {
    font-family: var(--ff-display);
    font-size: 2.4rem;
    font-weight: 700;
    color: var(--ink);
    line-height: 1.12;
    margin: 0 0 .5rem;
}
.hero-desc {
    font-family: var(--ff-body);
    font-size: .98rem;
    color: var(--slate);
    font-weight: 300;
    line-height: 1.7;
    max-width: 520px;
}
.hero-meta {
    display: flex;
    gap: .5rem;
    flex-wrap: wrap;
}
.hero-tag {
    font-family: var(--ff-mono);
    font-size: .65rem;
    font-weight: 500;
    padding: .3rem .65rem;
    border-radius: 3px;
    text-transform: uppercase;
    letter-spacing: .07em;
}
.hero-tag.blue   { background: rgba(59,125,216,.1);  color: var(--royal-2); border: 1px solid rgba(59,125,216,.2); }
.hero-tag.teal   { background: rgba(13,115,119,.1);  color: var(--teal);    border: 1px solid rgba(13,115,119,.2); }
.hero-tag.amber  { background: rgba(212,160,23,.1);  color: var(--gold);    border: 1px solid rgba(212,160,23,.2); }

/* Section header */
.sec-hdr {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin: 2.5rem 0 1.2rem;
    padding-bottom: .8rem;
    border-bottom: 1px solid var(--cloud);
}
.sec-num {
    font-family: var(--ff-mono);
    font-size: .65rem;
    font-weight: 600;
    color: var(--azure);
    background: rgba(59,125,216,.08);
    border: 1px solid rgba(59,125,216,.2);
    border-radius: 3px;
    padding: .2rem .45rem;
    letter-spacing: .06em;
}
.sec-title {
    font-family: var(--ff-display);
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--ink);
    margin: 0;
}
.sec-rule { flex: 1; height: 1px; background: var(--cloud); }

/* KPI Cards */
.kpi-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: .75rem; margin-bottom: .75rem; }
.kpi-card {
    background: var(--white);
    border: 1px solid var(--cloud);
    border-radius: var(--radius-lg);
    padding: 1.1rem 1.2rem;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    transition: box-shadow .2s, transform .15s;
}
.kpi-card:hover { box-shadow: var(--shadow); transform: translateY(-2px); }
.kpi-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0; height: 3px;
    border-radius: 0 0 var(--radius-lg) var(--radius-lg);
}
.kpi-card.royal::after  { background: linear-gradient(90deg, var(--royal), var(--azure)); }
.kpi-card.teal::after   { background: linear-gradient(90deg, var(--teal), var(--mint)); }
.kpi-card.amber::after  { background: linear-gradient(90deg, var(--gold), var(--sun)); }
.kpi-card.crimson::after{ background: linear-gradient(90deg, var(--crimson), var(--blush)); }
.kpi-card.emerald::after{ background: linear-gradient(90deg, var(--emerald), var(--sage)); }

.kpi-label {
    font-family: var(--ff-ui);
    font-size: .67rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: .1em;
    color: var(--slate-2);
    margin-bottom: .45rem;
}
.kpi-value {
    font-family: var(--ff-mono);
    font-size: 1.75rem;
    font-weight: 600;
    color: var(--ink);
    line-height: 1;
    margin-bottom: .25rem;
}
.kpi-unit {
    font-family: var(--ff-ui);
    font-size: .7rem;
    color: var(--fog);
    font-weight: 400;
}
.kpi-icon {
    position: absolute;
    top: 1rem; right: 1rem;
    font-size: 1.1rem;
    opacity: .25;
}

/* Chart wrapper */
.chart-panel {
    background: var(--white);
    border: 1px solid var(--cloud);
    border-radius: var(--radius-lg);
    padding: 1.2rem 1.3rem;
    box-shadow: var(--shadow-sm);
    margin-bottom: .75rem;
}
.chart-label {
    font-family: var(--ff-display);
    font-size: .95rem;
    font-weight: 600;
    color: var(--ink-2);
    margin-bottom: .2rem;
}
.chart-sublabel {
    font-family: var(--ff-ui);
    font-size: .72rem;
    color: var(--fog);
    margin-bottom: .9rem;
    text-transform: uppercase;
    letter-spacing: .05em;
}

/* Status badge */
.status-pill {
    display: inline-flex;
    align-items: center;
    gap: .35rem;
    font-family: var(--ff-mono);
    font-size: .66rem;
    font-weight: 600;
    letter-spacing: .07em;
    text-transform: uppercase;
    padding: .28rem .7rem;
    border-radius: 20px;
}
.status-pill.ok     { background: rgba(26,107,58,.08);  color: var(--leaf);   border: 1px solid rgba(26,107,58,.2); }
.status-pill.warn   { background: rgba(184,134,11,.08); color: var(--gold);   border: 1px solid rgba(184,134,11,.2); }
.status-pill.danger { background: rgba(139,26,46,.08);  color: var(--rose);   border: 1px solid rgba(139,26,46,.2); }
.status-pill.info   { background: rgba(26,58,107,.08);  color: var(--royal-2);border: 1px solid rgba(26,58,107,.2); }

/* AI Recommendation panel */
.rec-panel {
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    display: flex;
    gap: 1.2rem;
    align-items: flex-start;
    box-shadow: var(--shadow-sm);
}
.rec-panel.ok   { background: rgba(26,107,58,.04); border: 1px solid rgba(26,107,58,.15); border-left: 4px solid var(--leaf); }
.rec-panel.warn { background: rgba(184,134,11,.04); border: 1px solid rgba(184,134,11,.15); border-left: 4px solid var(--amber); }
.rec-panel.info { background: rgba(26,58,107,.04); border: 1px solid rgba(26,58,107,.12); border-left: 4px solid var(--royal-2); }
.rec-ico  { font-size: 1.8rem; line-height: 1; flex-shrink: 0; }
.rec-head { font-family: var(--ff-display); font-size: 1.05rem; font-weight: 600; color: var(--ink); margin-bottom: .3rem; }
.rec-body { font-family: var(--ff-body); font-size: .9rem; color: var(--slate); line-height: 1.7; margin: 0; }
.rec-body strong { color: var(--ink); font-weight: 600; }

/* Login page */
.login-wrap {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: var(--ink);
    padding: 2rem;
    position: fixed;
    inset: 0;
    z-index: 999;
}
.login-card {
    background: var(--ink-2);
    border: 1px solid var(--ink-3);
    border-radius: var(--radius-xl);
    padding: 2.5rem;
    width: 100%;
    max-width: 400px;
    box-shadow: var(--shadow-lg);
}
.login-logo {
    width: 56px; height: 56px;
    background: linear-gradient(135deg, var(--royal-2), var(--azure));
    border-radius: var(--radius-lg);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.6rem;
    margin: 0 auto 1.2rem;
    box-shadow: 0 8px 24px rgba(36,84,164,.5);
}
.login-title {
    font-family: var(--ff-display);
    font-size: 1.6rem;
    font-weight: 700;
    color: #fff;
    text-align: center;
    margin-bottom: .25rem;
}
.login-sub {
    font-family: var(--ff-ui);
    font-size: .78rem;
    color: var(--fog);
    text-align: center;
    margin-bottom: 1.8rem;
    text-transform: uppercase;
    letter-spacing: .08em;
}

/* Sidebar logo block */
.sb-logo {
    background: linear-gradient(180deg, var(--ink-2) 0%, var(--ink) 100%);
    margin: 0 -1rem;
    padding: 1.5rem 1rem 1.2rem;
    border-bottom: 1px solid var(--ink-3);
    margin-bottom: 1.2rem;
}
.sb-logo-row { display: flex; align-items: center; gap: .75rem; }
.sb-logo-icon {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, var(--royal-2), var(--azure));
    border-radius: var(--radius);
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
}
.sb-logo-text { font-family: var(--ff-display); font-size: 1.1rem; color: #fff; font-weight: 700; }
.sb-logo-ver  { font-family: var(--ff-mono); font-size: .6rem; color: var(--slate-2); letter-spacing: .08em; margin-top: .1rem; text-transform: uppercase; }

/* Divider with label */
.div-label {
    display: flex;
    align-items: center;
    gap: .6rem;
    margin: .8rem 0 .6rem;
    font-family: var(--ff-mono);
    font-size: .6rem;
    font-weight: 600;
    color: var(--slate-2);
    text-transform: uppercase;
    letter-spacing: .1em;
}
.div-label::before, .div-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--ink-3);
}

/* Progress status */
.prog-line {
    font-family: var(--ff-mono);
    font-size: .75rem;
    color: var(--slate-2);
    padding: .4rem .7rem;
    background: var(--white);
    border: 1px solid var(--cloud);
    border-radius: var(--radius);
    margin-top: .4rem;
}

/* Empty state */
.empty-state {
    text-align: center;
    padding: 5rem 2rem;
    max-width: 540px;
    margin: 0 auto;
}
.empty-icon {
    font-size: 3.5rem;
    margin-bottom: 1.2rem;
    display: block;
    opacity: .7;
}
.empty-title {
    font-family: var(--ff-display);
    font-size: 1.9rem;
    font-weight: 700;
    color: var(--ink);
    margin-bottom: .75rem;
}
.empty-desc {
    font-family: var(--ff-body);
    font-size: .95rem;
    color: var(--slate);
    line-height: 1.8;
    margin-bottom: 2rem;
}
.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: .75rem;
    margin-top: 1.5rem;
}
.feature-tile {
    background: var(--white);
    border: 1px solid var(--cloud);
    border-radius: var(--radius-lg);
    padding: 1.1rem .9rem;
    box-shadow: var(--shadow-sm);
}
.feature-ico { font-size: 1.3rem; margin-bottom: .45rem; }
.feature-name {
    font-family: var(--ff-mono);
    font-size: .63rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: .08em;
    color: var(--slate);
}

/* Footer strip */
.footer-strip {
    background: var(--ink);
    margin: 2rem -1rem -1rem;
    padding: 1rem 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-family: var(--ff-mono);
    font-size: .63rem;
    color: var(--slate-2);
    letter-spacing: .05em;
}
.footer-strip strong { color: var(--fog); }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# TIME FORMAT
# ══════════════════════════════════════════════

START_TIME = datetime.strptime("08:00", "%H:%M")

def to_clock(minutes):
    return (START_TIME + timedelta(minutes=int(minutes))).strftime("%H:%M")

# ══════════════════════════════════════════════
# SIMULATION ENGINE
# ══════════════════════════════════════════════

class CounselingQueueSimulation:
    def __init__(self, dataset, cbt_power=0.5, counselors=1):
        self.dataset    = dataset.copy().reset_index(drop=True)
        self.cbt_power  = cbt_power
        self.counselors = counselors

    def run(self):
        n   = len(self.dataset)
        ds  = self.dataset

        # ── Pre-extract columns as numpy arrays (avoid repeated .loc overhead) ──
        interarr = ds["Interarrival Time"].to_numpy(dtype=np.float64)
        stress   = ds["Stress Before CBT"].to_numpy(dtype=np.float64)
        resil    = ds["Resilience"].to_numpy(dtype=np.float64)

        # ── Vectorised pre-computations ──
        # Service time: 20 + stress * 35, rounded to int
        svc = np.round(20.0 + stress * 35.0).astype(np.int32)

        # Stress after CBT (fully vectorised)
        sa  = np.clip(stress - resil * self.cbt_power, 0.0, None)
        sa  = np.round(sa, 4)

        # Arrival minutes: cumulative sum of interarrival, first student at 0
        arr_m         = np.empty(n, dtype=np.float64)
        arr_m[0]      = 0.0
        arr_m[1:]     = np.cumsum(interarr[1:])   # student 0 has no prior

        # ── Queue scheduling loop (must stay sequential — inherently serial) ──
        avail = np.zeros(self.counselors, dtype=np.float64)
        beg   = np.empty(n, dtype=np.float64)
        end   = np.empty(n, dtype=np.float64)
        coun  = np.empty(n, dtype=np.int32)
        idle  = np.empty(n, dtype=np.float64)

        for i in range(n):
            a          = arr_m[i]
            s          = int(np.argmin(avail))
            prev       = avail[s]
            b          = prev if prev > a else a
            e          = b + svc[i]
            avail[s]   = e
            beg[i]     = b
            end[i]     = e
            coun[i]    = s + 1
            idle[i]    = a - prev if a > prev else 0.0

        wait = beg - arr_m

        # ── Batch-convert minutes → clock strings (vectorised via numpy) ──
        def mins_to_clock_vec(arr):
            total_mins = arr.astype(np.int64)
            hh = (total_mins // 60 + 8) % 24       # start at 08:00
            mm = total_mins % 60
            return [f"{h:02d}:{m:02d}" for h, m in zip(hh, mm)]

        out = ds.copy()
        out["Arrival Time"]          = mins_to_clock_vec(arr_m)
        out["Service Begins"]        = mins_to_clock_vec(beg)
        out["Service Ends"]          = mins_to_clock_vec(end)
        out["Arrival Minutes"]       = arr_m
        out["Service Time"]          = svc
        out["Service Begin Minutes"] = beg
        out["Service End Minutes"]   = end
        out["Waiting Time"]          = wait
        out["Counselor Idle Time"]   = idle
        out["Counselor"]             = coun
        out["Stress After CBT"]      = sa
        return out

# ══════════════════════════════════════════════
# DATASET GENERATOR
# ══════════════════════════════════════════════

def generate_dataset(n):
    rng = np.random.default_rng()
    return pd.DataFrame({
        "Student":           range(1, n + 1),
        "Interarrival Time": rng.integers(10, 60, n).astype(int),
        "Stress Before CBT": np.round(rng.uniform(0.40, 0.95, n), 3),
        "Resilience":        np.round(rng.uniform(0.15, 0.60, n), 3),
    })

# ══════════════════════════════════════════════
# EXPORT — TXT fallback (no external deps)
# ══════════════════════════════════════════════

def export_summary_txt(summary_df, avg_waiting, counselors, probability_wait):
    ts  = datetime.now().strftime("%d %B %Y  %H:%M")
    sep = "─" * 52
    lines = [
        "COUNSELINGQ SIMULATION REPORT",
        f"Generated : {ts}",
        sep, "",
        "SIMULATION SUMMARY", "",
    ]
    for _, row in summary_df.iterrows():
        lines.append(f"  {row['Indicator']:<40} {row['Value']}")
    lines += ["", sep, "", "AI RECOMMENDATION", ""]
    if avg_waiting > 20 or probability_wait > 0.60:
        lines.append(f"  ⚠  SYSTEM OVERLOADED — recommend {counselors+1} counselors.")
    elif avg_waiting < 5 and probability_wait < 0.30:
        lines.append("  ✓  SYSTEM EFFICIENT — current staffing is optimal.")
    else:
        lines.append("  ℹ  SYSTEM MODERATE — monitor during peak periods.")
    lines += ["", sep,
              "CounselingQ · Academic Queue Simulation System",
              "Developed for institutional HKI research purposes."]
    return "\n".join(lines).encode("utf-8")

def _safe(text):
    """Replace non-latin-1 characters so fpdf (Arial/latin-1) never chokes."""
    replacements = {
        "\u2014": "-",   # em dash
        "\u2013": "-",   # en dash
        "\u2018": "'",   # left single quote
        "\u2019": "'",   # right single quote
        "\u201c": '"',   # left double quote
        "\u201d": '"',   # right double quote
        "\u2026": "...", # ellipsis
        "\u00d7": "x",   # multiplication sign
        "\u2022": "*",   # bullet
        "\u2265": ">=",  # greater-equal
        "\u2264": "<=",  # less-equal
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    # Final fallback: drop anything still outside latin-1
    return text.encode("latin-1", errors="replace").decode("latin-1")


def try_fpdf(summary_df, avg_waiting, counselors, probability_wait):
    try:
        from fpdf import FPDF

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=18)

        # ── Header bar ──
        pdf.set_fill_color(26, 58, 107)
        pdf.rect(0, 0, 210, 28, "F")
        pdf.set_font("Arial", "B", 16)
        pdf.set_text_color(255, 255, 255)
        pdf.set_y(8)
        pdf.cell(0, 10, _safe("CounselingQ Simulation Report"), align="C", ln=True)
        pdf.set_font("Arial", "", 8)
        pdf.set_text_color(180, 200, 220)
        pdf.cell(0, 6,
                 _safe(f"Academic Queue Simulation System  |  "
                       f"{datetime.now().strftime('%d %B %Y  %H:%M')}"),
                 align="C", ln=True)
        pdf.ln(10)

        # ── Summary table ──
        pdf.set_font("Arial", "B", 11)
        pdf.set_text_color(15, 25, 35)
        pdf.cell(0, 8, _safe("Simulation Summary"), ln=True)
        pdf.set_draw_color(220, 232, 240)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(3)

        for idx, (_, row) in enumerate(summary_df.iterrows()):
            if idx % 2 == 0:
                pdf.set_fill_color(240, 245, 249)
                pdf.rect(10, pdf.get_y(), 190, 7, "F")
            pdf.set_font("Arial", "B", 8.5)
            pdf.set_text_color(74, 96, 128)
            pdf.cell(100, 7, _safe(f"  {row['Indicator']}"))
            pdf.set_font("Arial", "", 8.5)
            pdf.set_text_color(15, 25, 35)
            pdf.cell(0, 7, _safe(str(row["Value"])), ln=True)

        pdf.ln(6)

        # ── Recommendation ──
        pdf.set_font("Arial", "B", 11)
        pdf.set_text_color(15, 25, 35)
        pdf.cell(0, 8, _safe("AI Recommendation"), ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(3)
        pdf.set_font("Arial", "", 9)
        pdf.set_text_color(74, 96, 128)

        if avg_waiting > 20 or probability_wait > 0.60:
            msg = (f"System is overloaded. Average waiting time is {avg_waiting} minutes "
                   f"with {probability_wait:.1%} of students waiting. "
                   f"It is recommended to increase the number of counselors to {counselors + 1}.")
        elif avg_waiting < 5 and probability_wait < 0.30:
            msg = (f"System is operating efficiently. Average waiting time is {avg_waiting} minutes "
                   f"with only {probability_wait:.1%} of students waiting. "
                   f"Current allocation of {counselors} counselor(s) is well-calibrated.")
        else:
            msg = (f"System is moderately busy. Average waiting time is {avg_waiting} minutes "
                   f"with {probability_wait:.1%} probability of waiting. "
                   "Current allocation is acceptable; monitor closely during peak periods.")

        pdf.multi_cell(0, 6.5, _safe(msg))

        # ── Footer ──
        pdf.set_y(-20)
        pdf.set_draw_color(220, 232, 240)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(2)
        pdf.set_font("Arial", "", 7.5)
        pdf.set_text_color(140, 155, 170)
        pdf.cell(0, 5,
                 _safe("CounselingQ Academic Queue Simulation System - Developed for HKI Research"),
                 align="C")

        # ── Output — try dest="S" first, fall back to BytesIO ──
        try:
            raw = pdf.output(dest="S")
            # fpdf2 returns bytes directly; older fpdf returns str
            if isinstance(raw, str):
                return raw.encode("latin-1"), "pdf"
            return raw, "pdf"
        except Exception:
            buf = io.BytesIO()
            pdf.output(buf)
            return buf.getvalue(), "pdf"

    except ImportError:
        return export_summary_txt(summary_df, avg_waiting, counselors, probability_wait), "txt"

# ══════════════════════════════════════════════
# SVG CHARTS — zero external dependencies
# ══════════════════════════════════════════════

def _grid_y(pad, W, H, vmin, vmax, n=5, fmt=".2f"):
    out = ""
    for v in np.linspace(vmin, vmax, n):
        y = pad["t"] + H - ((v - vmin) / max(vmax - vmin, 1e-9)) * H
        out += (f'<line x1="{pad["l"]}" y1="{y:.1f}" x2="{pad["l"]+W}" y2="{y:.1f}" '
                f'stroke="#dce8f0" stroke-width="0.8" stroke-dasharray="3,3"/>'
                f'<text x="{pad["l"]-5}" y="{y+3.5:.1f}" fill="#8fa3b8" font-size="9" text-anchor="end"'
                f' font-family="IBM Plex Mono,monospace">{format(v, fmt)}</text>')
    return out

def make_svg_line(x_vals, y1_vals, y2_vals, label1, label2,
                  color1="#c0392b", color2="#27ae60", width=600, height=260):
    n = len(x_vals)
    if n == 0: return ""
    pad  = dict(l=52, r=20, t=36, b=40)
    W    = width - pad["l"] - pad["r"]
    H    = height - pad["t"] - pad["b"]
    ymax = max(float(np.max(y1_vals)), float(np.max(y2_vals)), 0.01)
    ymin = 0.0

    def px(i): return pad["l"] + (i / max(n - 1, 1)) * W
    def py(v): return pad["t"] + H - ((v - ymin) / (ymax - ymin + 1e-9)) * H

    grid = _grid_y(pad, W, H, ymin, ymax, fmt=".2f")

    def polyline(vals, col):
        pts = " ".join(f"{px(i):.1f},{py(v):.1f}" for i, v in enumerate(vals))
        fp  = (f"{px(0):.1f},{py(0):.1f} " + pts + f" {px(n-1):.1f},{py(0):.1f}")
        return (f'<polygon points="{fp}" fill="{col}" opacity="0.08"/>'
                f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2"'
                f' stroke-linejoin="round" stroke-linecap="round"/>')

    step = max(1, n // 8)
    xlabels = "".join(
        f'<text x="{px(i):.1f}" y="{pad["t"]+H+16}" fill="#8fa3b8" font-size="9"'
        f' text-anchor="middle" font-family="IBM Plex Mono,monospace">{int(x_vals[i])}</text>'
        for i in range(0, n, step))

    legend = (f'<rect x="{pad["l"]}" y="10" width="10" height="10" fill="{color1}" rx="2"/>'
              f'<text x="{pad["l"]+14}" y="19" fill="#4a6080" font-size="9"'
              f' font-family="Outfit,sans-serif">{label1}</text>'
              f'<rect x="{pad["l"]+100}" y="10" width="10" height="10" fill="{color2}" rx="2"/>'
              f'<text x="{pad["l"]+114}" y="19" fill="#4a6080" font-size="9"'
              f' font-family="Outfit,sans-serif">{label2}</text>')

    return (f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg"'
            f' style="width:100%;height:auto;display:block;">'
            f'<rect width="{width}" height="{height}" fill="#fafcfe" rx="8"/>'
            + grid + polyline(y1_vals, color1) + polyline(y2_vals, color2)
            + xlabels + legend + '</svg>')


def make_svg_bar(categories, values, color_a="#1a3a6b", color_b="#3b7dd8",
                 width=600, height=260):
    n = len(categories)
    if n == 0: return ""
    pad  = dict(l=52, r=20, t=36, b=40)
    W    = width - pad["l"] - pad["r"]
    H    = height - pad["t"] - pad["b"]
    vmax = max(float(np.max(values)), 0.01)
    vmin = 0.0

    grid = _grid_y(pad, W, H, vmin, vmax, fmt=".0f")

    gap   = W / n
    bar_w = max(2.0, gap * 0.62)

    def lerp(t, ca, cb):
        def h(s): return tuple(int(s[i:i+2], 16) for i in (1, 3, 5))
        r1,g1,b1 = h(ca); r2,g2,b2 = h(cb)
        return f"#{int(r1+(r2-r1)*t):02x}{int(g1+(g2-g1)*t):02x}{int(b1+(b2-b1)*t):02x}"

    bars = ""
    for i, (cat, val) in enumerate(zip(categories, values)):
        x  = pad["l"] + i * gap + (gap - bar_w) / 2
        bh = max(1.0, (val / vmax) * H)
        y  = pad["t"] + H - bh
        c  = lerp(i / max(n - 1, 1), color_a, color_b)
        bars += (f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bh:.1f}"'
                 f' fill="{c}" rx="2" opacity="0.9"/>')
        if n <= 30:
            bars += (f'<text x="{x+bar_w/2:.1f}" y="{pad["t"]+H+16}" fill="#8fa3b8" font-size="9"'
                     f' text-anchor="middle" font-family="IBM Plex Mono,monospace">{cat}</text>')

    return (f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg"'
            f' style="width:100%;height:auto;display:block;">'
            f'<rect width="{width}" height="{height}" fill="#fafcfe" rx="8"/>'
            + grid + bars + '</svg>')


def make_svg_hist(values, bins=25, color="#1a3a6b", mean_color="#b8860b",
                  width=600, height=260):
    counts, edges = np.histogram(values, bins=bins)
    pad  = dict(l=52, r=20, t=36, b=40)
    W    = width - pad["l"] - pad["r"]
    H    = height - pad["t"] - pad["b"]
    cmax = max(int(counts.max()), 1)
    emin, emax = float(edges[0]), float(edges[-1])

    def ex(v): return pad["l"] + ((v - emin) / max(emax - emin, 1e-9)) * W
    def ey(c): return pad["t"] + H - (c / cmax) * H

    grid = _grid_y(pad, W, H, 0, cmax, fmt=".0f")

    rects = ""
    for c, e0, e1 in zip(counts, edges[:-1], edges[1:]):
        x  = ex(float(e0)); x2 = ex(float(e1))
        bw = max(1.0, x2 - x - 1.0)
        bh = max(0.5, (c / cmax) * H)
        y  = ey(c)
        rects += (f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}"'
                  f' fill="{color}" opacity="0.82" rx="2"/>')

    mv  = float(np.mean(values))
    mxp = ex(mv)
    mline = (f'<line x1="{mxp:.1f}" y1="{pad["t"]}" x2="{mxp:.1f}" y2="{pad["t"]+H}"'
             f' stroke="{mean_color}" stroke-width="1.8" stroke-dasharray="5,3"/>'
             f'<rect x="{mxp+4:.1f}" y="{pad["t"]+4}" width="46" height="14" fill="{mean_color}" opacity="0.12" rx="3"/>'
             f'<text x="{mxp+6:.1f}" y="{pad["t"]+14}" fill="{mean_color}" font-size="9"'
             f' font-family="IBM Plex Mono,monospace" font-weight="600">μ={mv:.2f}</text>')

    step = max(1, bins // 6)
    xlabels = "".join(
        f'<text x="{ex(float(edges[i])):.1f}" y="{pad["t"]+H+16}" fill="#8fa3b8"'
        f' font-size="9" text-anchor="middle" font-family="IBM Plex Mono,monospace">{edges[i]:.1f}</text>'
        for i in range(0, len(edges), step))

    return (f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg"'
            f' style="width:100%;height:auto;display:block;">'
            f'<rect width="{width}" height="{height}" fill="#fafcfe" rx="8"/>'
            + grid + rects + mline + xlabels + '</svg>')

# ══════════════════════════════════════════════
# UI HELPERS
# ══════════════════════════════════════════════

def kpi(label, value, unit="", color="royal", icon=""):
    return (f'<div class="kpi-card {color}">'
            f'<div class="kpi-icon">{icon}</div>'
            f'<div class="kpi-label">{label}</div>'
            f'<div class="kpi-value">{value}</div>'
            f'<div class="kpi-unit">{unit}</div>'
            f'</div>')

def sec(num, title):
    st.markdown(
        f'<div class="sec-hdr">'
        f'<span class="sec-num">{num:02d}</span>'
        f'<span class="sec-title">{title}</span>'
        f'<span class="sec-rule"></span>'
        f'</div>', unsafe_allow_html=True)

def chart(title, sub, svg):
    st.markdown(
        f'<div class="chart-panel">'
        f'<div class="chart-label">{title}</div>'
        f'<div class="chart-sublabel">{sub}</div>'
        f'{svg}</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════
# LOGIN
# ══════════════════════════════════════════════

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown("""
    <div style="text-align:center;padding:3rem 0 1rem;">
        <div class="login-logo">🎓</div>
        <div class="login-title">CounselingQ</div>
        <div class="login-sub">Academic Queue Simulation System</div>
    </div>""", unsafe_allow_html=True)

    _, col, _ = st.columns([1, 1.1, 1])
    with col:
        username = st.text_input("Username", placeholder="Enter username")
        password = st.text_input("Password", type="password", placeholder="Enter password")

        if st.button("Sign In  →", use_container_width=True):
            if username == "admin" and password == "12345":
                st.session_state.login = True
                st.rerun()
            else:
                st.error("Invalid credentials.")

        st.markdown(
            '<div style="text-align:center;margin-top:.8rem;font-family:\'IBM Plex Mono\',monospace;'
            'font-size:.65rem;color:#6b849e;letter-spacing:.06em;">DEMO  ·  admin / 12345</div>',
            unsafe_allow_html=True)
    st.stop()

# ══════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════

with st.sidebar:
    st.markdown("""
    <div class="sb-logo">
        <div class="sb-logo-row">
            <div class="sb-logo-icon">🎓</div>
            <div>
                <div class="sb-logo-text">CounselingQ</div>
                <div class="sb-logo-ver">v2.0  ·  HKI Edition</div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="div-label">Parameters</div>', unsafe_allow_html=True)
    total_students   = st.slider("Number of Students",   10, 5000, 50,  step=10)
    cbt_power        = st.slider("CBT Effectiveness",  0.10, 1.00, 0.50, step=0.05)
    counselors       = st.slider("Number of Counselors",  1,   20,   1)
    monte_carlo_runs = st.slider("Monte Carlo Runs",     10,  500, 100,  step=10)

    st.markdown('<div class="div-label">Dataset</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload CSV",  type=["csv"],
        help="Required columns: Student · Interarrival Time · Stress Before CBT · Resilience")

    st.markdown('<div class="div-label">Actions</div>', unsafe_allow_html=True)
    generate_button = st.button("▶  Run Simulation", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Sign Out", use_container_width=True):
        st.session_state.login = False
        st.rerun()

# ══════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════

st.markdown(f"""
<div class="masthead">
    <div class="masthead-left">
        <div class="masthead-logo">🎓</div>
        <div>
            <div class="masthead-brand">CounselingQ</div>
            <div class="masthead-sub">Academic Queue Simulation System</div>
        </div>
    </div>
    <div class="masthead-badge">HKI Research Edition  ·  {datetime.now().strftime("%Y")}</div>
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# PAGE HERO
# ══════════════════════════════════════════════

st.markdown("""
<div class="page-hero">
    <div>
        <div class="hero-eyebrow">Simulation Dashboard</div>
        <div class="hero-h1">Counseling Queue<br>Simulation</div>
        <div class="hero-desc">
            Discrete-event simulation model for student counseling service queues,
            integrating Cognitive Behavioral Therapy (CBT) stress reduction
            and Monte Carlo probabilistic analysis.
        </div>
    </div>
    <div class="hero-meta">
        <span class="hero-tag blue">Discrete-Event</span>
        <span class="hero-tag teal">CBT Analytics</span>
        <span class="hero-tag amber">Monte Carlo</span>
    </div>
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# MAIN FLOW
# ══════════════════════════════════════════════

if generate_button or uploaded_file is not None:

    # ── Dataset ──────────────────────────────
    if uploaded_file is not None:
        dataset  = pd.read_csv(uploaded_file)
        required = ["Student", "Interarrival Time", "Stress Before CBT", "Resilience"]
        missing  = [c for c in required if c not in dataset.columns]
        if missing:
            st.error(f"Missing columns: {missing}")
            st.stop()
        dataset = dataset[required].reset_index(drop=True)
        st.success(f"✅  Dataset imported — {len(dataset):,} students loaded")
    else:
        with st.spinner("Generating dataset…"):
            dataset = generate_dataset(total_students)

    n_students = len(dataset)

    # ── Run ──────────────────────────────────
    sec(1, "Simulation Execution")
    prog = st.progress(0)
    stat = st.empty()

    model  = CounselingQueueSimulation(dataset, cbt_power=cbt_power, counselors=counselors)
    result = model.run()

    batch = max(1, n_students // 40)
    for i in range(0, n_students, batch):
        idx = min(i, n_students - 1)
        prog.progress((idx + 1) / n_students)
        if i % max(1, batch * 5) == 0:
            stat.markdown(
                f'<div class="prog-line">'
                f'[{idx+1:>5,} / {n_students:,}]  '
                f'Counselor {result.loc[idx,"Counselor"]}  ·  '
                f'{result.loc[idx,"Service Begins"]} → {result.loc[idx,"Service Ends"]}'
                f'</div>', unsafe_allow_html=True)
        if n_students <= 200:
            time.sleep(0.01)

    prog.progress(1.0)
    stat.markdown(
        '<span class="status-pill ok">✓ &nbsp;Simulation Complete</span>',
        unsafe_allow_html=True)

    # ── Metrics ──────────────────────────────
    avg_waiting       = round(result["Waiting Time"].mean(), 2)
    avg_service       = round(result["Service Time"].mean(), 2)
    avg_idle          = round(result["Counselor Idle Time"].mean(), 2)
    probability_wait  = round((result["Waiting Time"] > 0).mean(), 4)
    avg_stress_before = round(result["Stress Before CBT"].mean(), 4)
    avg_stress_after  = round(result["Stress After CBT"].mean(), 4)
    avg_stress_red    = round(avg_stress_before - avg_stress_after, 4)
    max_waiting       = int(result["Waiting Time"].max())

    sec(2, "Key Performance Indicators")

    row1_html = (
        '<div class="kpi-grid">'
        + kpi("Average Waiting Time", avg_waiting,       "minutes",           "royal",   "⏱")
        + kpi("Average Service Time", avg_service,       "minutes",           "teal",    "🔄")
        + kpi("Probability of Waiting", f"{probability_wait:.1%}", "of students wait", "amber", "📊")
        + kpi("Maximum Waiting Time",  max_waiting,      "minutes",           "crimson", "⚠")
        + '</div>'
    )
    row2_html = (
        '<div class="kpi-grid">'
        + kpi("Stress Before CBT",  f"{avg_stress_before:.3f}", "average level",     "crimson", "😟")
        + kpi("Stress After CBT",   f"{avg_stress_after:.3f}",  "average level",     "emerald", "😌")
        + kpi("Stress Reduction",   f"{avg_stress_red:.3f}",    f"CBT power {cbt_power}", "teal", "📉")
        + kpi("Active Counselors",  counselors,                 "in simulation",     "royal",   "👨‍⚕️")
        + '</div>'
    )
    st.markdown(row1_html + row2_html, unsafe_allow_html=True)

    summary_df = pd.DataFrame({
        "Indicator": [
            "Number of Students", "Number of Counselors",
            "Avg Waiting Time (min)", "Max Waiting Time (min)",
            "Avg Service Time (min)", "Avg Counselor Idle Time (min)",
            "Probability of Waiting", "Avg Stress Before CBT",
            "Avg Stress After CBT", "Avg Stress Reduction", "CBT Power",
        ],
        "Value": [
            n_students, counselors, avg_waiting, max_waiting,
            avg_service, avg_idle, f"{probability_wait:.2%}",
            avg_stress_before, avg_stress_after, avg_stress_red, cbt_power,
        ]
    })

    # ── Charts ────────────────────────────────
    sec(3, "Simulation Visualizations")

    arr = result["Student"].values
    if n_students > 600:
        idx_s  = np.linspace(0, n_students - 1, 600, dtype=int)
        s_arr  = arr[idx_s]
        sb_arr = result["Stress Before CBT"].values[idx_s]
        sa_arr = result["Stress After CBT"].values[idx_s]
        wt_arr = result["Waiting Time"].values[idx_s]
        note   = f" · sampled {600}/{n_students:,}"
    else:
        s_arr  = arr
        sb_arr = result["Stress Before CBT"].values
        sa_arr = result["Stress After CBT"].values
        wt_arr = result["Waiting Time"].values
        note   = ""

    c1, c2 = st.columns(2)
    with c1:
        chart("Stress Level Comparison",
              f"Before vs. After CBT Intervention{note}",
              make_svg_line(s_arr, sb_arr, sa_arr,
                            "Before CBT", "After CBT", "#c0392b", "#27ae60"))
    with c2:
        chart("Waiting Time Distribution",
              f"Per-student waiting time in minutes{note}",
              make_svg_bar([str(int(x)) for x in s_arr],
                           wt_arr.tolist(), "#1a3a6b", "#3b7dd8"))

    c3, c4 = st.columns(2)
    with c3:
        wl = result.groupby("Counselor")["Service Time"].sum()
        chart("Counselor Workload",
              "Total service time allocated per counselor",
              make_svg_bar([f"C{c}" for c in wl.index],
                           wl.values.tolist(), "#0d7377", "#22c9be"))
    with c4:
        red_arr = (result["Stress Before CBT"] - result["Stress After CBT"]).values
        chart("Stress Reduction Distribution",
              "Histogram of CBT-induced stress reduction per student",
              make_svg_hist(red_arr, bins=25, color="#1a6b3a", mean_color="#b8860b"))

    # ── Tables ────────────────────────────────
    sec(4, "Data Tables")

    COLS = ["Student", "Interarrival Time", "Arrival Time", "Service Time",
            "Service Begins", "Service Ends", "Waiting Time",
            "Counselor Idle Time", "Counselor",
            "Stress Before CBT", "Stress After CBT", "Resilience"]

    tab1, tab2, tab3 = st.tabs(["📥  Input Dataset", "📤  Simulation Result", "📑  Summary"])
    with tab1: st.dataframe(dataset, use_container_width=True, height=340)
    with tab2: st.dataframe(result[COLS], use_container_width=True, height=340)
    with tab3: st.dataframe(summary_df, use_container_width=True)

    # ── Export ────────────────────────────────
    sec(5, "Export Results")

    e1, e2 = st.columns(2)
    csv_bytes = result[COLS].to_csv(index=False).encode("utf-8")
    with e1:
        st.download_button(
            "⬇  Download Simulation Result (CSV)",
            data=csv_bytes,
            file_name=f"counselingq_result_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv",
            use_container_width=True)

    pdf_bytes, ext = try_fpdf(summary_df, avg_waiting, counselors, probability_wait)
    mime_lut = {"pdf": "application/pdf", "txt": "text/plain"}
    label    = "PDF" if ext == "pdf" else "TXT"
    with e2:
        st.download_button(
            f"⬇  Download Summary Report ({label})",
            data=pdf_bytes,
            file_name=f"counselingq_report_{datetime.now().strftime('%Y%m%d_%H%M')}.{ext}",
            mime=mime_lut[ext],
            use_container_width=True)

    # ── Monte Carlo ───────────────────────────
    sec(6, "Monte Carlo Analysis")

    mc_n = min(n_students, 200)
    with st.spinner(f"Running {monte_carlo_runs} Monte Carlo iterations…"):
        mc_rows = []
        for _ in range(monte_carlo_runs):
            d = generate_dataset(mc_n)
            r = CounselingQueueSimulation(d, cbt_power=cbt_power, counselors=counselors).run()
            mc_rows.append({
                "Avg Wait (min)":       round(float(r["Waiting Time"].mean()), 3),
                "P(Waiting)":           round(float((r["Waiting Time"] > 0).mean()), 4),
                "Avg Service (min)":    round(float(r["Service Time"].mean()), 3),
                "Avg Stress Reduction": round(float((r["Stress Before CBT"] - r["Stress After CBT"]).mean()), 4),
            })

    mc_df = pd.DataFrame(mc_rows)

    if n_students > 200:
        st.info(f"ℹ️  Monte Carlo uses {mc_n} students per iteration (performance cap). "
                f"Main simulation ran the full {n_students:,} students.")

    mc1, mc2 = st.columns(2)
    with mc1:
        st.markdown("**Descriptive Statistics**")
        st.dataframe(mc_df.describe().round(4), use_container_width=True)
    with mc2:
        chart("Waiting Time Distribution  (Monte Carlo)",
              f"Across {monte_carlo_runs} iterations · {mc_n} students each",
              make_svg_hist(mc_df["Avg Wait (min)"].values, bins=20,
                            color="#1a3a6b", mean_color="#b8860b"))

    chart("Service Time vs. Waiting Time  (Monte Carlo)",
          "Per-iteration averages across all simulation runs",
          make_svg_line(
              np.arange(1, len(mc_df) + 1),
              mc_df["Avg Service (min)"].values,
              mc_df["Avg Wait (min)"].values,
              "Avg Service", "Avg Wait", "#2454a4", "#0d7377"))

    # ── AI Recommendation ─────────────────────
    sec(7, "System Recommendation")

    if avg_waiting > 20 or probability_wait > 0.60:
        sc, ico, head = "warn", "⚠️", "System Overloaded"
        body = (f"Average waiting time is <strong>{avg_waiting} minutes</strong> and "
                f"<strong>{probability_wait:.1%}</strong> of students experience queuing delays. "
                f"It is recommended to increase the number of active counselors to "
                f"<strong>{counselors + 1}</strong> to reduce queue pressure and improve service quality.")
    elif avg_waiting < 5 and probability_wait < 0.30:
        sc, ico, head = "ok", "✅", "System Operating Efficiently"
        body = (f"Queue performance is excellent — only <strong>{probability_wait:.1%}</strong> of "
                f"students experience waiting, with an average delay of just "
                f"<strong>{avg_waiting} minutes</strong>. The current allocation of "
                f"<strong>{counselors}</strong> counselor(s) is well-calibrated for this demand.")
    else:
        sc, ico, head = "info", "ℹ️", "System at Moderate Load"
        body = (f"The system is operating at moderate capacity — average wait is "
                f"<strong>{avg_waiting} minutes</strong> with a "
                f"<strong>{probability_wait:.1%}</strong> probability of queuing. "
                "Current resource allocation is acceptable; close monitoring during peak periods is advised.")

    st.markdown(
        f'<div class="rec-panel {sc}">'
        f'<div class="rec-ico">{ico}</div>'
        f'<div><div class="rec-head">{head}</div>'
        f'<p class="rec-body">{body}</p></div>'
        f'</div>', unsafe_allow_html=True)

    # Footer
    st.markdown(
        f'<div class="footer-strip">'
        f'<span><strong>CounselingQ</strong>  ·  Academic Queue Simulation System</span>'
        f'<span>HKI Research Edition  ·  {datetime.now().strftime("%d %B %Y")}</span>'
        f'</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════
# EMPTY STATE
# ══════════════════════════════════════════════

else:
    st.markdown("""
    <div class="empty-state">
        <span class="empty-icon">🎓</span>
        <div class="empty-title">Ready to Simulate</div>
        <div class="empty-desc">
            Configure the simulation parameters in the sidebar panel,
            then click <strong>Run Simulation</strong> to begin —
            or upload your own CSV dataset for analysis.
        </div>
        <div class="feature-grid">
            <div class="feature-tile">
                <div class="feature-ico">👥</div>
                <div class="feature-name">Up to 5,000 students</div>
            </div>
            <div class="feature-tile">
                <div class="feature-ico">🧘</div>
                <div class="feature-name">CBT stress model</div>
            </div>
            <div class="feature-tile">
                <div class="feature-ico">🎲</div>
                <div class="feature-name">Monte Carlo analysis</div>
            </div>
            <div class="feature-tile">
                <div class="feature-ico">📊</div>
                <div class="feature-name">Queue KPI metrics</div>
            </div>
            <div class="feature-tile">
                <div class="feature-ico">💾</div>
                <div class="feature-name">CSV + PDF export</div>
            </div>
            <div class="feature-tile">
                <div class="feature-ico">🤖</div>
                <div class="feature-name">AI recommendation</div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)