import streamlit as st

st.title("🧠 Simple Quiz App")

# Questions and answers
quiz_data = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who developed Python?",
        "options": ["Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup", "James Gosling"],
        "answer": "Guido van Rossum"
    }
]

# Track score
score = 0

# Store submitted state
if "submitted" not in st.session_state:
    st.session_state.submitted = False

user_answers = []

# Show questions
for i, q in enumerate(quiz_data):
    st.subheader(f"Q{i+1}: {q['question']}")
    selected = st.radio(f"Select your answer:", q["options"], key=f"q{i}")
    user_answers.append(selected)

# Submit button
if st.button("Submit Answers"):
    st.session_state.submitted = True
    for i, q in enumerate(quiz_data):
        if user_answers[i] == q["answer"]:
            score += 1

# Show results
if st.session_state.submitted:
    st.success(f"🎉 You got {score} out of {len(quiz_data)} correct!")
    for i, q in enumerate(quiz_data):
        correct = "✅ Correct" if user_answers[i] == q["answer"] else f"❌ Wrong (Correct: {q['answer']})"
        st.write(f"Q{i+1}: {correct}")

