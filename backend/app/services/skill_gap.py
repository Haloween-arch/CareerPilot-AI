from app.embeddings.similarity import semantic_match

def analyze_skill_gap(resume_text, jd_keywords):

    resume_words = list(set(resume_text.lower().split()))

    matched_keywords = []

    for k in jd_keywords:
        if k.lower() in resume_text.lower():
            matched_keywords.append(k)

    semantic_matches = semantic_match(resume_words, jd_keywords)

    matched = list(set(matched_keywords + semantic_matches))

    missing = []

    for k in jd_keywords:
        if k not in matched:
            missing.append(k)

    return {
        "matched_skills": matched,
        "missing_skills": missing
    }