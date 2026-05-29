"""
=============================================================================
  Herbek Services — Site Web Vitrine Professionnel (Dark Mode)
  Framework : Streamlit
  Déploiement : Render (via GitHub)
=============================================================================
"""

import streamlit as st
import base64
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration de la page
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Herbek Services — Votre partenaire de confiance",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Constantes de la marque
# ---------------------------------------------------------------------------
BRAND_NAME = "Herbek Services"
SLOGAN = "L'excellence au service de votre réussite"
MISSION = (
    "Fournir des solutions de service professionnelles, fiables et accessibles "
    "qui accompagnent nos clients dans chacune de leurs étapes, avec rigueur, "
    "intégrité et un engagement total envers la satisfaction."
)

WHATSAPP_NUMBER = "243977777737"
PHONE_NUMBER = "+243977777737"
EMAIL_ADDRESS = "contact@herbek-services.com"

# Chemin du logo
LOGO_PATH = Path(__file__).parent / "assets" / "logo.jpg"

# ---------------------------------------------------------------------------
# Initialisation session_state pour les messages du formulaire
# ---------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------------------------------------------
# Fonction pour encoder le logo en base64
# ---------------------------------------------------------------------------
def get_logo_base64() -> str:
    """Lit le logo et le retourne encodé en base64 pour l'affichage HTML."""
    try:
        if LOGO_PATH.exists():
            with open(LOGO_PATH, "rb") as f:
                return base64.b64encode(f.read()).decode("utf-8")
    except Exception:
        pass
    return ""


# ---------------------------------------------------------------------------
# Injection CSS personnalisé — THÈME SOMBRE
# ---------------------------------------------------------------------------
def inject_custom_css():
    st.markdown("""
    <style>
    /* ── Import fonts ─────────────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@700;800;900&display=swap');

    /* ── Dark Theme Variables ─────────────────────────────────────── */
    :root {
        --primary: #3B82F6;
        --primary-light: #60A5FA;
        --primary-dark: #2563EB;
        --accent: #F59E0B;
        --accent-light: #FBBF24;
        --bg-dark: #0F172A;
        --bg-card: #1E293B;
        --bg-card-hover: #334155;
        --bg-input: #1E293B;
        --text-white: #F8FAFC;
        --text-body: #CBD5E1;
        --text-muted: #94A3B8;
        --border-color: #334155;
        --border-light: #475569;
        --shadow-sm: 0 2px 8px rgba(0,0,0,0.3);
        --shadow-md: 0 4px 20px rgba(0,0,0,0.4);
        --shadow-lg: 0 8px 40px rgba(0,0,0,0.5);
        --shadow-glow: 0 0 30px rgba(59,130,246,0.15);
        --radius: 16px;
        --radius-sm: 10px;
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }

    /* ── Streamlit Dark Base Override ─────────────────────────────── */
    .stApp {
        background: var(--bg-dark) !important;
        color: var(--text-body) !important;
    }

    /* ── Hide Streamlit chrome ────────────────────────────────────── */
    #MainMenu, footer { visibility: hidden; height: 0; }

    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 100% !important;
    }

    /* ── Sidebar Styling ──────────────────────────────────────────── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%) !important;
        border-right: 1px solid var(--border-color) !important;
    }

    section[data-testid="stSidebar"] .css-1d391kg {
        background: transparent !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] {
        display: none !important;
    }

    /* ── Sidebar logo area ────────────────────────────────────────── */
    .sidebar-logo {
        text-align: center;
        padding: 1.5rem 1rem 1rem;
        margin-bottom: 0.5rem;
    }

    .sidebar-logo img {
        width: 120px;
        height: 120px;
        border-radius: 20px;
        object-fit: cover;
        border: 3px solid var(--primary);
        box-shadow: 0 0 25px rgba(59,130,246,0.3);
        margin-bottom: 0.8rem;
    }

    .sidebar-logo h2 {
        font-family: 'Playfair Display', serif;
        font-size: 1.2rem;
        font-weight: 800;
        color: var(--text-white);
        margin: 0;
    }

    .sidebar-logo h2 span {
        color: var(--accent);
    }

    .sidebar-logo p {
        font-size: 0.75rem;
        color: var(--text-muted);
        margin: 0.3rem 0 0;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    .sidebar-divider {
        width: 50px;
        height: 3px;
        background: linear-gradient(90deg, var(--primary), var(--accent));
        margin: 1rem auto;
        border-radius: 2px;
    }

    /* ── Sidebar nav buttons ──────────────────────────────────────── */
    .sidebar-nav {
        display: flex;
        flex-direction: column;
        gap: 0.4rem;
        padding: 0 0.5rem;
    }

    .sidebar-nav a {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        padding: 0.75rem 1rem;
        border-radius: var(--radius-sm);
        color: var(--text-body);
        text-decoration: none;
        font-weight: 500;
        font-size: 0.95rem;
        transition: var(--transition);
        border: 1px solid transparent;
    }

    .sidebar-nav a:hover {
        background: var(--bg-card);
        color: var(--text-white);
        border-color: var(--border-color);
        transform: translateX(4px);
    }

    .sidebar-nav a .nav-emoji {
        font-size: 1.2rem;
        width: 28px;
        text-align: center;
    }

    /* ── Sidebar contact buttons ──────────────────────────────────── */
    .sidebar-contact {
        margin-top: 1.5rem;
        padding: 0 0.5rem;
        display: flex;
        flex-direction: column;
        gap: 0.6rem;
    }

    .sidebar-wa-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.6rem;
        background: #25D366;
        color: #FFFFFF !important;
        padding: 0.7rem 1rem;
        border-radius: var(--radius-sm);
        font-weight: 600;
        font-size: 0.9rem;
        text-decoration: none;
        transition: var(--transition);
        box-shadow: 0 4px 15px rgba(37,211,102,0.25);
    }

    .sidebar-wa-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(37,211,102,0.4);
        color: #FFFFFF !important;
    }

    .sidebar-call-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.6rem;
        background: var(--primary);
        color: #FFFFFF !important;
        padding: 0.7rem 1rem;
        border-radius: var(--radius-sm);
        font-weight: 600;
        font-size: 0.9rem;
        text-decoration: none;
        transition: var(--transition);
        box-shadow: 0 4px 15px rgba(59,130,246,0.25);
    }

    .sidebar-call-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(59,130,246,0.4);
        color: #FFFFFF !important;
    }

    .sidebar-phone {
        text-align: center;
        font-size: 0.8rem;
        color: var(--text-muted);
        margin-top: 0.3rem;
    }

    /* ── Hero Section ─────────────────────────────────────────────── */
    .hero {
        min-height: 88vh;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 40%, #0F172A 100%);
        padding: 3rem 2rem;
    }

    .hero::before {
        content: '';
        position: absolute;
        top: -30%;
        right: -15%;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(59,130,246,0.12) 0%, transparent 70%);
        border-radius: 50%;
        animation: float 8s ease-in-out infinite;
    }

    .hero::after {
        content: '';
        position: absolute;
        bottom: -20%;
        left: -10%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(245,158,11,0.08) 0%, transparent 70%);
        border-radius: 50%;
        animation: float 10s ease-in-out infinite reverse;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-30px); }
    }

    @keyframes pulse-glow {
        0%, 100% { box-shadow: 0 0 20px rgba(59,130,246,0.2); }
        50% { box-shadow: 0 0 40px rgba(59,130,246,0.4); }
    }

    .hero-content {
        position: relative;
        z-index: 2;
        text-align: center;
        max-width: 800px;
        margin: 0 auto;
    }

    .hero-logo-wrap {
        margin-bottom: 2rem;
    }

    .hero-logo-wrap img {
        width: 140px;
        height: 140px;
        border-radius: 28px;
        object-fit: cover;
        border: 3px solid var(--primary);
        box-shadow: 0 0 40px rgba(59,130,246,0.3);
        animation: pulse-glow 3s ease-in-out infinite;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(59,130,246,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(59,130,246,0.3);
        border-radius: 50px;
        padding: 0.5rem 1.5rem;
        font-size: 0.85rem;
        color: var(--primary-light);
        font-weight: 600;
        margin-bottom: 1.5rem;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 900;
        color: var(--text-white);
        line-height: 1.1;
        margin-bottom: 1.2rem;
        letter-spacing: -0.02em;
    }

    .hero-title span {
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        color: var(--text-body);
        line-height: 1.7;
        max-width: 600px;
        margin: 0 auto 2.5rem;
        font-weight: 300;
    }

    .hero-actions {
        display: flex;
        gap: 1rem;
        justify-content: center;
        flex-wrap: wrap;
    }

    .btn-primary {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
        color: #FFFFFF;
        padding: 1rem 2.5rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1rem;
        text-decoration: none;
        transition: var(--transition);
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 20px rgba(59,130,246,0.35);
    }

    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(59,130,246,0.5);
    }

    .btn-accent {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%);
        color: #0F172A;
        padding: 1rem 2.5rem;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1rem;
        text-decoration: none;
        transition: var(--transition);
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 20px rgba(245,158,11,0.3);
    }

    .btn-accent:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(245,158,11,0.5);
    }

    .btn-secondary {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(59,130,246,0.1);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(59,130,246,0.3);
        color: var(--primary-light);
        padding: 1rem 2.5rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1rem;
        text-decoration: none;
        transition: var(--transition);
        cursor: pointer;
    }

    .btn-secondary:hover {
        background: rgba(59,130,246,0.2);
        transform: translateY(-2px);
    }

    /* ── Stats Bar ────────────────────────────────────────────────── */
    .stats-bar {
        background: var(--bg-card);
        padding: 3.5rem 2rem;
        display: flex;
        justify-content: center;
        gap: 4rem;
        flex-wrap: wrap;
        border-top: 1px solid var(--border-color);
        border-bottom: 1px solid var(--border-color);
    }

    .stat-item { text-align: center; }

    .stat-number {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 900;
        line-height: 1;
        margin-bottom: 0.5rem;
        color: var(--text-white);
    }

    .stat-number span { color: var(--accent); }

    .stat-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--text-muted);
        font-weight: 500;
    }

    /* ── Section Common ───────────────────────────────────────────── */
    .section { padding: 5rem 2rem; }
    .section-dark { background: var(--bg-dark); }
    .section-card { background: var(--bg-card); }

    .section-inner { max-width: 1200px; margin: 0 auto; }

    .section-header { text-align: center; margin-bottom: 3.5rem; }

    .section-label {
        display: inline-block;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        color: var(--accent);
        margin-bottom: 0.8rem;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.6rem;
        font-weight: 800;
        color: var(--text-white);
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }

    .section-desc {
        font-size: 1.05rem;
        color: var(--text-muted);
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.7;
    }

    /* ── About Section ────────────────────────────────────────────── */
    .about-grid {
        display: grid;
        grid-template-columns: 1fr 1.2fr;
        gap: 4rem;
        align-items: center;
    }

    .about-image-box {
        background: linear-gradient(135deg, var(--bg-card) 0%, #334155 100%);
        border-radius: var(--radius);
        height: 420px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        border: 1px solid var(--border-color);
    }

    .about-image-box img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: var(--radius);
    }

    .about-image-box::before {
        content: '';
        position: absolute;
        top: -20%;
        right: -20%;
        width: 200px;
        height: 200px;
        background: rgba(245,158,11,0.1);
        border-radius: 50%;
    }

    .about-text h3 {
        font-family: 'Playfair Display', serif;
        font-size: 1.9rem;
        color: var(--text-white);
        margin-bottom: 1rem;
    }

    .about-text p {
        font-size: 1rem;
        line-height: 1.8;
        color: var(--text-body);
        margin-bottom: 1.5rem;
    }

    .value-list { list-style: none; padding: 0; margin: 0; }

    .value-list li {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        padding: 0.7rem 0;
        font-size: 0.95rem;
        color: var(--text-body);
        line-height: 1.6;
    }

    .value-list .icon {
        flex-shrink: 0;
        width: 36px;
        height: 36px;
        background: linear-gradient(135deg, var(--primary), var(--primary-dark));
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
    }

    /* ── Service Cards ────────────────────────────────────────────── */
    .services-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
    }

    .service-card {
        background: var(--bg-card);
        border-radius: var(--radius);
        padding: 2.2rem 1.8rem;
        border: 1px solid var(--border-color);
        transition: var(--transition);
        position: relative;
        overflow: hidden;
    }

    .service-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--primary), var(--accent));
        transform: scaleX(0);
        transform-origin: left;
        transition: var(--transition);
    }

    .service-card:hover {
        transform: translateY(-6px);
        border-color: var(--primary);
        box-shadow: var(--shadow-glow);
    }

    .service-card:hover::before { transform: scaleX(1); }

    .service-icon {
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, rgba(59,130,246,0.15) 0%, rgba(96,165,250,0.1) 100%);
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        margin-bottom: 1.3rem;
    }

    .service-card h4 {
        font-size: 1.15rem;
        font-weight: 700;
        color: var(--text-white);
        margin-bottom: 0.7rem;
    }

    .service-card p {
        font-size: 0.9rem;
        color: var(--text-muted);
        line-height: 1.7;
        margin: 0;
    }

    /* ── Why Choose Us ────────────────────────────────────────────── */
    .why-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
    }

    .why-card {
        background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 100%);
        border-radius: var(--radius);
        padding: 2.2rem 1.8rem;
        color: #FFFFFF;
        text-align: center;
        transition: var(--transition);
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(96,165,250,0.2);
    }

    .why-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(59,130,246,0.25);
    }

    .why-card .why-icon {
        font-size: 2.8rem;
        margin-bottom: 1.2rem;
        display: block;
    }

    .why-card h4 {
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.7rem;
    }

    .why-card p {
        font-size: 0.9rem;
        line-height: 1.7;
        color: rgba(255,255,255,0.85);
        margin: 0;
    }

    /* ── Contact Section ──────────────────────────────────────────── */
    .contact-grid {
        display: grid;
        grid-template-columns: 1.2fr 1fr;
        gap: 2.5rem;
    }

    .contact-form-box {
        background: var(--bg-card);
        border-radius: var(--radius);
        padding: 2.2rem;
        border: 1px solid var(--border-color);
    }

    .contact-form-box h3 {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        color: var(--text-white);
        margin-bottom: 1.5rem;
    }

    .contact-info-box {
        display: flex;
        flex-direction: column;
        gap: 1.2rem;
    }

    .contact-link {
        background: var(--bg-card);
        border-radius: var(--radius);
        padding: 1.5rem;
        border: 1px solid var(--border-color);
        display: flex;
        align-items: center;
        gap: 1.2rem;
        transition: var(--transition);
        text-decoration: none;
        color: inherit;
    }

    .contact-link:hover {
        transform: translateY(-2px);
        border-color: var(--primary);
        box-shadow: var(--shadow-glow);
    }

    .contact-link .cl-icon {
        width: 52px;
        height: 52px;
        background: linear-gradient(135deg, var(--primary), var(--primary-dark));
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.4rem;
        flex-shrink: 0;
    }

    .contact-link .cl-text h5 {
        font-size: 1rem;
        font-weight: 700;
        color: var(--text-white);
        margin: 0 0 0.3rem;
    }

    .contact-link .cl-text p {
        font-size: 0.85rem;
        color: var(--text-muted);
        margin: 0;
    }

    /* ── Message display area ─────────────────────────────────────── */
    .message-display {
        background: var(--bg-card);
        border-radius: var(--radius);
        padding: 1.5rem;
        border: 1px solid var(--border-color);
        margin-top: 1.5rem;
        max-height: 400px;
        overflow-y: auto;
    }

    .message-display h4 {
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--text-white);
        margin: 0 0 1rem;
    }

    .msg-item {
        background: var(--bg-dark);
        border-radius: var(--radius-sm);
        padding: 1rem;
        margin-bottom: 0.8rem;
        border-left: 3px solid var(--primary);
    }

    .msg-item .msg-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.5rem;
    }

    .msg-item .msg-name {
        font-weight: 700;
        color: var(--primary-light);
        font-size: 0.9rem;
    }

    .msg-item .msg-date {
        font-size: 0.75rem;
        color: var(--text-muted);
    }

    .msg-item .msg-email {
        font-size: 0.8rem;
        color: var(--text-muted);
        margin-bottom: 0.5rem;
    }

    .msg-item .msg-subject {
        display: inline-block;
        background: rgba(245,158,11,0.15);
        color: var(--accent);
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        margin-bottom: 0.5rem;
    }

    .msg-item .msg-body {
        font-size: 0.9rem;
        color: var(--text-body);
        line-height: 1.6;
        white-space: pre-wrap;
    }

    /* ── Footer ───────────────────────────────────────────────────── */
    .footer {
        background: #070D1A;
        color: rgba(255,255,255,0.5);
        padding: 3rem 2rem 2rem;
        text-align: center;
        border-top: 1px solid var(--border-color);
    }

    .footer-brand {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        font-weight: 800;
        color: var(--text-white);
        margin-bottom: 0.5rem;
    }

    .footer-brand span { color: var(--accent); }

    .footer p { font-size: 0.85rem; margin-bottom: 0.5rem; }

    .footer-links {
        display: flex;
        gap: 2rem;
        justify-content: center;
        margin: 1rem 0;
        flex-wrap: wrap;
    }

    .footer-links a {
        color: var(--text-muted);
        text-decoration: none;
        font-size: 0.85rem;
        transition: var(--transition);
    }

    .footer-links a:hover { color: var(--accent); }

    .footer-divider {
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, var(--primary), var(--accent));
        margin: 1.5rem auto;
        border-radius: 2px;
    }

    .footer-copy {
        font-size: 0.75rem;
        color: rgba(255,255,255,0.3);
    }

    /* ── Streamlit dark overrides ─────────────────────────────────── */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: var(--bg-dark) !important;
        color: var(--text-white) !important;
        border-radius: var(--radius-sm) !important;
        border: 2px solid var(--border-color) !important;
        padding: 0.8rem 1rem !important;
        font-size: 0.95rem !important;
        transition: var(--transition) !important;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(59,130,246,0.15) !important;
    }

    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder {
        color: var(--text-muted) !important;
    }

    .stTextInput > div > label,
    .stTextArea > div > label,
    .stSelectbox > div > label {
        color: var(--text-body) !important;
        font-weight: 500 !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, var(--primary), var(--primary-light)) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 0.8rem 2.5rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: var(--transition) !important;
        box-shadow: 0 4px 15px rgba(59,130,246,0.3) !important;
        width: 100%;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px rgba(59,130,246,0.4) !important;
    }

    .stSelectbox > div > div > div {
        background: var(--bg-dark) !important;
        color: var(--text-white) !important;
        border-radius: var(--radius-sm) !important;
        border: 2px solid var(--border-color) !important;
    }

    .stSelectbox div[data-baseweb="select"] div {
        color: var(--text-white) !important;
    }

    /* ── Success message ──────────────────────────────────────────── */
    .success-msg {
        background: rgba(34,197,94,0.1);
        border-left: 4px solid #22C55E;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        color: #86EFAC;
        font-weight: 500;
        margin-top: 1rem;
    }

    .error-msg {
        background: rgba(239,68,68,0.1);
        border-left: 4px solid #EF4444;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        color: #FCA5A5;
        font-weight: 500;
        margin-top: 1rem;
    }

    /* ── Responsive ───────────────────────────────────────────────── */
    @media (max-width: 768px) {
        .hero-title { font-size: 2rem; }
        .hero-subtitle { font-size: 0.95rem; }
        .hero { padding: 2rem 1.5rem; min-height: 75vh; }
        .section { padding: 3rem 1.5rem; }
        .section-title { font-size: 1.8rem; }
        .about-grid { grid-template-columns: 1fr; gap: 2rem; }
        .about-image-box { height: 250px; }
        .contact-grid { grid-template-columns: 1fr; }
        .stats-bar { gap: 2rem; padding: 2.5rem 1.5rem; }
        .stat-number { font-size: 2.2rem; }
        .hero-logo-wrap img { width: 100px; height: 100px; }
    }

    @media (max-width: 480px) {
        .hero-title { font-size: 1.6rem; }
        .hero-actions { flex-direction: column; align-items: center; }
        .btn-primary, .btn-secondary, .btn-accent { width: 100%; justify-content: center; }
        .services-grid { grid-template-columns: 1fr; }
        .why-grid { grid-template-columns: 1fr; }
    }
    </style>
    """, unsafe_allow_html=True)


# ===========================================================================
#  RENDU DE LA PAGE
# ===========================================================================
inject_custom_css()

logo_b64 = get_logo_base64()

# ── BARRE LATÉRALE AVEC LOGO + NAVIGATION ──────────────────────────────
with st.sidebar:
    # Logo de la marque
    if logo_b64:
        st.markdown(f"""
        <div class="sidebar-logo">
            <img src="data:image/jpeg;base64,{logo_b64}" alt="Herbek Services Logo">
            <h2>Herbek<span> Services</span></h2>
            <p>{SLOGAN}</p>
        </div>
        <div class="sidebar-divider"></div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="sidebar-logo">
            <div style="font-size:3.5rem; margin-bottom:0.5rem;">🤝</div>
            <h2>Herbek<span> Services</span></h2>
            <p>{SLOGAN}</p>
        </div>
        <div class="sidebar-divider"></div>
        """, unsafe_allow_html=True)

    # Navigation
    st.markdown("""
    <div class="sidebar-nav">
        <a href="#accueil"><span class="nav-emoji">🏠</span> Accueil</a>
        <a href="#apropos"><span class="nav-emoji">ℹ️</span> À propos</a>
        <a href="#services"><span class="nav-emoji">🛠️</span> Nos Services</a>
        <a href="#pourquoi"><span class="nav-emoji">🏆</span> Pourquoi nous</a>
        <a href="#contact"><span class="nav-emoji">📩</span> Contact</a>
    </div>
    """, unsafe_allow_html=True)

    # Boutons d'action directs
    st.markdown(f"""
    <div class="sidebar-divider"></div>
    <div class="sidebar-contact">
        <a href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank" class="sidebar-wa-btn">
            💬 WhatsApp
        </a>
        <a href="tel:{PHONE_NUMBER}" class="sidebar-call-btn">
            📞 Appeler
        </a>
        <div class="sidebar-phone">{PHONE_NUMBER}</div>
    </div>
    """, unsafe_allow_html=True)

    # Copyright
    st.markdown(f"""
    <div style="margin-top: 2rem; text-align: center;">
        <div class="sidebar-divider"></div>
        <p style="font-size: 0.7rem; color: var(--text-muted);">
            &copy; {datetime.now().year} {BRAND_NAME}<br>Tous droits réservés
        </p>
    </div>
    """, unsafe_allow_html=True)


# ── SECTION HERO / ACCUEIL ─────────────────────────────────────────────
hero_logo_html = ""
if logo_b64:
    hero_logo_html = f"""
    <div class="hero-logo-wrap">
        <img src="data:image/jpeg;base64,{logo_b64}" alt="Herbek Services">
    </div>"""

st.markdown(f"""
<section class="hero" id="accueil">
    <div class="hero-content">
        {hero_logo_html}
        <div class="hero-badge">Votre partenaire de confiance</div>
        <h1 class="hero-title">{BRAND_NAME}<br><span>{SLOGAN}</span></h1>
        <p class="hero-subtitle">{MISSION}</p>
        <div class="hero-actions">
            <a href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank" class="btn-accent">💬 Nous contacter sur WhatsApp</a>
            <a href="tel:{PHONE_NUMBER}" class="btn-primary">📞 Nous appeler</a>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ── BARRE DE STATISTIQUES ──────────────────────────────────────────────
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-number">500<span>+</span></div>
        <div class="stat-label">Clients satisfaits</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">5<span>+</span></div>
        <div class="stat-label">Années d'expérience</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">98<span>%</span></div>
        <div class="stat-label">Taux de satisfaction</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">24<span>/7</span></div>
        <div class="stat-label">Disponibilité</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION À PROPOS ───────────────────────────────────────────────────
about_image_html = ""
if logo_b64:
    about_image_html = f'<img src="data:image/jpeg;base64,{logo_b64}" alt="Herbek Services">'
else:
    about_image_html = "🤝"

st.markdown(f"""
<section class="section section-dark" id="apropos">
    <div class="section-inner">
        <div class="section-header">
            <div class="section-label">Qui sommes-nous</div>
            <h2 class="section-title">À propos d'Herbek Services</h2>
            <p class="section-desc">Découvrez l'histoire, les valeurs et la vision qui font d'Herbek Services un partenaire incontournable.</p>
        </div>
        <div class="about-grid">
            <div class="about-image-box">{about_image_html}</div>
            <div class="about-text">
                <h3>Un engagement fort, une promesse tenue</h3>
                <p>
                    Herbek Services est une entreprise de services fondée sur la conviction que chaque
                    client mérite une attention particulière, un suivi rigoureux et des résultats concrets.
                    Depuis notre création, nous avons bâti notre réputation sur la fiabilité, la transparence
                    et l'excellence opérationnelle. Notre équipe pluridisciplinaire intervient avec professionnalisme
                    sur chaque projet, en veillant toujours à comprendre vos besoins profonds avant de proposer
                    des solutions adaptées.
                </p>
                <p>
                    Nous croyons qu'un service de qualité n'est pas un luxe mais un droit. C'est pourquoi
                    nous nous efforçons de maintenir des tarifs justes tout en garantissant un niveau de prestation
                    qui dépasse les attentes. Chaque interaction avec Herbek Services est une promesse de sérieux,
                    de ponctualité et de respect des engagements.
                </p>
                <ul class="value-list">
                    <li>
                        <div class="icon">🎯</div>
                        <div><strong>Excellence</strong> — Nous visons la perfection dans chaque prestation, sans compromis sur la qualité.</div>
                    </li>
                    <li>
                        <div class="icon">🤝</div>
                        <div><strong>Intégrité</strong> — La transparence et l'honnêteté sont au cœur de chacune de nos relations.</div>
                    </li>
                    <li>
                        <div class="icon">⚡</div>
                        <div><strong>Réactivité</strong> — Nous intervenons rapidement et efficacement pour répondre à vos urgences.</div>
                    </li>
                    <li>
                        <div class="icon">💡</div>
                        <div><strong>Innovation</strong> — Nous adoptons les meilleures pratiques modernes pour vous servir mieux.</div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ── SECTION NOS SERVICES ───────────────────────────────────────────────
st.markdown("""
<section class="section section-card" id="services">
    <div class="section-inner">
        <div class="section-header">
            <div class="section-label">Ce que nous offrons</div>
            <h2 class="section-title">Nos Services</h2>
            <p class="section-desc">Des solutions complètes et sur mesure pour répondre à tous vos besoins professionnels et personnels.</p>
        </div>
        <div class="services-grid">
            <div class="service-card">
                <div class="service-icon">📋</div>
                <h4>Conseil & Accompagnement</h4>
                <p>Un accompagnement stratégique personnalisé pour vous guider dans vos projets professionnels et entrepreneuriaux. Nous analysons votre situation, identifions les opportunités et vous proposons un plan d'action concret et mesurable.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">💻</div>
                <h4>Solutions Numériques</h4>
                <p>Création de sites web, solutions digitales et transformation numérique pour propulser votre présence en ligne. Nous concevons des outils adaptés à votre secteur d'activité et à votre public cible.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">📊</div>
                <h4>Gestion & Administration</h4>
                <p>Services de gestion administrative, comptable et organisationnelle pour optimiser le fonctionnement de votre entreprise et vous permettre de vous concentrer sur votre cœur de métier.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🎓</div>
                <h4>Formation & Capacitation</h4>
                <p>Programmes de formation adaptés pour développer vos compétences et celles de vos collaborateurs. Des modules pratiques animés par des experts pour un impact durable sur votre performance.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🚚</div>
                <h4>Logistique & Transport</h4>
                <p>Solutions logistiques fiables et efficaces pour le transport de vos marchandises et la gestion de vos flux. Un réseau bien établi pour garantir la ponctualité et la sécurité de vos livraisons.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🔧</div>
                <h4>Services Techniques</h4>
                <p>Interventions techniques spécialisées, maintenance et assistance pour garantir la performance continue de vos installations, équipements et infrastructures techniques.</p>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ── SECTION POURQUOI NOUS CHOISIR ──────────────────────────────────────
st.markdown("""
<section class="section section-dark" id="pourquoi">
    <div class="section-inner">
        <div class="section-header">
            <div class="section-label">Notre différence</div>
            <h2 class="section-title">Pourquoi nous choisir ?</h2>
            <p class="section-desc">Ce qui distingue Herbek Services, c'est un engagement total envers l'excellence et la satisfaction de chaque client.</p>
        </div>
        <div class="why-grid">
            <div class="why-card">
                <span class="why-icon">🕐</span>
                <h4>Disponibilité 24h/7j</h4>
                <p>Nous sommes à vos côtés à tout moment. Que ce soit pour une urgence ou un suivi régulier, notre équipe est joignable et réactive 7 jours sur 7. Votre satisfaction ne prend jamais de vacances.</p>
            </div>
            <div class="why-card">
                <span class="why-icon">🏆</span>
                <h4>Expertise reconnue</h4>
                <p>Des années d'expérience et des centaines de clients satisfaits témoignent de notre savoir-faire. Nous investissons constamment dans la formation de notre équipe pour rester à la pointe des meilleures pratiques.</p>
            </div>
            <div class="why-card">
                <span class="why-icon">😊</span>
                <h4>Satisfaction garantie</h4>
                <p>Votre satisfaction est notre priorité absolue. Nous ne nous arrêtons pas tant que vous n'êtes pas pleinement satisfait du résultat. C'est notre engagement et notre fierté depuis le premier jour.</p>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ── SECTION CONTACT ─────────────────────────────────────────────────────
st.markdown("""
<section class="section section-card" id="contact">
    <div class="section-inner">
        <div class="section-header">
            <div class="section-label">Parlons ensemble</div>
            <h2 class="section-title">Contactez-nous</h2>
            <p class="section-desc">Une question, un projet, un besoin ? Écrivez-nous ou contactez-nous directement via WhatsApp ou téléphone.</p>
        </div>
        <div class="contact-grid">
""", unsafe_allow_html=True)

# Formulaire de contact
with st.container():
    st.markdown('<div class="contact-form-box"><h3>📝 Envoyez-nous un message</h3>', unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Votre nom complet *", placeholder="Ex : Jean Kabongo")
        with col2:
            email = st.text_input("Votre adresse email *", placeholder="Ex : jean@email.com")

        subject = st.selectbox("Objet du message", [
            "Demande d'information",
            "Demande de devis",
            "Partenariat",
            "Réclamation",
            "Autre"
        ])
        message = st.text_area("Votre message *", placeholder="Décrivez votre besoin ou votre question...", height=120)

        submitted = st.form_submit_button("🚀 Envoyer le message")

        if submitted:
            if not name or not email or not message:
                st.markdown('<div class="error-msg">⚠️ Veuillez remplir tous les champs obligatoires (*).</div>', unsafe_allow_html=True)
            else:
                # Stocker le message dans session_state
                st.session_state.messages.append({
                    "name": name,
                    "email": email,
                    "subject": subject,
                    "message": message,
                    "date": datetime.now().strftime("%d/%m/%Y à %H:%M"),
                })
                st.markdown(f"""
                <div class="success-msg">
                    ✅ Merci <strong>{name}</strong> ! Votre message a bien été enregistré.
                    Nous vous répondrons dans les plus brefs délais.
                </div>
                """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Zone d'affichage des messages soumis
if st.session_state.messages:
    msgs_html = ""
    for msg in reversed(st.session_state.messages):
        msgs_html += f"""
        <div class="msg-item">
            <div class="msg-header">
                <span class="msg-name">{msg['name']}</span>
                <span class="msg-date">{msg['date']}</span>
            </div>
            <div class="msg-email">{msg['email']}</div>
            <span class="msg-subject">{msg['subject']}</span>
            <div class="msg-body">{msg['message']}</div>
        </div>
        """

    st.markdown(f"""
    <div class="message-display">
        <h4>📬 Messages reçus ({len(st.session_state.messages)})</h4>
        {msgs_html}
    </div>
    """, unsafe_allow_html=True)

# Informations de contact (colonne droite)
st.markdown(f"""
            <div class="contact-info-box">
                <a href="mailto:{EMAIL_ADDRESS}" class="contact-link">
                    <div class="cl-icon">📧</div>
                    <div class="cl-text">
                        <h5>Email</h5>
                        <p>{EMAIL_ADDRESS}</p>
                    </div>
                </a>
                <a href="tel:{PHONE_NUMBER}" class="contact-link">
                    <div class="cl-icon">📞</div>
                    <div class="cl-text">
                        <h5>Téléphone</h5>
                        <p>{PHONE_NUMBER}</p>
                    </div>
                </a>
                <a href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank" class="contact-link">
                    <div class="cl-icon">💬</div>
                    <div class="cl-text">
                        <h5>WhatsApp</h5>
                        <p>Discutez avec nous instantanément</p>
                    </div>
                </a>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ── FOOTER ─────────────────────────────────────────────────────────────
footer_logo = ""
if logo_b64:
    footer_logo = f'<img src="data:image/jpeg;base64,{logo_b64}" alt="Herbek Services" style="width:50px; height:50px; border-radius:12px; margin-bottom:1rem; border: 2px solid var(--primary);">'

st.markdown(f"""
<footer class="footer">
    {footer_logo}
    <div class="footer-brand">Herbek<span> Services</span></div>
    <p>{SLOGAN}</p>
    <div class="footer-divider"></div>
    <div class="footer-links">
        <a href="#accueil">Accueil</a>
        <a href="#apropos">À propos</a>
        <a href="#services">Services</a>
        <a href="#pourquoi">Pourquoi nous</a>
        <a href="#contact">Contact</a>
    </div>
    <p class="footer-copy">&copy; {datetime.now().year} {BRAND_NAME}. Tous droits réservés.</p>
</footer>
""", unsafe_allow_html=True)