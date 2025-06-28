import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="TikTok Viewer", layout="wide")
st.title("📺 TikTok Live – Viewer & Recorder")

# Custom CSS für Chat-Stil
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
col_stream, col_chat = st.columns([3, 1])

# Lade Chat-Datei
try:
    chat_df = pd.read_csv("chat.csv")
except Exception:
    chat_df = pd.DataFrame(columns=["User", "Kommentar"])

with col_stream:
    st.subheader("🎬 Livestream")
    st.markdown("👉 [@naruepatnew live auf TikTok ansehen](https://www.tiktok.com/@naruepatnew/live)")
    st.video("example_stream.mp4")

    # Aufnahme-Button
    if st.button("📥 Chat speichern"):
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"chat_{now}.csv"
        chat_df.to_csv(filename, index=False)
        st.success(f"💾 Chat gespeichert als `{filename}`")

with col_chat:
    st.subheader("💬 Live-Chat")
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for _, row in chat_df.iterrows():
        user = row["User"]
        msg = row["Kommentar"]
        st.markdown(f"""
        <div class="chat-bubble">
            <span class="chat-user">{user}</span><br>{msg}
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)