from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_match(resume_text, jd_keywords):

    matches = []

    resume_embedding = model.encode([resume_text])  # 2D array

    for keyword in jd_keywords:

        keyword_embedding = model.encode([keyword])  # 2D array

        similarity = cosine_similarity(
            resume_embedding,
            keyword_embedding
        )[0][0]

        if similarity > 0.55:
            matches.append(keyword)

    return matches