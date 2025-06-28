import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Page Setup
st.set_page_config(page_title="TikTok Viewer", layout="wide")
st.title("📺 TikTok Livestream + Chat")

# Sidebar: Creator eingeben
st.sidebar.header("🎯 TikTok Creator auswählen")
username = st.sidebar.text_input("TikTok Username", value="naruepatnew")

# Chat-Datei dynamisch setzen
chat_file = f"chat_{username}.csv"
if not os.path.exists(chat_file):
    pd.DataFrame(columns=["User", "Kommentar"]).to_csv(chat_file, index=False)

# Spaltenlayout
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader(f"🔴 Stream von @{username}")
    stream_link = f"https://www.tiktok.com/@{username}/live"
    st.markdown(f"""
    <a href="{stream_link}" target="_blank">
        <button style="background-color:#fe2c55;color:#fff;padding:0.6em 1.2em;border:none;
        border-radius:8px;font-size:1rem;cursor:pointer;">
        👉 Livestream jetzt öffnen
        </button>
    </a>
    """, unsafe_allow_html=True)
    st.caption("Öffnet den TikTok-Stream in einem neuen Tab.")

with col2:
    st.subheader("💬 Chat")

    try:
        chat = pd.read_csv(chat_file)
        if chat.empty:
            st.info("Noch keine Kommentare vorhanden.")
        else:
            st.markdown('<div style="background-color:#1e1e20;padding:1em;border-radius:8px;'
                        'max-height:600px;overflow-y:auto;">', unsafe_allow_html=True)
            for _, row in chat.iterrows():
                st.markdown(f"""
                <div style="margin-bottom:0.75em;">
                    <span style="color:#fe2c55;font-weight:bold;">{row['User']}</span><br>
                    <span style="color:#f2f2f2;">{row['Kommentar']}</span>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        if st.button("💾 Chat speichern"):
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{username}_chat_{ts}.csv"
            chat.to_csv(filename, index=False)
            st.success(f"✅ Gespeichert als `{filename}`")

    except Exception as e:
        st.error(f"Fehler beim Laden von `{chat_file}`: {e}")