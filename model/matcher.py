from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume_text, job_desc):
    vectorizer = TfidfVectorizer()
    
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    
    return round(similarity[0][0] * 100, 2)