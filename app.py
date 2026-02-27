import streamlit as st
import time

st.set_page_config(page_title="Personality Prediction System", layout="centered")

# ---------------- CSS ----------------
st.markdown("""
<style>
.result-box {
    margin-top: 30px;
    padding: 25px;
    text-align: center;
    font-size: 26px;
    font-weight: bold;
    color: white;
    background: linear-gradient(135deg, #6a11cb, #2575fc);
    border-radius: 16px;
    animation: pop 0.6s ease-in-out;
}
@keyframes pop {
    0% {transform: scale(0.6); opacity: 0;}
    100% {transform: scale(1); opacity: 1;}
}
.warning {
    color: red;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Personality Prediction System")
st.write("Please answer all questions:")

# ---------------- Questions (NO DEFAULT SELECTION) ----------------
q1 = st.radio(
    "Q1. When you get free time, you usually:",
    [
        "A. Try something new or learn a new skill",
        "B. Relax with familiar activities",
        "C. Follow a fixed routine",
        "D. Avoid thinking much and just pass time"
    ],
    index=None,
    key="q1"
)

q2 = st.radio(
    "Q2. In stressful situations, you:",
    [
        "A. Stay calm and think logically",
        "B. Feel slightly anxious but manage",
        "C. Get stressed and overthink",
        "D. Feel very anxious or upset easily"
    ],
    index=None,
    key="q2"
)

q3 = st.radio(
    "Q3. When given a task with a deadline, you:",
    [
        "A. Finish it well before time",
        "B. Plan and complete it on time",
        "C. Do it at the last moment",
        "D. Often delay or struggle to finish"
    ],
    index=None,
    key="q3"
)

q4 = st.radio(
    "Q4. In social situations, you:",
    [
        "A. Love meeting new people and talking",
        "B. Enjoy socializing with known people",
        "C. Prefer small groups or limited interaction",
        "D. Avoid social situations if possible"
    ],
    index=None,
    key="q4"
)

q5 = st.radio(
    "Q5. When someone asks for help, you:",
    [
        "A. Always help, even if it’s inconvenient",
        "B. Help if possible",
        "C. Help only close people",
        "D. Usually avoid getting involved"
    ],
    index=None,
    key="q5"
)

# ---------------- Predict ----------------
if st.button("🔮 Predict Personality"):

    if None in [q1, q2, q3, q4, q5]:
        st.markdown("<p class='warning'>⚠ Please answer all questions.</p>", unsafe_allow_html=True)

    else:
        score = {"A": 3, "B": 2, "C": 1, "D": 0}
        def s(x): return score[x[0]]

        openness = s(q1)
        neuroticism = 3 - s(q2)
        conscientiousness = s(q3)
        extraversion = s(q4)
        agreeableness = s(q5)

        def predict_personality():
            if conscientiousness >= 3 and neuroticism <= 1:
                return "Responsible & Disciplined"
            elif extraversion >= 3 and agreeableness >= 3:
                return "Social & Friendly"
            elif openness >= 3:
                return "Creative & Curious"
            elif neuroticism >= 3:
                return "Emotionally Sensitive"
            elif extraversion <= 1:
                return "Reserved & Independent"
            else:
                return "Balanced Personality"

        with st.spinner("Analyzing your responses..."):
            time.sleep(1)

        result = predict_personality()

        st.markdown(
            f"<div class='result-box'>✨ Your Personality Type<br>{result}</div>",
            unsafe_allow_html=True
        )

# ---------------- TRUE RESET ----------------
if st.button("🔄 Refresh Questionnaire"):
    for key in ["q1", "q2", "q3", "q4", "q5"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()
