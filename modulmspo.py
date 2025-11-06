# modulmspo_modern_responsive_fixed.py
import streamlit as st
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="E-Modul MSPO FELDA 2.0",
    page_icon="https://felda.gov.my/images/photo/logo/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Responsive + Modern CSS ---
st.markdown(
    """
    <style>
    :root{
        --felda-orange: #FF6600;
        --felda-dark: #2B2B2B;
        --felda-earth: #6B4B2A;
        --felda-green: #1B5E20;
        --bg: #FAFAF9;
        --card-bg: #FFFFFF;
        --muted: #6B6B6B;
    }

    .stApp {
        background-color: var(--bg);
        color: var(--felda-dark);
        font-family: "Inter", "Helvetica Neue", Arial, sans-serif;
    }

    .header-row {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 0.5rem 1rem;
        margin-bottom: 0.25rem;
    }
    .header-logo {
        width: 220px;
        max-width: 35%;
        height: auto;
    }
    .header-title {
        margin: 0;
        padding: 0;
    }
    .header-sub {
        margin-top: -0.25rem;
        color: var(--muted);
        font-size: 0.95rem;
    }

    .card {
        background: var(--card-bg);
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 6px 18px rgba(16, 24, 40, 0.08);
        border: 1px solid rgba(16,24,40,0.03);
    }

    .announcement-card {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        transition: transform .15s ease, box-shadow .15s ease;
    }
    .announcement-card h4 {
        margin: 0 0 0.25rem 0;
        color: var(--felda-earth);
        font-size: 1.05rem;
    }
    .announcement-card p.date {
        margin: 0 0 0.5rem 0;
        color: var(--muted);
        font-size: 0.88rem;
    }

    .principle-card {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        justify-content: space-between;
        padding: 1rem;
        border-radius: 10px;
        min-height: 110px;
    }
    .principle-title {
        font-weight: 700;
        color: var(--felda-green);
        font-size: 1rem;
    }
    .principle-desc {
        color: var(--muted);
        font-size: 0.95rem;
    }

    .stButton>button {
        border-radius: 8px;
        padding: 0.6rem 0.8rem;
        font-weight: 700;
        font-size: 0.95rem;
        border: none;
    }
    .link-btn {
        background: linear-gradient(90deg, var(--felda-orange), #e85a00);
        color: white !important;
        border: none !important;
        box-shadow: 0 6px 14px rgba(255,102,0,0.15);
    }

    .footer-small {
        color: var(--muted);
        font-size: 0.85rem;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fff, #FAFBFA);
        padding: 1rem 0.75rem 2rem 0.75rem;
    }
    .sidebar-logo {
        width: 160px;
        max-width: 100%;
        margin: 0 auto 0.5rem auto;
        display: block;
    }
    .sidebar-title {
        color: var(--felda-green);
        font-weight: 700;
        margin-bottom: 0.25rem;
        font-size: 0.98rem;
    }

    @media (max-width: 900px) {
        .header-logo { width: 160px; }
        .header-row { padding: 0.5rem 0.5rem; gap: 0.6rem; }
        .stApp { padding: 0; }
    }

    @media (max-width: 768px) {
        .header-logo { width: 120px; }
        .header-title { font-size: 1.05rem; }
        .header-sub { font-size: 0.9rem; }

        /* best-effort stacking of Streamlit columns */
        .css-1lcbmhc, .css-1lczr2b, .css-1gk6s8v {
            flex-direction: column !important;
        }
        .css-1d391kg, .css-12oz5g7, .css-14xtw13 {
            width: 100% !important;
            min-width: 100% !important;
        }

        .announcement-card, .principle-card, .card {
            width: 100% !important;
            box-sizing: border-box;
        }

        .stButton>button {
            width: 100% !important;
        }
    }

    h1, h2, h3, h4, p, li, a, span, div {
        color: var(--felda-dark) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header with FELDA logo (top) ---
FELDA_LOGO = "https://felda.gov.my/images/photo/logo/logo.png"

st.markdown(
    f"""
    <div class="header-row">
        <img src="{FELDA_LOGO}" class="header-logo" alt="FELDA logo" />
        <div>
            <h1 class="header-title">🌿 E-Modul MSPO FELDA 2.0</h1>
            <div class="header-sub">Portal Latihan Pensijilan — Malaysian Sustainable Palm Oil (MSPO) 2.0</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# --- Intro / Info ---
st.info(
    "Selamat datang ke **E-Modul MSPO FELDA 2.0** — platform latihan digital untuk meningkatkan pemahaman dan pelaksanaan prinsip MSPO. Gunakan butang di bawah setiap modul untuk membuka sumber di SharePoint/OneDrive."
)

st.markdown("## 📢 Pengumuman Terkini")

announcements = [
    {
        "date": "1 November 2025",
        "title": "FELDA Capai 100% Pensijilan MSPO! 🎉",
        "content": "Tahniah kepada semua rancangan atas kejayaan ini. FELDA kini berjaya mencapai 100% pensijilan MSPO bagi semua rancangan, hasil usaha berterusan semua pihak."
    },
    {
        "date": "5–7 Nov 2025",
        "title": "Audit Dalaman - Gugusan Jengka 18",
        "content": "Sila pastikan semua dokumentasi lengkap sebelum tarikh audit. Rujuk checklist dalaman dan sediakan semua bukti objektif yang berkaitan."
    },
    {
        "date": "18–20 Nov 2025",
        "title": "Audit Luaran - Gugusan Triang",
        "content": "Pastikan akses pintu masuk log dan rekod latihan pekerja dikemaskini."
    }
]

# Render announcements (two columns on wide screens)
cols = st.columns(2)
for i, ann in enumerate(announcements):
    col = cols[i % 2]
    with col:
        st.markdown(
            f"""
            <div class="card announcement-card">
                <h4>{ann['title']}</h4>
                <p class="date">{ann['date']}</p>
                <div style="color: #444; font-size:0.95rem;">{ann['content']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")

# --- Module Links Section ---
st.markdown("## 📚 Modul MSPO 2.0 — Akses Sumber")
st.markdown("Klik butang **Akses Modul** untuk membuka dokumen rujukan (OneDrive/SharePoint).")

modules = [
    ("P1", "Komitmen dan Tanggungjawab Pengurusan", "🤝", "https://feldagov-my.sharepoint.com/:f:/g/personal/jk_felda_feldagov_onmicrosoft_com/EthOPknnDeFKqIWuXEG9nRYBTkn0LkMj8b0H0g7QasBVRQ?e=z6ED5X"),
    ("P2", "Ketelusan", "📄", "https://feldagov-my.sharepoint.com/:f:/g/personal/jk_felda_feldagov_onmicrosoft_com/EpbAFAB0PpNPgknhRLrA_jkBwbFBNuhMw3oXSy9EB8wnNQ?e=VQo6Xy"),
    ("P3", "Pematuhan Kepada Undang-Undang", "⚖️", "https://feldagov-my.sharepoint.com/:f:/g/personal/jk_felda_feldagov_onmicrosoft_com/Et_7uwJCrHpGkpAxJdMXrJEBxjJcXWWlPgdxFy312OAmfA?e=A1y8T4"),
    ("P4", "Tanggungjawab Sosial & Keselamatan", "👨‍🏭", "https://feldagov-my.sharepoint.com/:f:/g/personal/jk_felda_feldagov_onmicrosoft_com/EvOKSXLalP9NpSxbBSfhY74BievO9jtbnBr7gFYNeceDqw?e=aQV1Fk"),
    ("P5", "Alam Sekitar & Penjagaan Ekosistem", "🌳", "https://feldagov-my.sharepoint.com/:f:/g/personal/jk_felda_feldagov_onmicrosoft_com/EuFU6F-Dr85LqbHyfWhL82YBHWA7LuClMHyFC1wbgdVGXA?e=s3aTAo"),
    ("MANUAL", "Dokumen Manual, Polisi dan Prosedur", "📑", "https://feldagov-my.sharepoint.com/:f:/g/personal/jk_felda_feldagov_onmicrosoft_com/EtJ5hWHrFxlPjLxT-u7JocEBrBQMJgZrh1v5og2UaQ5gag?e=WHlTq8")
]

cols_mod = st.columns(2, gap="large")
for i, (code, title, icon, link) in enumerate(modules):
    col = cols_mod[i % 2]
    with col:
        st.markdown(
            f"""
            <div class="card principle-card">
                <div>
                    <div class="principle-title">{icon} {code}: {title}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        # Use st.link_button if available, otherwise fallback to anchor
        try:
            st.link_button(label=f"📥 Akses Modul {code}", url=link, use_container_width=True)
        except Exception:
            st.markdown(
                f"""<a href="{link}" target="_blank" style="text-decoration:none;">
                        <div class="stButton"><button class="link-btn" style="width:100%;">📥 Akses Modul {code}</button></div>
                   </a>""",
                unsafe_allow_html=True,
            )

st.markdown("---")

# --- Footer / Contact ---
st.markdown("## 📞 Hubungi Kami")
col_email, col_right = st.columns([2, 1])
with col_email:
    st.markdown(
        """
        <div class="card" style="padding:0.8rem;">
            <div style="font-weight:700; color:#2B2B2B;">Untuk sebarang pertanyaan berkaitan E-Modul MSPO:</div>
            <div style="margin-top:0.5rem; color:#444;">
                • <strong>Email</strong>: <a href="mailto:kelestarian.f@felda.net.my">kelestarian.f@felda.net.my</a><br/>
                • <strong>Hotline</strong>: +603-2191 2191
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_right:
    st.markdown(
        f"""
        <div style="text-align: right;">
            <img src="{FELDA_LOGO}" class="sidebar-logo" alt="FELDA logo" />
            <div class="footer-small">© {datetime.now().year} FELDA | MSPO 2.0</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- Sidebar content (logo + guide) ---
with st.sidebar:
    st.markdown(f'<img src="{FELDA_LOGO}" class="sidebar-logo" alt="FELDA logo" />', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">📖 Panduan Penggunaan</div>', unsafe_allow_html=True)
    st.info(
        "1. Pilih Prinsip (P1–P5) • 2. Klik 'Akses Modul' • 3. Dokumen akan dibuka di tab baru (OneDrive/SharePoint)."
    )
    st.markdown('<div class="sidebar-title">🌱 Tentang MSPO</div>', unsafe_allow_html=True)
    st.success(
        "MSPO memastikan pengeluaran minyak sawit secara mampan melalui amalan terbaik, pematuhan undang-undang, dan tanggungjawab sosial."
    )

    st.markdown(f"""
        <div style="margin-top: 1rem; border-top: 1px solid #eee; padding-top:0.8rem;">
            <div style="color:#666; font-size:0.9rem;">Tarikh Terkini: {datetime.now().strftime('%d %B %Y')}</div>
        </div>
    """, unsafe_allow_html=True)

# --- Small maintenance note ---
st.markdown(
    """
    <div style="margin-top:12px; color:#666; font-size:0.9rem;">
    <em>Nota teknikal:</em> Jika susunan kolum tidak bertukar kepada satu lajur pada peranti tertentu, cuba kemas kini versi Streamlit anda. Jika masih terdapat isu, pastekan log error penuh dan saya akan debug lanjut.
    </div>
    """,
    unsafe_allow_html=True,
)
