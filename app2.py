# -*- coding: utf-8 -*-
"""
Aplikasi Streamlit satu file untuk:
Simulasi Sistem Antrian Layanan Konseling Mahasiswa Menggunakan Agent Based Modeling
untuk Analisis Waktu Tunggu dan Efisiensi Sistem.

Login demo:
- Username: admin
- Password: 123456
"""


# ============================================================
# style.py
# ============================================================
import streamlit as st

def apply_style():

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

# ============================================================
# sim_engine.py
# ============================================================
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ══════════════════════════════════════════════
# KONFIGURASI WAKTU
# ══════════════════════════════════════════════

START_TIME = datetime.strptime("08:00", "%H:%M")

def to_clock(minutes):
    return (START_TIME + timedelta(minutes=int(minutes))).strftime("%H:%M")


# ══════════════════════════════════════════════
# STUDENT AGENT
# ══════════════════════════════════════════════

class StudentAgent:
    """
    StudentAgent merepresentasikan mahasiswa sebagai agent.
    Setiap mahasiswa memiliki atribut dan perilaku individual:
    - waktu kedatangan
    - tingkat stres awal
    - resilience
    - prioritas risiko
    - toleransi waktu tunggu
    - peningkatan stres saat menunggu
    - perubahan stres setelah CBT
    """

    def __init__(self, row, stress_growth_rate=0.002):
        self.student_id = int(row["Student"])
        self.interarrival_time = float(row["Interarrival Time"])
        self.stress_before = float(row["Stress Before CBT"])
        self.current_stress = float(row["Stress Before CBT"])
        self.resilience = float(row["Resilience"])
        self.stress_growth_rate = float(stress_growth_rate)

        self.arrival_minutes = 0.0
        self.service_begin = 0.0
        self.service_end = 0.0
        self.waiting_time = 0.0
        self.service_time = 0
        self.counselor_idle_time = 0.0
        self.assigned_counselor = None

        self.stress_after = self.stress_before
        self.priority_score = self.calculate_priority()
        self.max_tolerance = self.calculate_wait_tolerance()

        self.status = "menunggu"
        self.left_queue = False

    def calculate_priority(self):
        """
        Mahasiswa dengan stres tinggi dan resilience rendah
        memiliki prioritas risiko lebih tinggi.
        """
        risk_score = (self.stress_before * 0.7) + ((1 - self.resilience) * 0.3)
        return round(risk_score, 4)

    def calculate_wait_tolerance(self):
        """
        Toleransi menunggu dipengaruhi oleh resilience dan stres awal.
        Resilience tinggi membuat mahasiswa lebih mampu menunggu.
        """
        tolerance = 25 + (self.resilience * 45) - (self.stress_before * 15)
        return max(10, round(tolerance, 2))

    def update_stress_while_waiting(self, waiting_minutes):
        """
        Perilaku adaptif mahasiswa:
        semakin lama menunggu, stres dapat meningkat.
        """
        stress_increase = waiting_minutes * self.stress_growth_rate * (1 - self.resilience)
        self.current_stress = min(1.0, round(self.stress_before + stress_increase, 4))

    def decide_to_leave_queue(self, waiting_minutes):
        """
        Mahasiswa dapat batal antri jika waktu tunggu melebihi toleransi.
        Keputusan ini membuat skenario lebih sesuai dengan ABM.
        """
        if waiting_minutes > self.max_tolerance:
            leave_probability = min(0.35, (waiting_minutes - self.max_tolerance) / 100)
            if leave_probability > 0.25:
                self.left_queue = True
                self.status = "batal antri"
        return self.left_queue

    def calculate_service_time(self, counselor_fatigue=0.0):
        """
        Waktu layanan dipengaruhi stres terkini, prioritas risiko,
        dan fatigue konselor.
        """
        base_time = 20 + (self.current_stress * 35)
        priority_adjustment = self.priority_score * 5
        fatigue_adjustment = counselor_fatigue * 6
        self.service_time = int(round(base_time + priority_adjustment + fatigue_adjustment))
        return self.service_time

    def receive_cbt(self, cbt_power):
        """
        Perilaku mahasiswa setelah menerima layanan CBT.
        CBT menurunkan stres berdasarkan resilience dan efektivitas CBT.
        """
        reduction = self.resilience * cbt_power
        self.stress_after = round(max(0.0, self.current_stress - reduction), 4)
        self.status = "selesai dilayani"


# ══════════════════════════════════════════════
# COUNSELOR AGENT
# ══════════════════════════════════════════════

class CounselorAgent:
    """
    CounselorAgent merepresentasikan konselor sebagai agent.
    Konselor memiliki:
    - waktu tersedia
    - total pelayanan
    - idle time
    - jumlah mahasiswa dilayani
    - fatigue akibat beban layanan
    """

    def __init__(self, counselor_id):
        self.counselor_id = counselor_id
        self.available_time = 0.0
        self.total_service_time = 0.0
        self.total_idle_time = 0.0
        self.students_served = 0
        self.fatigue = 0.0
        self.status = "tersedia"

    def update_fatigue(self):
        """
        Fatigue meningkat sesuai jumlah mahasiswa yang dilayani,
        tetapi dibatasi agar tidak terlalu besar.
        """
        self.fatigue = min(1.0, self.students_served * 0.015)

    def serve_student(self, student):
        """
        Interaksi utama antara CounselorAgent dan StudentAgent.
        Konselor melayani mahasiswa, menghitung waktu tunggu,
        idle time, service time, dan memperbarui status agent.
        """
        idle_time = max(0.0, student.arrival_minutes - self.available_time)
        service_begin = max(student.arrival_minutes, self.available_time)
        waiting_time = service_begin - student.arrival_minutes

        student.update_stress_while_waiting(waiting_time)
        student.decide_to_leave_queue(waiting_time)

        # Dalam layanan konseling, mahasiswa prioritas tetap dilayani
        # meskipun melewati toleransi, agar output simulasi tetap lengkap.
        student.left_queue = False
        student.status = "sedang dilayani"

        self.update_fatigue()
        service_time = student.calculate_service_time(self.fatigue)
        service_end = service_begin + service_time

        student.service_begin = service_begin
        student.service_end = service_end
        student.waiting_time = waiting_time
        student.counselor_idle_time = idle_time
        student.assigned_counselor = self.counselor_id

        self.available_time = service_end
        self.total_service_time += service_time
        self.total_idle_time += idle_time
        self.students_served += 1
        self.update_fatigue()
        self.status = "sibuk"

        return student


# ══════════════════════════════════════════════
# COUNSELING ENVIRONMENT
# ══════════════════════════════════════════════

class CounselingEnvironment:
    """
    CounselingEnvironment adalah lingkungan ABM.
    Environment mengatur:
    - pembentukan agent mahasiswa
    - agent konselor
    - aturan kedatangan
    - aturan pemilihan konselor
    - interaksi agent
    - pencatatan hasil simulasi
    """

    def __init__(self, dataset, cbt_power=0.5, counselors=1):
        self.dataset = dataset.copy().reset_index(drop=True)
        self.cbt_power = float(cbt_power)
        self.counselor_count = int(counselors)

        self.student_agents = []
        self.counselor_agents = [
            CounselorAgent(counselor_id=i + 1)
            for i in range(self.counselor_count)
        ]

    def create_student_agents(self):
        """
        Membuat StudentAgent dari dataset dan menghitung arrival time.
        """
        arrival_minutes = 0.0
        agents = []

        for idx, row in self.dataset.iterrows():
            student = StudentAgent(row)

            if idx == 0:
                arrival_minutes = 0.0
            else:
                arrival_minutes += student.interarrival_time

            student.arrival_minutes = arrival_minutes
            agents.append(student)

        self.student_agents = agents

    def choose_counselor(self, student):
        """
        Aturan keputusan environment:
        mahasiswa diarahkan ke konselor yang paling cepat tersedia.
        Jika ada kondisi sama, konselor dengan fatigue lebih rendah dipilih.
        """
        return min(
            self.counselor_agents,
            key=lambda c: (c.available_time, c.fatigue, c.students_served)
        )

    def run(self):
        """
        Menjalankan simulasi ABM berdasarkan interaksi agent.
        """
        self.create_student_agents()

        # Agent dengan prioritas tinggi tetap datang sesuai urutan waktu,
        # tetapi priority_score digunakan untuk memengaruhi service time.
        for student in self.student_agents:
            counselor = self.choose_counselor(student)
            counselor.serve_student(student)
            student.receive_cbt(self.cbt_power)

        return self.to_dataframe()

    def to_dataframe(self):
        """
        Mengubah hasil interaksi agent menjadi dataframe.
        Format kolom tetap disesuaikan dengan dashboard utama.
        """
        out = self.dataset.copy()

        out["Arrival Time"] = [to_clock(s.arrival_minutes) for s in self.student_agents]
        out["Service Begins"] = [to_clock(s.service_begin) for s in self.student_agents]
        out["Service Ends"] = [to_clock(s.service_end) for s in self.student_agents]

        out["Arrival Minutes"] = [s.arrival_minutes for s in self.student_agents]
        out["Service Time"] = [s.service_time for s in self.student_agents]
        out["Service Begin Minutes"] = [s.service_begin for s in self.student_agents]
        out["Service End Minutes"] = [s.service_end for s in self.student_agents]

        out["Waiting Time"] = [s.waiting_time for s in self.student_agents]
        out["Counselor Idle Time"] = [s.counselor_idle_time for s in self.student_agents]
        out["Counselor"] = [s.assigned_counselor for s in self.student_agents]
        out["Stress After CBT"] = [s.stress_after for s in self.student_agents]

        # Kolom tambahan khusus ABM
        out["Priority Score"] = [s.priority_score for s in self.student_agents]
        out["Wait Tolerance"] = [s.max_tolerance for s in self.student_agents]
        out["Current Stress"] = [s.current_stress for s in self.student_agents]
        out["Agent Status"] = [s.status for s in self.student_agents]

        return out


# Nama class tetap dipertahankan agar kompatibel dengan app.py
class CounselingQueueSimulation(CounselingEnvironment):
    pass


# ══════════════════════════════════════════════
# DATASET GENERATOR
# ══════════════════════════════════════════════

def generate_dataset(n):
    """
    Membuat dataset agent mahasiswa secara otomatis.
    Setiap baris data akan menjadi satu StudentAgent.
    """
    rng = np.random.default_rng()

    return pd.DataFrame({
        "Student": range(1, n + 1),
        "Interarrival Time": rng.integers(10, 60, n).astype(int),
        "Stress Before CBT": np.round(rng.uniform(0.40, 0.95, n), 3),
        "Resilience": np.round(rng.uniform(0.15, 0.60, n), 3),
    })


# ============================================================
# export_utils.py
# ============================================================
from datetime import datetime
import io

# ══════════════════════════════════════════════
# EXPORT LAPORAN
# ══════════════════════════════════════════════

def export_summary_txt(summary_df, avg_waiting, counselors, probability_wait):
    ts = datetime.now().strftime("%d %B %Y  %H:%M")
    sep = "-" * 52
    lines = [
        "LAPORAN SIMULASI ANTRIAN KONSELING MAHASISWA",
        f"Dibuat pada : {ts}",
        sep, "",
        "RINGKASAN SIMULASI", "",
    ]

    for _, row in summary_df.iterrows():
        lines.append(f"  {row['Indikator']:<40} {row['Nilai']}")

    lines += ["", sep, "", "REKOMENDASI SISTEM", ""]

    if avg_waiting > 20 or probability_wait > 0.60:
        lines.append(f"  Sistem padat. Disarankan menambah jumlah konselor menjadi {counselors + 1}.")
    elif avg_waiting < 5 and probability_wait < 0.30:
        lines.append("  Sistem efisien. Jumlah konselor saat ini sudah sesuai.")
    else:
        lines.append("  Sistem berada pada beban sedang. Lakukan pemantauan pada jam sibuk.")

    lines += [
        "", sep,
        "Simulasi Antrian Konseling Mahasiswa Berbasis Agent Based Modeling",
        "Dikembangkan untuk kebutuhan penelitian akademik."
    ]

    return "\n".join(lines).encode("utf-8")


def _safe(text):
    text = str(text)
    replacements = {
        "\u2014": "-",
        "\u2013": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2026": "...",
        "\u00d7": "x",
        "\u2022": "*",
        "\u2265": ">=",
        "\u2264": "<=",
        "\u2713": "OK",
        "\u26a0": "!",
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text.encode("latin-1", errors="replace").decode("latin-1")


def try_fpdf(summary_df, avg_waiting, counselors, probability_wait):
    try:
        from fpdf import FPDF

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=18)

        pdf.set_fill_color(26, 58, 107)
        pdf.rect(0, 0, 210, 28, "F")
        pdf.set_font("Arial", "B", 14)
        pdf.set_text_color(255, 255, 255)
        pdf.set_y(8)
        pdf.cell(0, 10, _safe("Laporan Simulasi Antrian Konseling Mahasiswa"), align="C", ln=True)

        pdf.set_font("Arial", "", 8)
        pdf.set_text_color(180, 200, 220)
        pdf.cell(
            0, 6,
            _safe(f"Agent Based Modeling | {datetime.now().strftime('%d %B %Y  %H:%M')}"),
            align="C", ln=True
        )
        pdf.ln(10)

        pdf.set_font("Arial", "B", 11)
        pdf.set_text_color(15, 25, 35)
        pdf.cell(0, 8, _safe("Ringkasan Simulasi"), ln=True)
        pdf.set_draw_color(220, 232, 240)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(3)

        indicator_col = "Indikator" if "Indikator" in summary_df.columns else "Indicator"
        value_col = "Nilai" if "Nilai" in summary_df.columns else "Value"

        for idx, (_, row) in enumerate(summary_df.iterrows()):
            if idx % 2 == 0:
                pdf.set_fill_color(240, 245, 249)
                pdf.rect(10, pdf.get_y(), 190, 7, "F")

            pdf.set_font("Arial", "B", 8.5)
            pdf.set_text_color(74, 96, 128)
            pdf.cell(100, 7, _safe(f"  {row[indicator_col]}"))

            pdf.set_font("Arial", "", 8.5)
            pdf.set_text_color(15, 25, 35)
            pdf.cell(0, 7, _safe(str(row[value_col])), ln=True)

        pdf.ln(6)
        pdf.set_font("Arial", "B", 11)
        pdf.set_text_color(15, 25, 35)
        pdf.cell(0, 8, _safe("Rekomendasi Sistem"), ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(3)

        pdf.set_font("Arial", "", 9)
        pdf.set_text_color(74, 96, 128)

        if avg_waiting > 20 or probability_wait > 0.60:
            msg = (
                f"Sistem berada pada kondisi padat. Rata-rata waktu tunggu adalah "
                f"{avg_waiting} menit dengan probabilitas menunggu {probability_wait:.1%}. "
                f"Disarankan menambah jumlah konselor menjadi {counselors + 1}."
            )
        elif avg_waiting < 5 and probability_wait < 0.30:
            msg = (
                f"Sistem berjalan efisien. Rata-rata waktu tunggu hanya {avg_waiting} menit "
                f"dengan probabilitas menunggu {probability_wait:.1%}. "
                f"Jumlah {counselors} konselor sudah cukup untuk kondisi simulasi ini."
            )
        else:
            msg = (
                f"Sistem berada pada beban sedang. Rata-rata waktu tunggu adalah "
                f"{avg_waiting} menit dengan probabilitas menunggu {probability_wait:.1%}. "
                "Jumlah konselor saat ini masih dapat digunakan, tetapi perlu dipantau saat jam sibuk."
            )

        pdf.multi_cell(0, 6.5, _safe(msg))

        pdf.set_y(-20)
        pdf.set_draw_color(220, 232, 240)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(2)
        pdf.set_font("Arial", "", 7.5)
        pdf.set_text_color(140, 155, 170)
        pdf.cell(
            0, 5,
            _safe("Simulasi Antrian Konseling Mahasiswa Berbasis Agent Based Modeling"),
            align="C"
        )

        try:
            raw = pdf.output(dest="S")
            if isinstance(raw, str):
                return raw.encode("latin-1"), "pdf"
            return raw, "pdf"
        except Exception:
            buf = io.BytesIO()
            pdf.output(buf)
            return buf.getvalue(), "pdf"

    except ImportError:
        return export_summary_txt(summary_df, avg_waiting, counselors, probability_wait), "txt"


# ============================================================
# svg_charts.py
# ============================================================
import numpy as np

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

# ============================================================
# ui_helpers.py
# ============================================================
import streamlit as st

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

# ============================================================
# app.py - APLIKASI UTAMA
# ============================================================
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time


st.set_page_config(
    page_title="Simulasi Antrian Konseling Mahasiswa",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_style()

# ══════════════════════════════════════════════
# LOGIN
# ══════════════════════════════════════════════

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown("""
    <div style="text-align:center;padding:3rem 0 1rem;">
        <div class="login-logo">🎓</div>
        <div class="login-title">Konseling Mahasiswa</div>
        <div class="login-sub">Simulasi Antrian Berbasis Agent Based Modeling</div>
    </div>""", unsafe_allow_html=True)

    _, col, _ = st.columns([1, 1.1, 1])
    with col:
        username = st.text_input("Nama Pengguna", placeholder="Masukkan nama pengguna")
        password = st.text_input("Kata Sandi", type="password", placeholder="Masukkan kata sandi")

        if st.button("Masuk →", use_container_width=True):
            if username.lower() == "admin" and password == "123456":
                st.session_state.login = True
                st.rerun()
            else:
                st.error("Nama pengguna atau kata sandi salah.")

        st.markdown(
            '<div style="text-align:center;margin-top:.8rem;font-family:\'IBM Plex Mono\',monospace;'
            'font-size:.65rem;color:#6b849e;letter-spacing:.06em;">DEMO · admin / 123456</div>',
            unsafe_allow_html=True
        )
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
                <div class="sb-logo-text">Simulasi Konseling</div>
                <div class="sb-logo-ver">ABM · Progress 3</div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="div-label">Parameter ABM</div>', unsafe_allow_html=True)
    total_students = st.slider("Jumlah Mahasiswa", 10, 5000, 50, step=10)
    cbt_power = st.slider("Efektivitas CBT", 0.10, 1.00, 0.50, step=0.05)
    counselors = st.slider("Jumlah Konselor", 1, 20, 1)
    monte_carlo_runs = st.slider("Jumlah Iterasi Monte Carlo", 10, 500, 100, step=10)

    st.markdown('<div class="div-label">Dataset</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Unggah Dataset CSV",
        type=["csv"],
        help="Kolom wajib: Student, Interarrival Time, Stress Before CBT, Resilience"
    )

    st.markdown('<div class="div-label">Aksi</div>', unsafe_allow_html=True)
    generate_button = st.button("▶ Jalankan Simulasi", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Keluar", use_container_width=True):
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
            <div class="masthead-brand">Simulasi Antrian Konseling Mahasiswa</div>
            <div class="masthead-sub">Agent Based Modeling untuk Analisis Waktu Tunggu dan Efisiensi Sistem</div>
        </div>
    </div>
    <div class="masthead-badge">Mukhamad Sofyan · {datetime.now().strftime("%Y")}</div>
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════

st.markdown("""
<div class="page-hero">
    <div>
        <div class="hero-eyebrow">Dashboard Simulasi</div>
        <div class="hero-h1">Agent Based Modeling<br>Antrian Konseling Mahasiswa</div>
        <div class="hero-desc">
            Model simulasi layanan konseling mahasiswa menggunakan Agent Based Modeling,
            dengan mahasiswa sebagai agent penerima layanan, konselor sebagai agent pelayanan,
            dan environment sebagai pengatur proses antrian, CBT, waktu tunggu, serta efisiensi sistem.
        </div>
    </div>
    <div class="hero-meta">
        <span class="hero-tag blue">Agent Based Modeling</span>
        <span class="hero-tag teal">Analisis Waktu Tunggu</span>
        <span class="hero-tag amber">Efisiensi Sistem</span>
    </div>
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# MAIN FLOW
# ══════════════════════════════════════════════

if generate_button or uploaded_file is not None:

    # Dataset
    if uploaded_file is not None:
        dataset = pd.read_csv(uploaded_file)
        required = ["Student", "Interarrival Time", "Stress Before CBT", "Resilience"]
        missing = [c for c in required if c not in dataset.columns]

        if missing:
            st.error(f"Kolom dataset belum lengkap: {missing}")
            st.stop()

        dataset = dataset[required].reset_index(drop=True)
        st.success(f"Dataset berhasil diunggah — {len(dataset):,} mahasiswa dimuat")
    else:
        with st.spinner("Membuat dataset agent mahasiswa..."):
            dataset = generate_dataset(total_students)

    n_students = len(dataset)

    # Eksekusi simulasi
    sec(1, "Eksekusi Simulasi ABM")
    prog = st.progress(0)
    stat = st.empty()

    model = CounselingQueueSimulation(dataset, cbt_power=cbt_power, counselors=counselors)
    result = model.run()

    batch = max(1, n_students // 40)
    for i in range(0, n_students, batch):
        idx = min(i, n_students - 1)
        prog.progress((idx + 1) / n_students)

        if i % max(1, batch * 5) == 0:
            stat.markdown(
                f'<div class="prog-line">'
                f'[{idx + 1:>5,} / {n_students:,}] '
                f'Konselor {result.loc[idx, "Counselor"]} · '
                f'{result.loc[idx, "Service Begins"]} → {result.loc[idx, "Service Ends"]}'
                f'</div>',
                unsafe_allow_html=True
            )

        if n_students <= 200:
            time.sleep(0.01)

    prog.progress(1.0)
    stat.markdown(
        '<span class="status-pill ok">✓ Simulasi ABM Selesai</span>',
        unsafe_allow_html=True
    )

    # Metrik
    avg_waiting = round(result["Waiting Time"].mean(), 2)
    avg_service = round(result["Service Time"].mean(), 2)
    avg_idle = round(result["Counselor Idle Time"].mean(), 2)
    probability_wait = round((result["Waiting Time"] > 0).mean(), 4)
    avg_stress_before = round(result["Stress Before CBT"].mean(), 4)
    avg_stress_after = round(result["Stress After CBT"].mean(), 4)
    avg_stress_red = round(avg_stress_before - avg_stress_after, 4)
    max_waiting = int(result["Waiting Time"].max())
    avg_priority = round(result["Priority Score"].mean(), 4) if "Priority Score" in result else 0
    avg_tolerance = round(result["Wait Tolerance"].mean(), 2) if "Wait Tolerance" in result else 0

    sec(2, "Indikator Kinerja Utama")

    row1_html = (
        '<div class="kpi-grid">'
        + kpi("Rata-rata Waktu Tunggu", avg_waiting, "menit", "royal", "⏱")
        + kpi("Rata-rata Waktu Layanan", avg_service, "menit", "teal", "🔄")
        + kpi("Probabilitas Menunggu", f"{probability_wait:.1%}", "mahasiswa menunggu", "amber", "📊")
        + kpi("Waktu Tunggu Maksimum", max_waiting, "menit", "crimson", "⚠")
        + '</div>'
    )

    row2_html = (
        '<div class="kpi-grid">'
        + kpi("Stres Sebelum CBT", f"{avg_stress_before:.3f}", "rata-rata", "crimson", "😟")
        + kpi("Stres Setelah CBT", f"{avg_stress_after:.3f}", "rata-rata", "emerald", "😌")
        + kpi("Penurunan Stres", f"{avg_stress_red:.3f}", f"CBT {cbt_power}", "teal", "📉")
        + kpi("Jumlah Konselor Aktif", counselors, "agent konselor", "royal", "👨‍⚕️")
        + '</div>'
    )

    row3_html = (
        '<div class="kpi-grid">'
        + kpi("Rata-rata Prioritas Agent", f"{avg_priority:.3f}", "skor risiko", "amber", "🧠")
        + kpi("Rata-rata Toleransi Tunggu", f"{avg_tolerance:.2f}", "menit", "teal", "⌛")
        + kpi("Jumlah Agent Mahasiswa", n_students, "student agent", "royal", "👥")
        + kpi("Metode Simulasi", "ABM", "Agent Based Modeling", "emerald", "🤖")
        + '</div>'
    )

    st.markdown(row1_html + row2_html + row3_html, unsafe_allow_html=True)

    summary_df = pd.DataFrame({
        "Indikator": [
            "Jumlah Mahasiswa",
            "Jumlah Konselor",
            "Rata-rata Waktu Tunggu (menit)",
            "Waktu Tunggu Maksimum (menit)",
            "Rata-rata Waktu Layanan (menit)",
            "Rata-rata Idle Time Konselor (menit)",
            "Probabilitas Menunggu",
            "Rata-rata Stres Sebelum CBT",
            "Rata-rata Stres Setelah CBT",
            "Rata-rata Penurunan Stres",
            "Rata-rata Priority Score Agent",
            "Rata-rata Toleransi Tunggu Agent",
            "Efektivitas CBT",
            "Metode Simulasi",
        ],
        "Nilai": [
            n_students,
            counselors,
            avg_waiting,
            max_waiting,
            avg_service,
            avg_idle,
            f"{probability_wait:.2%}",
            avg_stress_before,
            avg_stress_after,
            avg_stress_red,
            avg_priority,
            avg_tolerance,
            cbt_power,
            "Agent Based Modeling",
        ]
    })

    # Visualisasi
    sec(3, "Visualisasi Hasil Simulasi")

    arr = result["Student"].values
    if n_students > 600:
        idx_s = np.linspace(0, n_students - 1, 600, dtype=int)
        s_arr = arr[idx_s]
        sb_arr = result["Stress Before CBT"].values[idx_s]
        sa_arr = result["Stress After CBT"].values[idx_s]
        wt_arr = result["Waiting Time"].values[idx_s]
        note = f" · sampel {600}/{n_students:,}"
    else:
        s_arr = arr
        sb_arr = result["Stress Before CBT"].values
        sa_arr = result["Stress After CBT"].values
        wt_arr = result["Waiting Time"].values
        note = ""

    c1, c2 = st.columns(2)
    with c1:
        chart(
            "Perbandingan Tingkat Stres",
            f"Sebelum dan setelah intervensi CBT{note}",
            make_svg_line(s_arr, sb_arr, sa_arr, "Sebelum CBT", "Setelah CBT", "#c0392b", "#27ae60")
        )

    with c2:
        chart(
            "Distribusi Waktu Tunggu",
            f"Waktu tunggu setiap mahasiswa dalam menit{note}",
            make_svg_bar([str(int(x)) for x in s_arr], wt_arr.tolist(), "#1a3a6b", "#3b7dd8")
        )

    c3, c4 = st.columns(2)
    with c3:
        wl = result.groupby("Counselor")["Service Time"].sum()
        chart(
            "Beban Kerja Konselor",
            "Total waktu layanan yang diterima setiap konselor",
            make_svg_bar([f"K{c}" for c in wl.index], wl.values.tolist(), "#0d7377", "#22c9be")
        )

    with c4:
        red_arr = (result["Stress Before CBT"] - result["Stress After CBT"]).values
        chart(
            "Distribusi Penurunan Stres",
            "Histogram penurunan stres mahasiswa setelah CBT",
            make_svg_hist(red_arr, bins=25, color="#1a6b3a", mean_color="#b8860b")
        )

    # Tabel
    sec(4, "Tabel Data Simulasi")

    COLS = [
        "Student", "Interarrival Time", "Arrival Time", "Service Time",
        "Service Begins", "Service Ends", "Waiting Time",
        "Counselor Idle Time", "Counselor",
        "Stress Before CBT", "Current Stress", "Stress After CBT",
        "Resilience", "Priority Score", "Wait Tolerance", "Agent Status"
    ]

    existing_cols = [c for c in COLS if c in result.columns]

    tab1, tab2, tab3 = st.tabs([
        "Dataset Input",
        "Hasil Simulasi ABM",
        "Ringkasan"
    ])

    with tab1:
        st.dataframe(dataset, use_container_width=True, height=340)

    with tab2:
        st.dataframe(result[existing_cols], use_container_width=True, height=340)

    with tab3:
        st.dataframe(summary_df, use_container_width=True)

    # Export
    sec(5, "Export Hasil")

    e1, e2 = st.columns(2)
    csv_bytes = result[existing_cols].to_csv(index=False).encode("utf-8")

    with e1:
        st.download_button(
            "⬇ Unduh Hasil Simulasi (CSV)",
            data=csv_bytes,
            file_name=f"hasil_simulasi_abm_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv",
            use_container_width=True
        )

    pdf_bytes, ext = try_fpdf(summary_df, avg_waiting, counselors, probability_wait)
    mime_lut = {"pdf": "application/pdf", "txt": "text/plain"}
    label = "PDF" if ext == "pdf" else "TXT"

    with e2:
        st.download_button(
            f"⬇ Unduh Laporan Ringkasan ({label})",
            data=pdf_bytes,
            file_name=f"laporan_simulasi_abm_{datetime.now().strftime('%Y%m%d_%H%M')}.{ext}",
            mime=mime_lut[ext],
            use_container_width=True
        )

    # Monte Carlo
    sec(6, "Analisis Monte Carlo")

    mc_n = min(n_students, 200)
    with st.spinner(f"Menjalankan {monte_carlo_runs} iterasi Monte Carlo..."):
        mc_rows = []

        for _ in range(monte_carlo_runs):
            d = generate_dataset(mc_n)
            r = CounselingQueueSimulation(d, cbt_power=cbt_power, counselors=counselors).run()

            mc_rows.append({
                "Rata-rata Waktu Tunggu": round(float(r["Waiting Time"].mean()), 3),
                "Probabilitas Menunggu": round(float((r["Waiting Time"] > 0).mean()), 4),
                "Rata-rata Waktu Layanan": round(float(r["Service Time"].mean()), 3),
                "Rata-rata Penurunan Stres": round(float((r["Stress Before CBT"] - r["Stress After CBT"]).mean()), 4),
            })

    mc_df = pd.DataFrame(mc_rows)

    if n_students > 200:
        st.info(
            f"Monte Carlo menggunakan {mc_n} mahasiswa per iterasi untuk menjaga performa. "
            f"Simulasi utama tetap menggunakan {n_students:,} mahasiswa."
        )

    mc1, mc2 = st.columns(2)
    with mc1:
        st.markdown("**Statistik Deskriptif**")
        st.dataframe(mc_df.describe().round(4), use_container_width=True)

    with mc2:
        chart(
            "Distribusi Waktu Tunggu Monte Carlo",
            f"Berdasarkan {monte_carlo_runs} iterasi dengan {mc_n} mahasiswa per iterasi",
            make_svg_hist(mc_df["Rata-rata Waktu Tunggu"].values, bins=20, color="#1a3a6b", mean_color="#b8860b")
        )

    chart(
        "Waktu Layanan vs Waktu Tunggu Monte Carlo",
        "Perbandingan rata-rata per iterasi simulasi",
        make_svg_line(
            np.arange(1, len(mc_df) + 1),
            mc_df["Rata-rata Waktu Layanan"].values,
            mc_df["Rata-rata Waktu Tunggu"].values,
            "Rata-rata Layanan",
            "Rata-rata Tunggu",
            "#2454a4",
            "#0d7377"
        )
    )

    # Rekomendasi
    sec(7, "Rekomendasi Sistem")

    if avg_waiting > 20 or probability_wait > 0.60:
        sc, ico, head = "warn", "⚠️", "Sistem Antrian Padat"
        body = (
            f"Rata-rata waktu tunggu mencapai <strong>{avg_waiting} menit</strong> dan "
            f"<strong>{probability_wait:.1%}</strong> mahasiswa mengalami antrian. "
            f"Berdasarkan hasil simulasi ABM, sistem disarankan menambah jumlah konselor menjadi "
            f"<strong>{counselors + 1}</strong> agar tekanan antrian berkurang."
        )
    elif avg_waiting < 5 and probability_wait < 0.30:
        sc, ico, head = "ok", "✅", "Sistem Berjalan Efisien"
        body = (
            f"Sistem menunjukkan performa baik. Hanya <strong>{probability_wait:.1%}</strong> "
            f"mahasiswa mengalami waktu tunggu dengan rata-rata <strong>{avg_waiting} menit</strong>. "
            f"Jumlah <strong>{counselors}</strong> konselor sudah sesuai untuk skenario ini."
        )
    else:
        sc, ico, head = "info", "ℹ️", "Sistem Berada pada Beban Sedang"
        body = (
            f"Sistem masih berada pada kondisi cukup stabil dengan rata-rata waktu tunggu "
            f"<strong>{avg_waiting} menit</strong> dan probabilitas menunggu "
            f"<strong>{probability_wait:.1%}</strong>. Jumlah konselor saat ini masih dapat digunakan, "
            "tetapi perlu dipantau ketika jumlah mahasiswa meningkat."
        )

    st.markdown(
        f'<div class="rec-panel {sc}">'
        f'<div class="rec-ico">{ico}</div>'
        f'<div><div class="rec-head">{head}</div>'
        f'<p class="rec-body">{body}</p></div>'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="footer-strip">'
        f'<span><strong>Simulasi Antrian Konseling Mahasiswa</strong> · Agent Based Modeling</span>'
        f'<span>Progress 3 · {datetime.now().strftime("%d %B %Y")}</span>'
        f'</div>',
        unsafe_allow_html=True
    )

# ══════════════════════════════════════════════
# EMPTY STATE
# ══════════════════════════════════════════════

else:
    st.markdown("""
    <div class="empty-state">
        <span class="empty-icon">🎓</span>
        <div class="empty-title">Siap Menjalankan Simulasi</div>
        <div class="empty-desc">
            Atur parameter simulasi pada sidebar, lalu klik
            <strong>Jalankan Simulasi</strong> untuk memulai.
            Sistem ini menggunakan Agent Based Modeling untuk menganalisis
            waktu tunggu dan efisiensi layanan konseling mahasiswa.
        </div>
        <div class="feature-grid">
            <div class="feature-tile">
                <div class="feature-ico">👥</div>
                <div class="feature-name">Agent Mahasiswa</div>
            </div>
            <div class="feature-tile">
                <div class="feature-ico">👨‍⚕️</div>
                <div class="feature-name">Agent Konselor</div>
            </div>
            <div class="feature-tile">
                <div class="feature-ico">🧠</div>
                <div class="feature-name">Prioritas Risiko</div>
            </div>
            <div class="feature-tile">
                <div class="feature-ico">📊</div>
                <div class="feature-name">Analisis Waktu Tunggu</div>
            </div>
            <div class="feature-tile">
                <div class="feature-ico">💾</div>
                <div class="feature-name">Export CSV dan PDF</div>
            </div>
            <div class="feature-tile">
                <div class="feature-ico">🤖</div>
                <div class="feature-name">Agent Based Modeling</div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
