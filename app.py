import streamlit
import streamlit as st
from textblob import TextBlob
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def generate_feedback(answer):
    return (
        "Feedback:\n"
        "- Clarity: Good\n"
        "- Confidence: Moderate\n"
        "- Relevance: High\n"
        "- Technical Depth: Needs improvement\n"
        "Suggestions: Try to elaborate more on technical aspects and structure your answer clearly."
    )

def analyze_sentiment(answer):
    blob = TextBlob(answer)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

def analyze_grammar(answer):
    doc = nlp(answer)
    return len(list(doc.sents)), len(doc), sum(1 for token in doc if token.pos_ == "X")

st.title("🧠 Interview Feedback Bot")
st.write("Enter your interview answer below to receive feedback:")

user_input = st.text_area("Your Answer", height=200)

if st.button("Analyze"):
    if user_input.strip():
        st.subheader("🔍 Analysis")
        polarity, subjectivity = analyze_sentiment(user_input)
        st.write(f"**Sentiment Polarity:** {polarity:.2f}")
        st.write(f"**Subjectivity:** {subjectivity:.2f}")

        num_sentences, num_tokens, num_errors = analyze_grammar(user_input)
        st.write(f"**Sentences:** {num_sentences}")
        st.write(f"**Words/Tokens:** {num_tokens}")
        st.write(f"**Potential Grammar Issues:** {num_errors}")

        st.subheader("📝 LLM Feedback")
        st.text(generate_feedback(user_input))
    else:
        st.warning("Please enter your answer before clicking Analyze.")
