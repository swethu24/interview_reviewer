import streamlit as st
import helper

st.title("Resume Analyzer & Job Matcher")

uploaded_file = st.file_uploader("Upload your resume in pdf format", type=["pdf"])
job_input = st.text_area("Paste job descriptions (one per line)")

if uploaded_file and job_input:
    with st.spinner("Processing resume..."):
        resume_text = helper.extract_text_from_pdf(uploaded_file)
        entities = helper.extract_entities(resume_text)
        job_descriptions = job_input.strip().split("\n")
        matches = helper.match_jobs(resume_text, job_descriptions)

    st.subheader("Extracted Key Words from Your Resume")
    for _,words in entities.items():
        st.write(",".join(words) if words else "")

    st.subheader("Job Descripton Top 5 Match Scores")
    for job, score in matches[:5]:
        st.markdown(f"**Score:** {score:.2f}")
        st.write(job)
        st.markdown("---")
