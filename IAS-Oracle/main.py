import streamlit as st
from utils.pdf_extractor import extract_text_from_pdf
from summarizer.summarize_news import summarize_pdf
from evaluator.evaluate_answers import evaluate_answer
from question_generator.assignment_generator import generate_assignment
from utils.audio_summary import generate_audio_summary
from utils.api_calls import get_news_summary

# Streamlit UI setup
st.title("IAS Oracle")
st.write("Welcome to IAS Oracle! Upload PDF and perform analysis.")

# Upload PDF file
pdf_file = st.file_uploader("Upload Newspaper PDF", type=["pdf"])
if pdf_file is not None:
    with open("data/sample_newspaper.pdf", "wb") as f:
        f.write(pdf_file.read())

    # Summarize the PDF using an API
    summary_mode = st.selectbox("Select Summary Mode", ["Bullet Points", "Detailed"])
    summary = summarize_pdf("data/sample_newspaper.pdf", mode=summary_mode.lower())
    st.write("Summary:")
    st.write(summary)

    # Use external API for summary (optional)
    if st.checkbox("Use external API for news summary"):
        api_summary = get_news_summary("data/sample_newspaper.pdf", summary_mode)
        st.write("API Summary:")
        st.write(api_summary)

# Assignment Generation
topic = st.text_input("Enter Topic for Assignment:")
if st.button("Generate Assignment"):
    assignment = generate_assignment("data/sample_newspaper.pdf", topic)
    st.write("Generated Assignment:")
    st.write(assignment)

# Answer Evaluation
user_answer = st.text_area("Enter Your Answer for Evaluation:")
if st.button("Evaluate Answer"):
    model_answer = "Model answer for comparison."  # Replace with a model answer.
    feedback = evaluate_answer(user_answer, model_answer)
    st.write("Feedback:")
    st.write(feedback)

# Audio Summary
if st.button("Generate Audio Summary"):
    generate_audio_summary(summary, "audio_summary.mp3")
    st.write("Audio summary generated!")

