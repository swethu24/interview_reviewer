import fitz
import spacy
from sentence_transformers import SentenceTransformer, util

nlp = spacy.load("en_core_web_sm")
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def extract_entities(text):
    doc = nlp(text)
    entities = {
        "ORG": [],
        "PERSON": [],
        "GPE": [],
        "DATE": [],
        "EDUCATION": [],
        "SKILLS": []
    }
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)
    return entities


def match_jobs(resume_text, job_descriptions):
    resume_embedding = embedder.encode(resume_text, convert_to_tensor=True)
    job_scores = []
    for job in job_descriptions:
        job_embedding = embedder.encode(job, convert_to_tensor=True)
        score = util.cos_sim(resume_embedding, job_embedding).item()
        job_scores.append((job, score))
    job_scores.sort(key=lambda x: x[1], reverse=True)
    return job_scores