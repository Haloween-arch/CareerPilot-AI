from app.embeddings.similarity import semantic_match


def calculate_ats_score(resume_text, jd_keywords):

    if not jd_keywords:
        return 0

    resume_lower = resume_text.lower()

    # -------- Keyword Match Score --------
    keyword_matches = []

    for keyword in jd_keywords:
        if keyword.lower() in resume_lower:
            keyword_matches.append(keyword)

    keyword_score = len(keyword_matches) / len(jd_keywords)


    # -------- Semantic Match Score --------
    semantic_matches = semantic_match(resume_text, jd_keywords)

    semantic_score = len(semantic_matches) / len(jd_keywords)


    # -------- Final ATS Score --------
    # Weighted combination
    final_score = (0.6 * keyword_score) + (0.4 * semantic_score)

    ats_score = final_score * 100

    return round(ats_score, 2)