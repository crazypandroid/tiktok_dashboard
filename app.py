import streamlit as st
import pandas as pd
from datetime import datetime

# Streamlit Konfiguration
st.set_page_config(page_title="TikTok Live Dashboard", layout="wide")
st.title("📺 TikTok Live mit Chat")

# Custom CSS für modernes UI
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

with col2:
    st.subheader("💬 Live-Chat")

    try:
        chat = pd.read_csv("chat.csv")

        # Chat anzeigen
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for _, row in chat.iterrows():
            user = row['User']
            msg = row['Kommentar']
            st.markdown(f"""
            <div class="chat-bubble">
                <span class="chat-user">{user}</span><br>{msg}
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Chat speichern
        if st.button("💾 Chat speichern"):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"chat_{timestamp}.csv"
            chat.to_csv(filename, index=False)
            st.success(f"✅ Chat gespeichert als `{filename}`")

    except FileNotFoundError:
        st.warning("⚠️ Die Datei `chat.csv` wurde nicht gefunden.")