import streamlit as st
import openai

openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

def get_llm_feedback(answer):
    prompt = f"""
    You are an expert interview coach. Analyze the following interview answer and provide feedback on:
    - Clarity
    - Confidence
    - Relevance
    - Technical Depth
    - Suggestions for improvement

    Give concise, actionable feedback.Also give a score from 1 to 10 based on the overall quality of the answer.
    Please provide a sample answer on how can it be improved.
    Answer:
    \"\"\"{answer}\"\"\"
    """
    response = openai.ChatCompletion.create(
        model="openrouter/gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
        )
    print(response)
    return response['choices'][0]['message']['content']

# Streamlit UI
st.title("🧠 Interview Feedback Bot (LLM Powered)")
user_input = st.text_area("Type your interview answer here:", height=200)

if st.button("Get Feedback"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            feedback = get_llm_feedback(user_input)
        st.subheader("📝 Feedback")
        st.write(feedback)
    else:
        st.warning("Please enter your answer before clicking.")
