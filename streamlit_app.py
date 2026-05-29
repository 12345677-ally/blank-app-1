import streamlit as st

# ページの基本設定
st.set_page_config(page_title="スマホ通知音 改善版", page_icon="📱", layout="centered")

# --- 💡追加：通知を画面に残すための「記憶箱」 ---
if "notif_history" not in st.session_state:
    st.session_state.notif_history = []

st.title("📱 スマホ通知音のUI改善デモ")
st.write("ボタンを押すと通知が来ます")

# 通知をすべて消して最初からやり直すボタン
if st.button("🗑️ ロック画面の通知をすべて消去"):
    st.session_state.notif_history = []
    st.rerun()

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
            st.toast("LINE: お疲れ様！明日のゼミの件なんだけど...", icon="💬")
            # 記憶箱に通知を追加
            st.session_state.notif_history.insert(0, "💬 LINE: お疲れ様！明日のゼミの件なんだけど...")
            
    with col2:
        if st.button("📦 Amazonの通知", key="bad_amazon"):
            st.audio("かわいい動き09.mp3", format="audio/mp3", autoplay=True)
            st.toast("Amazon: ご注文の品が本日到着予定です", icon="📦")
            st.session_state.notif_history.insert(0, "📦 Amazon: ご注文の品が本日到着予定です")
            
    with col3:
        if st.button(" 🌤️天気予報の通知", key="bad_calendar"):
            st.audio("かわいい動き09.mp3", format="audio/mp3", autoplay=True)
            st.toast("天気予報: 雨が降り始めます ", icon="🌤️")
            st.session_state.notif_history.insert(0, "🌤️ 天気予報: 雨が降り始めます")


# --- 改善案のGOOD UI ---
with tab2:
    st.header("直感的な聴覚デザイン")
    st.write("それぞれのアプリに合った通知音。ポップアップを見なくても音が教えてくれます。")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💬 LINEの通知", key="good_line"):
            # 💡修正：.m4aファイルなので format="audio/mp4" に変更しました
            st.audio("_96034830.m4a", format="audio/mp4", autoplay=True)
            st.toast("LINE: お疲れ様！明日のゼミの件なんだけど...", icon="💬")
            st.session_state.notif_history.insert(0, "💬 LINE: お疲れ様！明日のゼミの件なんだけど...")
            
    with col2:
        if st.button("📦 Amazonの通知", key="good_amazon"):
            st.audio("チャイム・インターホン02.mp3", format="audio/mp3", autoplay=True)
            st.toast("Amazon: ご注文の品が本日到着予定です", icon="📦")
            st.session_state.notif_history.insert(0, "📦 Amazon: ご注文の品が本日到着予定です")
            
    with col3:
        if st.button("🌤️ 天気予報の通知", key="good_calendar"):
            st.audio("天候・雨04.mp3", format="audio/mp3", autoplay=True)
            st.toast("天気予報: 雨が降り始めます", icon="🌤️")
            st.session_state.notif_history.insert(0, "🌤️ 天気予報: 雨が降り始めます")

# --- 📱 追加：ロック画面風の表示エリア ---
st.divider() # 区切り線
st.subheader("📱 現在のロック画面")

# 記憶箱の中身を一つずつ取り出して画面に並べる
if len(st.session_state.notif_history) == 0:
    st.write("通知はありません")
else:
    for msg in st.session_state.notif_history:
        st.info(msg) # 通知っぽい枠で表示

# ボタンの見栄えを良くするCSS
st.markdown("""
