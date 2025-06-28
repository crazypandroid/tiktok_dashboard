import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Streamlit Konfiguration
st.set_page_config(page_title="TikTok Live Dashboard", layout="wide")
st.title("📺 TikTok Live mit Chat")

# Chat-Datei vorbereiten
CHAT_FILE = "chat.csv"
if not os.path.exists(CHAT_FILE):
    df_init = pd.DataFrame(columns=["User", "Kommentar"])
    df_init.to_csv(CHAT_FILE, index=False)

# Custom CSS für TikTok-Vibe
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

# Spaltenaufteilung
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

    # Kommentar-Eingabe
    st.markdown("### 💬 Kommentar posten")
    with st.form(key="chat_form"):
        user = st.text_input("Benutzername", max_chars=30, key="username")
        kommentar = st.text_area("Dein Kommentar", key="comment")
        send = st.form_submit_button("📤 Abschicken")

        if send and user.strip() and kommentar.strip():
            df = pd.read_csv(CHAT_FILE)
            new_row = pd.DataFrame({"User": 