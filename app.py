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
You are enough and you are so so loved. I wish I could give you the whole world as a gift,
just to show how thankful i am for you.
Never forget that.
"""
]



# -----------------------------
# MOOD ANALYSIS
# -----------------------------
def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity

def mood_response(polarity):
    if polarity < -0.5:
        return {
            "type": "Devastated",
            "affirmation": "Just take a deep breath... Remeber nothing deserves to be angry. ",
            "action": "Drink some water and breathe slowly till you are calm."
            
        }
    elif polarity < -0.3:
        return {
            "type": "Sad",
            "affirmation": "You don't have to carry everything alone.",
            "action": "Wrap yourself in something warm and breathe slowly."
        }
    elif polarity < -0.1:
        return {
            "type": "Anxious",
            "affirmation": "Everything will be okay i promise.",
            "action": "Call me!!!"
        }
    elif polarity < 0:
        return {
            "type": "Low Energy",
            "affirmation": "It's okay to move gently today.",
            "action": "Drink water and take a small break."
        }
    elif polarity < 0.4:
        return {
            "type": "Good",
            "affirmation": "Steady days are the best days.",
            "action": "Do one small thing that makes you smile."
        }
    else:
        return {
            "type": "Happy",
            "affirmation": "Your energy is beautiful today.",
            "action": "Channel that into something creative."
        }

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
<p class='typewriter' style='animation-delay: 6s'>So, Happy birthday to my favourit human on earth❤️</p>
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
        st.error("NOOOO TRY AGAIN DUMMY!😡")
        
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
        and somehow I still can't believe I get to be yours.
    </p>
    <div class='bday-card'>
        <div class='bday-wishes'>
            <p class='bday-message' style ='font-size: 28px;'>
                On this special day I wanted to make u a special gift to show you how much you mean to me, 
                and I dont even think it will ever be enough to express my feelings for you! 
                Mina, you mean the whole world to me. You are the reason I smile, laugh and find hope in the little things we do.
                I truly wish you the happiest birthday ever, a one where you feel the most loved because you are.
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

# -----------------------------
# 🐾 Mood Care
# -----------------------------
elif page == "🐾 Mood Care Companion":
    st.header("Mood Analysis Engine")
    text = st.text_area("Describe how you feel")

    if st.button("Analyze Mood"):
        polarity, subjectivity = analyze_mood(text)
        result = mood_response(polarity)
        cat_gifs = {
            "Happy": "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
            "Sad": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3YwbTFtbTVreGIzejVtMmU4NHVnMXdqd2N6dDk3bDY4N29rNHp6dSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/MDJ9IbxxvDUQM/giphy.gif",
            "Low Energy": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXN0b3Nma3JkYWhuenZsbWlvNHRhc2p5NzVmM3B6bDljdTF1eXIwMiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3SeYw59KBJGXJzKvBq/giphy.gif",
            "Neutral": "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3czRzczd1cWdlaWllejdhNXU2OGZ1bWFlZzgzYXR5N2Fwb2NyYXdxZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/29czd4FQNdnkJZ1npy/giphy.gif",
        }
        gif_url = cat_gifs.get(result["type"], cat_gifs["Neutral"])

        st.markdown(f"""
<div class='glass' style='display:flex; align-items:center; gap:20px;'>
    <img src='{gif_url}' width='150' style='border-radius:12px;'>
    <div>
        <b>Detected Mood:</b> {result['type']}<br>
        <b>Affirmation:</b> {result['affirmation']}<br>
        <b>Action:</b> {result['action']}<br>
        <b>Cat Wisdom:</b> {result['cat']}
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 😼 Compatibility Analyzer
# -----------------------------
elif page == "😼 Compatibility Analyzer":
    st.header("Compatibility Prediction Model")

    mood_val = st.slider("Mood Level", 0.0, 1.0, 0.7)
    sleep = st.slider("Sleep Quality", 0.0, 1.0, 0.8)
    hunger = st.slider("Hunger Level", 0.0, 1.0, 0.5)
    battery = st.slider("Social Battery", 0.0, 1.0, 0.6)

    if st.button("Predict Compatibility"):
        features = np.array([[mood_val, sleep, hunger, battery]])
        score = model.predict(features)[0]

        st.markdown(f"<div class='glass'>"
                    f"<b>Predicted Compatibility:</b> {score:.2f}%<br>"
                    f"Cuddle Probability: {min(score+5,100):.1f}%<br>"
                    f"</div>", unsafe_allow_html=True)
