import streamlit as st
import numpy as np
import random
from textblob import TextBlob # type: ignore
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Tote's Birthday🎂",page_icon="❤️", layout="centered")

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&family=Dancing+Script:wght@700&family=Pacifico&display=swap');

* {
    font-family: 'Quicksand', sans-serif;
}
            
header[data-testid="stHeader"] {
    background: #003d3d !important;
    border-bottom: 1px solid rgba(0, 200, 180, 0.2);
}

.stApp {
    background: linear-gradient(135deg, #003d3d, #006666, #008080, #00a896, #02c39a);
    background-size: 400% 400%;
    animation: gradientShift 10s ease infinite;
    color: #e0ffff;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

[data-testid="stSidebar"] {
    background: rgba(0, 60, 60, 0.85) !important;
    border-right: 1px solid #00a896;
}

[data-testid="stSidebar"] * {
    color: #e0ffff !important;
}

.glass {
    background: rgba(0, 128, 128, 0.2);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(0, 200, 180, 0.3);
    color: #e0ffff;
}

.stButton > button {
    background: linear-gradient(135deg, #008080, #02c39a);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 25px;
    font-weight: 700;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0, 200, 180, 0.3);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #02c39a, #008080);
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(0, 200, 180, 0.5);
}

.stSlider > div > div > div {
    background: #02c39a !important;
}

.stTextArea textarea, .stTextInput input {
    background: rgba(0, 80, 80, 0.4) !important;
    color: #e0ffff !important;
    border: 1px solid #00a896 !important;
    border-radius: 10px !important;
}

.stSelectbox > div > div {
    background: rgba(0, 80, 80, 0.4) !important;
    color: #e0ffff !important;
    border: 1px solid #00a896 !important;
    border-radius: 10px !important;
}

h1, h2, h3 {
    text-align: center;
    color: #e0ffff;
    text-shadow: 0 0 20px rgba(2, 195, 154, 0.6);
}

.stPlotlyChart, [data-testid="stMetric"] {
    background: rgba(0, 80, 80, 0.3);
    border-radius: 12px;
    padding: 10px;
}

.stDateInput input {
    background: rgba(0, 80, 80, 0.4) !important;
    color: #e0ffff !important;
    border: 1px solid #00a896 !important;
    border-radius: 10px !important;
}

.stRadio label {
    color: #e0ffff !important;
}

.typewriter {
    overflow: hidden;
    border-right: 0.25px transparent;
    white-space: nowrap;
    width: 0;
    animation: typing 3s steps(40, end) forwards, blink 0.75s step-end infinite;
    color: #e0ffff;
}

.typewriter:nth-child(2) { animation-delay: 3s; }
.typewriter:nth-child(3) { animation-delay: 6s; }

@keyframes typing {
    from { width: 0 }
    to { width: 100% }
}

@keyframes blink {
    from, to { border-color: transparent }
    50% { border-color: #02c39a }
}

/* ---- BIRTHDAY PAGE ---- */
.bday-wrapper {
    text-align: center;
    padding: 20px 0 40px 0;
}

.bday-main {
    font-family: 'Pacifico', cursive;
    font-size: clamp(48px, 10vw, 90px);
    background: linear-gradient(135deg, #e0ffff, #02c39a, #ffffff, #00a896);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 4s ease infinite, popIn 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    display: block;
    line-height: 1.2;
    filter: drop-shadow(0 0 30px rgba(2, 195, 154, 0.5));
}

.bday-name {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(36px, 8vw, 72px);
    color: #ffffff;
    text-shadow: 0 0 30px rgba(2, 195, 154, 0.8), 0 0 60px rgba(2, 195, 154, 0.4);
    animation: popIn 0.8s 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) both;
    display: block;
    margin-top: 10px;
}

@keyframes popIn {
    0%   { opacity: 0; transform: scale(0.5) translateY(30px); }
    100% { opacity: 1; transform: scale(1) translateY(0); }
}

.bday-emoji-row {
    font-size: 40px;
    margin: 20px 0;
    animation: fadeSlideUp 1s 0.6s both;
    letter-spacing: 8px;
}

.bday-message {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(18px, 3vw, 26px);
    color: #e0ffff;
    line-height: 1.9;
    animation: fadeSlideUp 1s 0.9s both;
    max-width: 600px;
    margin: 0 auto;
    padding: 0 20px;
}

@keyframes fadeSlideUp {
    0%   { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

.bday-card {
    background: rgba(0, 128, 128, 0.15);
    border: 1px solid rgba(2, 195, 154, 0.4);
    border-radius: 24px;
    backdrop-filter: blur(16px);
    padding: 35px;
    margin: 30px auto;
    max-width: 620px;
    box-shadow: 0 0 40px rgba(2, 195, 154, 0.15), inset 0 0 40px rgba(2, 195, 154, 0.05);
    animation: fadeSlideUp 1s 1.2s both;
}

.bday-wishes {
    font-size: 15px;
    color: rgba(224, 255, 255, 0.85);
    line-height: 2;
    text-align: left;
}

.bday-wishes span {
    display: block;
    padding: 6px 0;
    border-bottom: 1px solid rgba(2, 195, 154, 0.15);
}

.bday-wishes span:last-child {
    border-bottom: none;
}

.bday-footer {
    font-family: 'Dancing Script', cursive;
    font-size: 22px;
    color: #02c39a;
    margin-top: 30px;
    animation: fadeSlideUp 1s 1.5s both;
    text-shadow: 0 0 20px rgba(2, 195, 154, 0.6);
}

.confetti-row {
    font-size: 28px;
    animation: bounce 1s ease infinite alternate, fadeSlideUp 1s 1.8s both;
    display: inline-block;
    letter-spacing: 5px;
}

@keyframes bounce {
    from { transform: translateY(0px); }
    to   { transform: translateY(-8px); }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.hearts-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.heart {
    position: absolute;
    font-size: 24px;
    animation: floatHeart linear infinite;
    opacity: 0;
    filter: drop-shadow(0 0 6px rgba(2, 195, 154, 0.4));
}

@keyframes floatHeart {
    0%   { transform: translateY(100vh) scale(0.5); opacity: 0; }
    10%  { opacity: 0.6; }
    90%  { opacity: 0.2; }
    100% { transform: translateY(-10vh) scale(1.1); opacity: 0; }
}
</style>

<div class="hearts-container">
    <div class="heart" style="left:5%;  font-size:16px; animation-duration:12s; animation-delay:0s;">🩵</div>
    <div class="heart" style="left:15%; font-size:28px; animation-duration:18s; animation-delay:2s;">🩵</div>
    <div class="heart" style="left:25%; font-size:20px; animation-duration:14s; animation-delay:5s;">🩵</div>
    <div class="heart" style="left:35%; font-size:32px; animation-duration:20s; animation-delay:1s;">🩵</div>
    <div class="heart" style="left:45%; font-size:16px; animation-duration:16s; animation-delay:7s;">🩵</div>
    <div class="heart" style="left:55%; font-size:24px; animation-duration:13s; animation-delay:3s;">🩵</div>
    <div class="heart" style="left:65%; font-size:36px; animation-duration:19s; animation-delay:6s;">🤍</div>
    <div class="heart" style="left:75%; font-size:20px; animation-duration:15s; animation-delay:4s;">🤍</div>
    <div class="heart" style="left:85%; font-size:28px; animation-duration:17s; animation-delay:8s;">🤍</div>
    <div class="heart" style="left:92%; font-size:16px; animation-duration:11s; animation-delay:2s;">🤍</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# TRAIN COMPATIBILITY MODEL
# -----------------------------
@st.cache_resource
def train_model():
    np.random.seed(42)
    X = np.random.rand(300, 4)
    y = (X[:,0]*30 + X[:,1]*20 + X[:,2]*25 + X[:,3]*25)
    model = LinearRegression()
    model.fit(X, y)
    return model

model = train_model()

# -----------------------------
# LOVE LETTERS
# -----------------------------
love_letters = [
     """This one is a reminder, reminding you that i will always love you, 
     always grateful for having you and nothing will ever be as special as you are to me🫂
     """,
      """Reminder: htfdal dyman aghla w a7la 7aga 7asltly ya mina❤️
     """,
       """ You will always be my favourite smile, plssss dont stop smiling everrrr🥹
     """,
        """ Reminder: Tote mafesh a7la menak fel donia wala ashtar menak, if u r feeling down pls dont myl u r doing perfect🫂
     """,

    """Dear loml,
I love the way your eyes light up when you talk about something you care about, the wayyou smile and look me in the eyes when we both know we want to kiss so much. And I adore the smell of all of your perfumes and scents.
You make even the most normal days feel like something worth remembering.
I really love spending every second with you!
""",

    """To my favorite person,
There's no one else I'd rather be myself with.
You make me laugh harder and feel safer than anyone ever has.
Thank you for existing.
""",

    """Hey baby,
I was thinking about you today which honestly isn't new, I think about you all the time.
Writing these feels so wholesome and special to me, just like how i feel about you.
You are so deeply loved ya mina, even on the days you forget it.
Love and miss you soo much❤️""",

    """My love,
I dont have the right words for what you mean to me.
But I hope you feel it anyway, in every small thing I do, in every moment I choose you.
You are my favorite chapter in life.
""",

    """To my baby,
I hope you know that you are somebody's reason to smile every single day.
You are enough and you are so so loved. I wish I could give you the whole world as a gift, just to show how thankful i am for you.
Never forget that.
"""
]



# -----------------------------
# MOOD ANALYSIS — ANN MODEL
# -----------------------------
from textblob import TextBlob
from sklearn.neural_network import MLPClassifier

MOOD_LABELS = ["Devastated", "Sad", "Anxious", "Low Energy", "Good", "Happy"]

MOOD_RESPONSES = {
    "Devastated": {
        "affirmation": "Just take a deep breath... nothing deserves to break you.",
        "action": "Drink some water and breathe slowly till you are calm."
    },
    "Sad": {
        "affirmation": "You don't have to carry everything alone.",
        "action": "Wrap yourself in something warm and breathe slowly."
    },
    "Anxious": {
        "affirmation": "Everything will be okay i promise.",
        "action": "Call me!!!"
    },
    "Low Energy": {
        "affirmation": "It's okay to move gently today.",
        "action": "Drink water and take a small break."
    },
    "Good": {
        "affirmation": "I hope all your days are as good as now.",
        "action": "Do one small thing that makes you smile."
    },
    "Happy": {
        "affirmation": "Your energy is beautiful today.",
        "action": "YAY, we are happy. Try to use the good energy in something useful"
    }
}

@st.cache_resource
def train_mood_ann():
    X = np.array([
        # Devastated (polarity, subjectivity, word_count, exclamation, question)
        [-0.9, 0.9, 0.4, 0, 0], [-0.8, 0.8, 0.3, 0, 0], [-0.7, 0.9, 0.5, 0, 1],
        [-0.85, 0.7, 0.36, 0, 0], [-0.75, 0.85, 0.44, 0, 1],
        [-0.95, 0.95, 0.5, 0, 0], [-0.88, 0.82, 0.42, 0, 0],
        [-0.72, 0.91, 0.38, 0, 1], [-0.83, 0.76, 0.46, 0, 0],
        [-0.91, 0.88, 0.52, 0, 1], [-0.78, 0.93, 0.34, 0, 0],
        [-0.86, 0.79, 0.48, 0, 1], [-0.69, 0.87, 0.41, 0, 0],

        # Sad
        [-0.5, 0.7, 0.3, 0, 0], [-0.4, 0.6, 0.24, 0, 1], [-0.45, 0.75, 0.36, 0, 0],
        [-0.35, 0.65, 0.2, 0, 0], [-0.5, 0.8, 0.4, 0, 1],
        [-0.55, 0.72, 0.32, 0, 0], [-0.42, 0.68, 0.26, 0, 0],
        [-0.48, 0.77, 0.38, 0, 1], [-0.38, 0.63, 0.22, 0, 0],
        [-0.52, 0.74, 0.34, 0, 1], [-0.46, 0.69, 0.28, 0, 0],
        [-0.36, 0.71, 0.42, 0, 1], [-0.53, 0.66, 0.30, 0, 0],

        # Anxious
        [-0.2, 0.8, 0.6, 1, 1], [-0.15, 0.9, 0.5, 1, 1], [-0.25, 0.7, 0.56, 0, 1],
        [-0.1, 0.85, 0.7, 1, 1], [-0.2, 0.75, 0.44, 0, 1],
        [-0.18, 0.82, 0.62, 1, 1], [-0.22, 0.88, 0.54, 0, 1],
        [-0.12, 0.78, 0.66, 1, 1], [-0.28, 0.84, 0.48, 0, 1],
        [-0.16, 0.91, 0.58, 1, 1], [-0.24, 0.73, 0.64, 0, 1],
        [-0.19, 0.86, 0.52, 1, 1], [-0.14, 0.79, 0.68, 1, 1],

        # Low Energy
        [-0.1, 0.5, 0.16, 0, 0], [-0.05, 0.4, 0.12, 0, 0], [-0.08, 0.6, 0.2, 0, 0],
        [-0.03, 0.45, 0.14, 0, 0], [-0.09, 0.55, 0.18, 0, 0],
        [-0.07, 0.42, 0.15, 0, 0], [-0.04, 0.52, 0.13, 0, 0],
        [-0.06, 0.48, 0.17, 0, 0], [-0.02, 0.38, 0.11, 0, 0],
        [-0.11, 0.58, 0.19, 0, 0], [-0.01, 0.44, 0.16, 0, 0],
        [0.0,  0.35, 0.10, 0, 0], [0.01,  0.41, 0.14, 0, 0],

        # Good
        [0.2, 0.5, 0.24, 0, 0], [0.3, 0.6, 0.3, 0, 0], [0.25, 0.55, 0.2, 0, 0],
        [0.35, 0.5, 0.36, 0, 0], [0.15, 0.45, 0.28, 0, 0],
        [0.22, 0.52, 0.26, 0, 0], [0.32, 0.58, 0.32, 0, 0],
        [0.28, 0.48, 0.22, 0, 0], [0.18, 0.54, 0.34, 0, 0],
        [0.38, 0.62, 0.38, 0, 0], [0.42, 0.56, 0.30, 0, 0],
        [0.45, 0.51, 0.27, 0, 0], [0.40, 0.49, 0.33, 0, 0],

        # Happy
        [0.8, 0.7, 0.4, 1, 0], [0.9, 0.8, 0.5, 1, 0], [0.7, 0.6, 0.36, 1, 0],
        [0.85, 0.75, 0.44, 1, 0], [0.75, 0.65, 0.32, 1, 0],
        [0.82, 0.72, 0.42, 1, 0], [0.88, 0.78, 0.48, 1, 0],
        [0.76, 0.68, 0.38, 1, 0], [0.92, 0.82, 0.52, 1, 0],
        [0.78, 0.74, 0.46, 1, 0], [0.86, 0.76, 0.40, 1, 0],
        [0.94, 0.84, 0.54, 1, 0], [0.72, 0.62, 0.34, 1, 0],
    ])

    y = np.array([0]*13 + [1]*13 + [2]*13 + [3]*13 + [4]*13 + [5]*13)

    model = MLPClassifier(
        hidden_layer_sizes=(64, 128, 64),  # bigger network
        activation='relu',
        max_iter=2000,                     # more training
        random_state=42,
        learning_rate='adaptive',          # smarter learning rate
        early_stopping=True,               # stops when it peaks
        validation_fraction=0.15
    )
    model.fit(X, y)
    return model

mood_ann = train_mood_ann()

def extract_features(text):
    import re
    clean_text = re.sub(r'(.)\1{2,}', r'\1', text)
    blob = TextBlob(clean_text)
    polarity     = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    word_count   = min(len(clean_text.split()) / 50, 1.0)
    exclamation  = min(text.count('!') / 3, 1.0)
    question     = min(text.count('?') / 3, 1.0)
    return np.array([[polarity, subjectivity, word_count, exclamation, question]])

def analyze_mood(text):
    features = extract_features(text)
    probs     = mood_ann.predict_proba(features)[0]
    mood_idx  = int(np.argmax(probs))
    confidence = float(probs[mood_idx]) * 100
    blob = TextBlob(text)
    return mood_idx, confidence, blob.sentiment.polarity, blob.sentiment.subjectivity

# -----------------------------
# LANDING
# -----------------------------
if "entered" not in st.session_state:
    st.session_state.entered = False

if not st.session_state.entered:
    st.title("🌌 Our Little Universe")
    st.markdown("""
<p class='typewriter' style='animation-delay: 0s'>This is a small gift for u loml...</p>
<p class='typewriter' style='animation-delay: 3s'>I wanted to say Happy Birthday in the most special way...</p>
<p class='typewriter' style='animation-delay: 6s'>So, Happy 21st birthday to my favourite human on earth❤️</p>
""", unsafe_allow_html=True)

    from datetime import date
    CORRECT_BIRTHDAY = date(2005, 3, 5)

    birthday = st.date_input(
        "Enter Your Passkey🤫🔐",
        min_value=date(2000, 1, 1),
        max_value=date(2010, 12, 31),
        value=date(2000, 1, 1)
    )
    if st.button("Enter"):
        if birthday == CORRECT_BIRTHDAY:
            st.session_state.entered = True
            st.rerun()
        else:
            st.error("Are u serious? TRY AGAIN! 😡")
    st.stop()

# -----------------------------
# NAVIGATION
# -----------------------------
page = st.sidebar.radio("Navigate", [
    "🎂 Happy Birthday",
    "💌 Love Letter Generator",
    "🐾 Mood Care Companion",
    "😼 Compatibility Analyzer",
])

# -----------------------------
# 🎂 BIRTHDAY PAGE
# -----------------------------
if page == "🎂 Happy Birthday":
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Pacifico&display=swap');

.bday-wrapper { text-align: center; padding: 20px 0 40px 0; }
.bday-main {
    font-family: 'Pacifico', cursive;
    font-size: clamp(48px, 10vw, 90px);
    background: linear-gradient(135deg, #e0ffff, #02c39a, #ffffff, #00a896);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 4s ease infinite, popIn 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    display: block; line-height: 1.2;
    filter: drop-shadow(0 0 30px rgba(2, 195, 154, 0.5));
}
.bday-name {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(36px, 8vw, 72px);
    color: #ffffff;
    text-shadow: 0 0 30px rgba(2, 195, 154, 0.8), 0 0 60px rgba(2, 195, 154, 0.4);
    animation: popIn 0.8s 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) both;
    display: block; margin-top: 10px;
}
@keyframes popIn {
    0%   { opacity: 0; transform: scale(0.5) translateY(30px); }
    100% { opacity: 1; transform: scale(1) translateY(0); }
}
.bday-emoji-row { font-size: 40px; margin: 20px 0; animation: fadeSlideUp 1s 0.6s both; letter-spacing: 8px; }
.bday-message {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(18px, 3vw, 26px);
    color: #e0ffff; line-height: 1.9;
    animation: fadeSlideUp 1s 0.9s both;
    max-width: 600px; margin: 0 auto; padding: 0 20px;
}
@keyframes fadeSlideUp {
    0%   { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}
.bday-card {
    background: rgba(0, 128, 128, 0.15);
    border: 1px solid rgba(2, 195, 154, 0.4);
    border-radius: 24px; backdrop-filter: blur(16px);
    padding: 35px; margin: 30px auto; max-width: 620px;
    box-shadow: 0 0 40px rgba(2, 195, 154, 0.15), inset 0 0 40px rgba(2, 195, 154, 0.05);
    animation: fadeSlideUp 1s 1.2s both;
}
.bday-wishes { font-size: 15px; color: rgba(224, 255, 255, 0.85); line-height: 2; text-align: left; }
.bday-wishes span { display: block; padding: 6px 0; border-bottom: 1px solid rgba(2, 195, 154, 0.15); }
.bday-wishes span:last-child { border-bottom: none; }
.bday-footer {
    font-family: 'Dancing Script', cursive; font-size: 22px;
    color: #02c39a; margin-top: 30px;
    animation: fadeSlideUp 1s 1.5s both;
    text-shadow: 0 0 20px rgba(2, 195, 154, 0.6);
}
.confetti-row {
    font-size: 28px;
    animation: bounce 1s ease infinite alternate, fadeSlideUp 1s 1.8s both;
    display: inline-block; letter-spacing: 5px;
}
@keyframes bounce {
    from { transform: translateY(0px); }
    to   { transform: translateY(-8px); }
}
</style>

<div class='bday-wrapper'>
    <span class='bday-main'>Happy Birthday</span>
    <span class='bday-name'>my love 🎂</span>
    <p class='bday-message' style ='font-size: 20px;'>
        Another year of you existing in this world<br>
        and somehow I still can't believe we have made it this far.
    </p>
    <div class='bday-card'>
        <div class='bday-wishes'>
            <p class='bday-message' style ='font-size: 28px;'>
                On this special day I wanted to make u a special gift to show you how much you mean to me, 
                and I dont even think it will ever be enough to express my feelings for you! 
                Mina, you mean the whole world to me. You are the reason I smile, laugh and find hope in the little things we do.
                Our relationship is the one thing i will always remember till the day i die, it holds so much memories and meaning.
                Minaaaa enta mn aktr el hagat el bgd mfesh menha etnen fel donia, this love won't ever be replaced mahma hasal fel hyah w aked
                msh hygy zyo!! ana msh 3arfa ezay enta bgd had helw awy kda mn bara w mn gwa w bgd u r perfect in every single thing a human can do.
                lw a3adt a3ed momyzatk msh hakhlas bs bgd u r one of a kind ya toteee.I truly wish you the happiest birthday ever, a one where you feel the most loved because you are.
                Wishing you the happiest life as well, a life that we both dream of. 
                No words will ever be enough for you, I feel like I want to keep writing till tomorrow.
                But i will leave the rest of my feelings for other letters and more reminders for you, that you have my whole heart forever and always.
        <br>
        I love you more than anything in the whole universe.❤️
    </p>
        </div>
    </div>
    <p class='bday-message' style='margin-top: 10px; font-size: 26px;'>
        Thank you for being you.<br>
        Thank you for letting me love you.<br>
        Happy birthday, my favourite person on earth.
    </p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 💌 Love Letter Generator
# -----------------------------
elif page == "💌 Love Letter Generator":
    st.header("💌 A Letter For You")

    if st.button("Generate Letter"):
        letter = random.choice(love_letters)
        st.markdown(f"<div class='glass' style='white-space: pre-line;'>{letter}</div>", unsafe_allow_html=True)



elif page == "🐾 Mood Care Companion":
    st.header("Mood Analysis Engine")
    text = st.text_area("Describe how you feel... (write a few sentences for best results 🩵)")

    if st.button("Analyze Mood"):
        mood_idx, confidence, polarity, subjectivity = analyze_mood(text)
        mood_type = MOOD_LABELS[mood_idx]
        result = MOOD_RESPONSES[mood_type]

        cat_gifs = {
            "Happy":      "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
            "Sad":        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGJrdnlleXh4YWlpdjlmYWRzYXZlNHVoNDJhbjl2cmJiOGt4OWF3ayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/fFa05KbZowXiEIyRse/giphy.gif",
            "Low Energy": "https://media.giphy.com/media/3SeYw59KBJGXJzKvBq/giphy.gif",
            "Good":       "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3czczeDh1azJoOWp3Nm5zMTdoZ242Z2pzbmZzM3ZtMHo3bnB1cjI3MCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/15UbO1LY4O2Fxw8gnI/giphy.gif",
            "Devastated": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGJrdnlleXh4YWlpdjlmYWRzYXZlNHVoNDJhbjl2cmJiOGt4OWF3ayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/901mxGLGQN2PyCQpoc/giphy.gif",
            "Anxious":    "https://media.giphy.com/media/3SeYw59KBJGXJzKvBq/giphy.gif",
        }
        gif_url = cat_gifs.get(mood_type, cat_gifs["Good"])

        # Confidence bar colors
        bar_color = {
            "Happy": "#02c39a", "Good": "#00a896",
            "Neutral": "#008080", "Low Energy": "#006666",
            "Anxious": "#FF8C69", "Sad": "#6495ED", "Devastated": "#4169E1"
        }.get(mood_type, "#02c39a")

        st.markdown(f"""
<div class='glass' style='display:flex; align-items:center; gap:20px;'>
    <img src='{gif_url}' width='150' style='border-radius:12px;'>
    <div style='flex:1'>
        <b>The Ai thinks you are:</b> {mood_type}<br>
         <div style='flex:1'>
        <b>Percentage of the model :</b> {confidence:.1f}%<br>
        <div style='background:rgba(0,0,0,0.2); border-radius:10px; margin:6px 0 10px 0; height:10px;'>
            <div style='width:{confidence}%; background:{bar_color}; height:10px; border-radius:10px; transition:width 1s ease;'></div>
        </div>
        <b>Affirmation:</b> {result['affirmation']}<br>
        <b>Action:</b> {result['action']}
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 😼 Compatibility Analyzer
# -----------------------------
elif page == "😼 Compatibility Analyzer":
    st.header("How Compatible Are We Right Now? 🩵")
    st.markdown("<p style='text-align:center; color:#e0ffff; opacity:0.8;'>be honest...</p>", unsafe_allow_html=True)

    mood_val = st.slider("😊 How's your mood?",        0.0, 1.0, 0.7)
    sleep    = st.slider("😴 How well did you sleep?", 0.0, 1.0, 0.8)
    hunger   = st.slider("🍕 How hungry are you?",     0.0, 1.0, 0.5)
    battery  = st.slider("🔋 Social battery level?",   0.0, 1.0, 0.6)

    if st.button("Calculate Our Vibe ✨"):
        features = np.array([[mood_val, sleep, hunger, battery]])
        score = model.predict(features)[0]
        score = min(max(score, 0), 100)

        cuddle    = min(score + 5, 100)
        hiss      = max(0, 100 - score)
        kiss_prob = min(score * 1.1, 100)

        if score >= 80:
            emoji   = "🥰"
            verdict = "Absolutely obsessed with each other right now"
            vibe    = "Dangerous levels of cuteness incoming. Hold each other immediately."
            color   = "#02c39a"
        elif score >= 60:
            emoji   = "😊"
            verdict = "Pretty great actually"
            vibe    = "Good vibes, soft energy. Perfect for a walk or watching something together."
            color   = "#00a896"
        elif score >= 40:
            emoji   = "😐"
            verdict = "Neutral but fixable"
            vibe    = "Maybe eat something first. Food fixes everything."
            color   = "#008080"
        elif score >= 20:
            emoji   = "😴"
            verdict = "Someone needs a nap"
            vibe    = "Low energy mode. Quiet time together still counts."
            color   = "#006666"
        else:
            emoji   = "🙈"
            verdict = "chaotic but we make it work"
            vibe    = "Someone is hungry AND tired. Order food. Now."
            color   = "#004d4d"

        output_html  = "<div style='text-align:center; padding:30px; background:rgba(0,128,128,0.2); border-radius:20px; backdrop-filter:blur(12px); border:1px solid rgba(0,200,180,0.3);'>"
        output_html += "<div style='font-size:64px; margin-bottom:10px;'>" + emoji + "</div>"
        output_html += "<div style='font-size:28px; font-weight:700; color:" + color + "; margin-bottom:6px;'>" + f"{score:.1f}% Compatible" + "</div>"
        output_html += "<div style='font-size:18px; color:#e0ffff; margin-bottom:20px; font-style:italic;'>" + verdict + "</div>"
        output_html += "<div style='background:rgba(0,0,0,0.25); border-radius:20px; height:14px; margin:0 auto 24px auto; max-width:500px;'>"
        output_html += "<div style='width:" + f"{score:.1f}" + "%; background:linear-gradient(90deg,#008080," + color + "); height:14px; border-radius:20px;'></div></div>"
        output_html += "<div style='display:flex; justify-content:center; gap:16px; flex-wrap:wrap; margin-bottom:20px;'>"
        output_html += "<div style='background:rgba(0,128,128,0.3); border:1px solid rgba(2,195,154,0.4); border-radius:50px; padding:8px 18px; font-size:14px; color:#e0ffff;'>🤗 Cuddle Prob: <b>" + f"{cuddle:.1f}%" + "</b></div>"
        output_html += "<div style='background:rgba(0,128,128,0.3); border:1px solid rgba(2,195,154,0.4); border-radius:50px; padding:8px 18px; font-size:14px; color:#e0ffff;'>😼 Hiss Level: <b>" + f"{hiss:.1f}%" + "</b></div>"
        output_html += "<div style='background:rgba(0,128,128,0.3); border:1px solid rgba(2,195,154,0.4); border-radius:50px; padding:8px 18px; font-size:14px; color:#e0ffff;'>💋 Kiss Prob: <b>" + f"{kiss_prob:.1f}%" + "</b></div>"
        output_html += "</div>"
        output_html += "<div style='background:rgba(0,80,80,0.4); border-radius:14px; padding:14px 20px; font-size:15px; color:#e0ffff; border:1px solid rgba(2,195,154,0.2);'>🩵 &nbsp; " + vibe + "</div>"
        output_html += "</div>"

        st.markdown(output_html, unsafe_allow_html=True)