# 🚀 CareerPilot AI

#### AI Resume Analyzer, ATS Optimizer and Career Guidance Platform

CareerPilot AI is an AI-powered resume analysis platform that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS), identify skill gaps, and discover relevant job opportunities.

The platform analyzes a resume against a job description and generates improvement suggestions, predicts ATS compatibility, recommends skills to learn, and suggests relevant job roles.

---

# ✨ Features

#### AI Resume Analysis

Upload a resume and compare it with a job description to receive intelligent insights.

- Resume parsing for PDF and DOCX
- AI-powered resume improvement suggestions
- Line-by-line optimization guidance
- Resume vs Job Description comparison

---

#### ATS Score Prediction

Predict how well a resume matches a job description.

The system uses:

- Keyword matching
- Semantic similarity using sentence embeddings

Example:

```
ATS Score Before: 47%
Predicted ATS Score After Improvements: 81%
```

---

#### Skill Gap Detection

Detect missing skills required for the target job role.

Example Missing Skills:

- Docker
- Microservices
- System Design
- CI/CD

---

#### Learning Recommendations

CareerPilot suggests learning resources for missing skills.

Resources include:

- YouTube tutorials
- Coursera courses
- Developer roadmaps

Example:

Skill: Docker

- YouTube tutorial link
- Course link
- Developer roadmap

---

#### DSA Preparation Plan

Generate recommended Data Structures and Algorithms topics to improve technical interview readiness.

Example topics:

- Graphs
- Dynamic Programming
- System Design Basics

---

#### Job Recommendations

Suggest relevant job roles based on resume analysis.

Example:

```
Full Stack Developer — 91% match
Backend Engineer — 84% match
React Developer — 78% match
```

Each recommendation includes a LinkedIn job search link.

---

# 🏗 Architecture

Frontend (React)

↓

FastAPI Backend

↓

Resume Parser (PDF / DOCX)

↓

Job Description Keyword Extractor

↓

ATS Score Engine

↓

Skill Gap Analyzer

↓

AI Suggestion Engine (Gemini)

↓

Job Recommendation Engine

---

# 🛠 Tech Stack

#### Backend

- FastAPI
- Python
- Sentence Transformers
- Scikit-learn
- pdfplumber
- python-docx

#### AI & NLP

- Google Gemini API
- Semantic embeddings
- Cosine similarity scoring

#### Frontend

- React
- Tailwind CSS

---

# 📂 Project Structure

```
backend
│
├── app
│   ├── api
│   │   └── routes_optimizer.py
│   │
│   ├── services
│   │   ├── resume_parser.py
│   │   ├── jd_analyzer.py
│   │   ├── ats_score.py
│   │   ├── optimizer_service.py
│   │   └── skill_gap.py
│   │
│   ├── embeddings
│   │   └── similarity.py
│   │
│   ├── llm
│   │   │
│   │   └── gemini_client.py
│   │
│   └── main.py
│
├── uploads
│
└── requirements.txt
```

---

# ⚙ Installation

#### Clone Repository

```bash
git clone https://github.com/yourusername/careerpilot-ai.git
cd careerpilot-ai
```

---

#### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Mac / Linux

```
source venv/bin/activate
```

---

#### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file and add:

```
GEMINI_API_KEY=your_api_key_here
```

---

# ▶ Run the Server

```bash
python -m uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates API docs.

```
http://127.0.0.1:8000/docs
```

---

# 🔌 API Endpoint

#### Analyze Resume

```
POST /optimize-resume
```

Inputs:

- Resume file (PDF or DOCX)
- Job Description text

Example Response:

```
ats_before
predicted_ats_after
matched_skills
missing_skills
suggestions
learning_resources
dsa_plan
recommended_jobs
```

---

# 🔮 Future Improvements

- LinkedIn job scraping
- Resume auto-tailoring for each job
- AI resume generation with a one-page template
- Automated job application assistant
- GitHub profile integration
- Personalized career roadmap

---

# 📄 License

MIT License

---

⭐ If you found this project useful, consider starring the repository!
