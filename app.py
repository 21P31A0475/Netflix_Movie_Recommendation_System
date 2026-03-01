import streamlit as st
import pandas as pd
import pickle
import base64

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Netflix Recommender",
                   layout="wide",
                   initial_sidebar_state="collapsed")

# ---------- BACKGROUND ----------
def set_bg(img_file):
    with open(img_file, "rb") as f:
        img = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.65),
                                    rgba(0,0,0,0.65)),
                    url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    #MainMenu, footer {{visibility:hidden;}}
    h1, p, label {{color:white;}}
    .stButton>button {{
        background:#E50914;
        color:white;
        border:none;
        border-radius:6px;
    }}
    </style>
    """, unsafe_allow_html=True)

set_bg("NetflixLogo(1).png")   # <-- Netflix Background image

# ---------- NETFLIX LOGO TOP LEFT ----------
st.markdown("""
<div style="position:absolute; top:20px; left:40px;">
<img src="https://upload.wikimedia.org/wikipedia/commons/7/7a/Logonetflix.png" width="140">
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)


# ---------- LOAD DATA ----------
similarity = pickle.load(open('moviessimilarity.pkl', 'rb'))
df = pd.read_csv('tmdbdf.csv').iloc[:len(similarity)]

# ---------- TITLE ----------
st.markdown("<h1 style='text-align:center;'>Netflix Movie Recommendation System</h1>",
            unsafe_allow_html=True)

# ---------- SELECT ----------
movie = st.selectbox("Choose a Movie", df['title'])

# ---------- RECOMMEND ----------
def recommend(movie):
    idx = df[df['title']==movie].index[0]
    scores = sorted(list(enumerate(similarity[idx])),
                    key=lambda x:x[1],
                    reverse=True)[1:6]
    names, posters = [], []
    for i in scores:
        names.append(df.iloc[i[0]].title)
        poster = df.iloc[i[0]]['poster_path']
        posters.append("https://image.tmdb.org/t/p/w500/"+poster
                       if pd.notnull(poster)
                       else "https://via.placeholder.com/500x750")
    return names, posters

# ---------- BUTTON ----------
if st.button("Recommend Movies"):
    names, posters = recommend(movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i], width="stretch")
            st.markdown(f"<p style='text-align:center'>{names[i]}</p>",

                        unsafe_allow_html=True)
