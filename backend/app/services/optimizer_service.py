from app.llm.gemini_client import generate_response
from app.services.ats_score import calculate_ats_score
from app.services.jd_analyzer import extract_keywords
from app.services.skill_gap import analyze_skill_gap
import json
import re


def extract_json_from_response(response: str):
    """
    Safely extract JSON from LLM output.
    """
    try:
        match = re.search(r"\{.*\}", response, re.DOTALL)
        if match:
            return json.loads(match.group())
        return None
    except:
        return None


def generate_learning_resources(skills):
    """
    Convert skills into learning resources with links.
    """
    resources = []

    for skill in skills[:8]:

        skill_query = skill.replace(" ", "+")

        resources.append({
            "skill": skill,
            "youtube": f"https://www.youtube.com/results?search_query={skill_query}+tutorial",
            "course": f"https://www.coursera.org/search?query={skill_query}",
            "roadmap": f"https://roadmap.sh/{skill_query.lower()}"
        })

    return resources


def generate_job_links(roles, resume_text):
    """
    Convert job titles into LinkedIn search links + match score
    """

    jobs = []

    resume_lower = resume_text.lower()

    for role in roles:

        query = role.replace(" ", "%20")

        role_words = role.lower().split()

        # simple match score
        match_count = sum(1 for w in role_words if w in resume_lower)

        score = 70 + (match_count * 10)

        if score > 95:
            score = 95

        jobs.append({
            "role": role,
            "match_score": score,
            "label": f"{role} — {score}% match",
            "linkedin": f"https://www.linkedin.com/jobs/search/?keywords={query}"
        })

    # sort by best match
    jobs.sort(key=lambda x: x["match_score"], reverse=True)

    return jobs


def analyze_resume_and_suggest(resume_text, jd_text):

    keywords = extract_keywords(jd_text)

    skill_analysis = analyze_skill_gap(resume_text, keywords)

    ats_score = calculate_ats_score(resume_text, keywords)

    prompt = f"""
You are an AI Career Advisor and ATS Resume Reviewer.

Analyze the candidate resume against the job description.

Return ONLY valid JSON.

JSON format:

{{
 "predicted_ats_score": number,

 "suggestions":[
    {{
      "section":"EXPERIENCE | PROJECTS | SUMMARY | SKILLS",
      "current":"exact line from resume",
      "suggested":"improved line",
      "reason":"why this improves ATS score",
      "keyword_added":"ATS keyword added"
    }}
 ],

 "learning_plan":[
   "skill to learn"
 ],

 "dsa_plan":[
   "DSA topic to practice"
 ],

 "job_recommendations":[
   "job role"
 ]
}}

Rules:
- Provide at least 6 resume improvement suggestions
- Suggest improvements line by line
- Add measurable achievements when possible
- Add missing ATS keywords naturally
- Predict ATS score after applying suggestions

Missing Skills:
{skill_analysis['missing_skills']}

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    response = generate_response(prompt)

    data = extract_json_from_response(response)

    if not data:
        data = {
            "predicted_ats_score": ats_score,
            "suggestions": [],
            "learning_plan": [],
            "dsa_plan": [],
            "job_recommendations": [
                "Full Stack Developer",
                "Backend Engineer",
                "React Developer"
            ]
        }

    learning_resources = generate_learning_resources(
        data.get("learning_plan", skill_analysis["missing_skills"])
    )

    job_links = generate_job_links(
        data.get("job_recommendations", []),
        resume_text
    )

    return {
        "ats_before": ats_score,
        "predicted_ats_after": data.get("predicted_ats_score", ats_score),
        "skill_gap": skill_analysis,
        "suggestions": data.get("suggestions", []),
        "learning_resources": learning_resources,
        "dsa_plan": data.get("dsa_plan", []),
        "job_recommendations": job_links
    }