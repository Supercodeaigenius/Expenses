import streamlit as st
"""Build a deterministic set of mixed-operation maths questions.

    The question type rotates through addition, subtraction, multiplication,
    and division so the quiz has variety while keeping integer answers.
"""

def _generate_questions(total_questions: int = 100):

    questions = []
    for idx in range(1, total_questions + 1):
        operation = idx % 4
        if operation == 0:
            left = 5 + idx
            right = 2 + (idx % 9)
            prompt = f"{left} + {right}"
            answer = left + right
        elif operation == 1:
            left = 15 + idx
            right = 3 + (idx % 8)
            prompt = f"{left} - {right}"
            answer = left - right
        elif operation == 2:
            left = 2 + (idx % 11)
            right = 2 + (idx % 9)
            prompt = f"{left} x {right}"
            answer = left * right
        else:
            denominator = 2 + (idx % 8)
            quotient = 2 + (idx % 10)
            left = denominator * quotient
            prompt = f"{left} / {denominator}"
            answer = quotient

        questions.append({"prompt": prompt, "answer": answer})

    return questions

"""Render the quiz UI and manage all quiz interactions/state.

    This function initializes session state once, shows the current question,
    records the user's answer, handles navigation, evaluates correctness, and
    displays overall progress/score.
"""
def render_math_quiz_page():

    total_questions = 100

    # Initialize quiz state once per session.
    if "math_quiz_questions" not in st.session_state:
        st.session_state.math_quiz_questions = _generate_questions(total_questions)
    if "math_quiz_answers" not in st.session_state:
        st.session_state.math_quiz_answers = [None] * total_questions
    if "math_quiz_index" not in st.session_state:
        st.session_state.math_quiz_index = 0

    current_index = st.session_state.math_quiz_index
    questions = st.session_state.math_quiz_questions
    answers = st.session_state.math_quiz_answers
    current_question = questions[current_index]

    st.markdown("<div class='section-title'>Maths Quiz</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-sub'>Solve all 100 questions and track your score as you go.</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div class='card'><h4>Question {current_index + 1} of {total_questions}</h4><p><strong>{current_question['prompt']} = ?</strong></p></div>",
        unsafe_allow_html=True,
    )

    # Keep one answer field per question and persist answers by index.
    answer_key = f"math_quiz_answer_{current_index}"
    existing_answer = answers[current_index]
    default_value = "" if existing_answer is None else str(existing_answer)
    user_answer = st.text_input("Your answer", value=default_value, key=answer_key)

    normalized = user_answer.strip()
    if normalized == "":
        answers[current_index] = None
    else:
        try:
            answers[current_index] = int(normalized)
        except ValueError:
            answers[current_index] = None
            st.warning("Please enter a whole number.")

    # Place all controls on one horizontal line.
    button_cols = st.columns([1, 1, 2, 1])
    with button_cols[0]:
        previous_clicked = st.button(
            "Previous",
            disabled=current_index == 0,
            use_container_width=True,
        )
    with button_cols[1]:
        next_clicked = st.button(
            "Next",
            disabled=current_index == total_questions - 1,
            use_container_width=True,
        )
    with button_cols[2]:
        check_clicked = st.button(
            "Check Answer & Calculate Score",
            type="primary",
            use_container_width=True,
        )
    with button_cols[3]:
        back_clicked = st.button("Back to Home", use_container_width=True)

    # Validate the current answer and show overall score snapshot.
    if check_clicked:
        if answers[current_index] is None:
            st.warning("Please enter a whole number before checking your answer.")
        elif answers[current_index] != current_question["answer"]:
            st.error("That answer is wrong. Please try again.")
        else:
            st.success("Correct answer. Nice work!")

        correct = sum(
            1
            for idx, question in enumerate(questions)
            if answers[idx] is not None and answers[idx] == question["answer"]
        )
        answered = sum(1 for answer in answers if answer is not None)
        st.info(f"Score: {correct}/{total_questions} | Answered: {answered}/{total_questions}")

    # Navigation actions rerun to refresh the page at the new state.
    if previous_clicked:
        st.session_state.math_quiz_index -= 1
        st.rerun()
    if next_clicked:
        st.session_state.math_quiz_index += 1
        st.rerun()
    if back_clicked:
        st.query_params.clear()
        st.rerun()
