from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_reference_notes(path="data/agriculture_notes.txt"):
    text = Path(path).read_text(encoding="utf-8")
    chunks = [chunk.strip() for chunk in text.split("\n---\n") if chunk.strip()]
    return chunks

def retrieve_notes(query, notes, top_k=3):
    """Small local TF-IDF retriever for the prototype; not a verified diagnosis engine."""
    if not notes or not query.strip():
        return []
    corpus = [query] + notes
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words=None)
    matrix = vectorizer.fit_transform(corpus)
    scores = cosine_similarity(matrix[0:1], matrix[1:]).flatten()
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    return [{"text": notes[i], "score": float(score)} for i, score in ranked[:top_k] if score > 0]
