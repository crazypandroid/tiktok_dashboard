import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Dashboard-Konfiguration
st.set_page_config(page_title="TikTok Dual View", layout="wide")
st.title("📺 TikTok Livestream + Chat Tracker")

# Sidebar: Creator eingeben
st.sidebar.header("🎯 TikTok-Creator auswählen")
username_input = st.sidebar.text_input("TikTok Username", value="naruepatnew")

# Dynamischer Pfad zur Chat-Datei
chat_file = f"chat_{username_input}.csv"
if not os.path.exists(chat_file):
    pd.DataFrame(columns=["User", "Kommentar"]).to_csv(chat_file, index=False)

# Spalten: Stream links, Chat rechts
stream_col, chat_col = st.columns([3, 1])

with stream_col:
    st.subheader(f"🔴 Livestream: @{username_input}")
    tiktok_url = f"https://www.tiktok.com/@{username_input}/live"
    st.markdown(f"""
    <iframe src="{tiktok_url}" height="600" width="100%" frameborder="0"
    allowfullscreen allow="autoplay"></iframe>
    """, unsafe_allow_html=True)
    st.caption("⚠️ Falls der Livestream im iframe nicht funktioniert, öffne ihn im neuen Tab:")
    st.markdown(f"[🌐 Direkt ansehen bei TikTok →]({tiktok_url})")

with chat_col:
    st.subheader("💬 Live-Chat")

    try:
        chat = pd.read_csv(chat_file)
        if chat.empty:
            st.info("Keine Kommentare vorhanden.")
        else:
            st.markdown(
                '<div style="background-color:#1e1e20;padding:1em;border-radius:8px;'
                'max-height:600px;overflow-y:auto;font-family:sans-serif;">',
                unsafe_allow_html=True
            )
            for _, row in chat.iterrows():
                st.markdown(f"""
                <div style="margin-bottom:0.75em;">
                    <span style="color:#fe2c55;font-weight:bold;">{row['User']}</span><br>
                    <span style="color:#f2f2f2;">{row['Kommentar']}</span>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        if st.button("💾 Chat speichern"):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            export_file = f"{username_input}_chat_{timestamp}.csv"
            chat.to_csv(export_file, index=False)
            st.success(f"✅ Chat gespeichert als `{export_file}`")

    except Exception as e:
        st.error(f"Fehler beim Laden von `{chat_file}`: {e}")