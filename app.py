import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Konfiguration
st.set_page_config(page_title="TikTok Live Dashboard", layout="wide")
st.title("📺 TikTok Live mit Chat")

# Chat-Datei definieren
CHAT_FILE = "chat.csv"
if not os.path.exists(CHAT_FILE):
    pd.DataFrame(columns=["User", "Kommentar"]).to_csv(CHAT_FILE, index=False)

# UI-Styles
st.markdown("""
<style>
.chat-container {
    background-color: #1e1e20;
    padding: 1em;
    border-radius: 10px;
    max-height: 600px;
    overflow-y: auto;
    font-family: 'Segoe UI', sans-serif;
    font-size: 0.95rem;
    color: #f2f2f2;
}
.chat-bubble {
    background-color: #2c2c2e;
    padding: 0.6em 1em;
    border-radius: 15px;
    margin-bottom: 0.5em;
}
.chat-user {
    color: #fe2c55;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Spalten
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("🔴 Livestream")
    st.markdown("""
    <a href="https://www.tiktok.com/@naruepatnew/live" target="_blank">
        <button style="background-color:#fe2c55;color:#fff;padding:0.6em 1.2em;border:none;
        border-radius:8px;font-size:1rem;cursor:pointer;">
        Jetzt TikTok-Stream öffnen
        </button>
    </a>
    """, unsafe_allow_html=True)

    st.markdown("### 💬 Kommentar abgeben")
    with st.form(key="chat_form"):
        username = st.text_input("Benutzername")
        kommentar = st.text_area("Kommentar")
        senden = st.form_submit_button("📤 Absenden")

        if senden and username.strip() and kommentar.strip():
            chat = pd.read_csv(CHAT_FILE)
            neuer_eintrag = pd.DataFrame([{
                "User": username.strip(),
                "Kommentar": kommentar.strip()
            }])
            chat = pd.concat([chat, neuer_eintrag], ignore_index=True)
            chat.to_csv(CHAT_FILE, index=False)
            st.success("✅ Kommentar gespeichert!")

with col2:
    st.subheader("💬 Live-Chat")

    try:
        chat = pd.read_csv(CHAT_FILE)
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for _, row in chat.iterrows():
            st.markdown(f"""
            <div class="chat-bubble">
                <span class="chat-user">{row['User']}</span><br>{row['Kommentar']}
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("💾 Chat speichern"):
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"chat_{ts}.csv"
            chat.to_csv(filename, index=False)
            st.success(f"📁 Chat gespeichert als `{filename}`")

    except Exception as e:
        st.error(f"Fehler beim Laden von `chat.csv`: {e}")