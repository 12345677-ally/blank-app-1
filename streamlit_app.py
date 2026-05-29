import streamlit as st

# ページの基本設定
st.set_page_config(page_title="スマホ通知音 改善版", page_icon="📱", layout="centered")

st.title("📱 スマホ通知音のUI改善デモ")
st.write("ボタンを押すと通知が来ます")

# タブでBAD UIとGOOD UIを分ける
tab1, tab2 = st.tabs(["❌ 現状 (BAD UI)", "✨ 提案 (GOOD UI)"])

# --- 現状のBAD UI ---
with tab1:
    st.header("画一的な通知音による混乱")
    st.write("すべて同じ通知音。ポップアップを見ないと何の通知か分かりません。")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💬 LINEの通知", key="bad_line"):
            st.audio("かわいい動き09.mp3", format="audio/mp3", autoplay=True)
            # スマホの通知風ポップアップを表示
            st.toast("LINE: お疲れ様！明日のゼミの件なんだけど...", icon="💬")
            
    with col2:
        if st.button("📦 Amazonの通知", key="bad_amazon"):
            st.audio("かわいい動き09.mp3", format="audio/mp3", autoplay=True)
            st.toast("Amazon: ご注文の品が本日到着予定です", icon="📦")
            
    with col3:
        if st.button(" 🌤️天気予報の通知", key="bad_calendar"):
            st.audio("かわいい動き09.mp3", format="audio/mp3", autoplay=True)
            st.toast("天気予報: 雨が降り始めます ", icon="🌤️")


# --- 改善案のGOOD UI ---
with tab2:
    st.header("直感的な聴覚デザイン")
    st.write("それぞれのアプリに合った通知音。ポップアップを見なくても音が教えてくれます。")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💬 LINEの通知", key="good_line"):
            st.audio("_96034830.m4a", format="audio/mp3", autoplay=True)
            st.toast("LINE: お疲れ様！明日のゼミの件なんだけど...", icon="💬")
            
    with col2:
        if st.button("📦 Amazonの通知", key="good_amazon"):
            st.audio("チャイム・インターホン02.mp3", format="audio/mp3", autoplay=True)
            st.toast("Amazon: ご注文の品が本日到着予定です", icon="📦")
            
    with col3:
        if st.button("🌤️ 天気予報の通知", key="good_calendar"):
            st.audio("天候・雨04.mp3", format="audio/mp3", autoplay=True)
            st.toast("天気予報: 雨が降り始めます", icon="🌤️")

# ボタンの見栄えを良くするCSS
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 60px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)
