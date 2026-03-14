import re


# Common technical skills dictionary
TECH_SKILLS = {
    "python","java","c","c++","c#","javascript","typescript",
    "react","angular","vue","node","express","django","flask",
    "spring","springboot","dotnet","aspnet","asp.net",
    "sql","mysql","postgresql","mongodb","redis",
    "docker","kubernetes","aws","azure","gcp",
    "git","github","gitlab","ci","cd","ci/cd",
    "linux","rest","restful","graphql","microservices",
    "system design","distributed systems",
    "machine learning","deep learning","tensorflow","pytorch",
    "nlp","opencv","scikit","pandas","numpy",
    "html","css","bootstrap","tailwind",
    "unit testing","pytest","jest","selenium",
    "entity framework","dependency injection",
    "data structures","algorithms"
}


def normalize_skill(word):
    """
    Normalize common variations.
    """
    word = word.lower()

    replacements = {
        "node.js": "node",
        "nodejs": "node",
        "react.js": "react",
        "reactjs": "react",
        ".net": "dotnet",
        "asp.net": "aspnet",
        "postgres": "postgresql",
        "k8s": "kubernetes"
    }

    return replacements.get(word, word)


def extract_keywords(jd_text):

    # Extract words + technical phrases
    tokens = re.findall(r"[A-Za-z\.\+#]+", jd_text)

    tokens = [normalize_skill(t) for t in tokens]

    extracted = set()

    for token in tokens:

        token = token.lower()

        if token in TECH_SKILLS:
            extracted.add(token)

    # also detect multi-word skills
    jd_lower = jd_text.lower()

    multi_word_skills = [
        "system design",
        "machine learning",
        "deep learning",
        "unit testing",
        "dependency injection",
        "entity framework",
        "data structures"
    ]

    for skill in multi_word_skills:
        if skill in jd_lower:
            extracted.add(skill)

    return list(extracted)