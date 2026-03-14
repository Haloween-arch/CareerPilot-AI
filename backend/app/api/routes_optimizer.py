from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import shutil
import os
import uuid

from app.services.resume_parser import parse_resume
from app.services.jd_analyzer import extract_keywords
from app.services.optimizer_service import analyze_resume_and_suggest
from app.services.ats_score import calculate_ats_score

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/optimize-resume")
async def optimize_resume(
    resume: UploadFile = File(...),
    jd: str = Form(...)
):

    file_path = None

    try:

        # Validate JD
        if not jd or len(jd.strip()) < 20:
            raise HTTPException(
                status_code=400,
                detail="Job description is too short"
            )

        # Validate file type
        if not resume.filename.lower().endswith((".pdf", ".docx")):
            raise HTTPException(
                status_code=400,
                detail="Only PDF and DOCX files are supported"
            )

        # Create unique filename
        unique_filename = f"{uuid.uuid4()}_{resume.filename}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)

        # Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        # Parse resume text
        resume_text = parse_resume(file_path)

        if not resume_text or len(resume_text.strip()) < 30:
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from resume"
            )

        # Extract keywords from JD
        keywords = extract_keywords(jd)

        # ATS score before suggestions
        ats_before = calculate_ats_score(resume_text, keywords)

        # Run AI analysis
        analysis = analyze_resume_and_suggest(resume_text, jd)

        return {
            "resume_text": resume_text,

            "ats_before": ats_before,
            "predicted_ats_after": analysis.get("predicted_ats_after", ats_before),

            "matched_skills": analysis["skill_gap"]["matched_skills"],
            "missing_skills": analysis["skill_gap"]["missing_skills"],

            "suggestions": analysis.get("suggestions", []),

            "learning_resources": analysis.get("learning_resources", []),

            "dsa_plan": analysis.get("dsa_plan", []),

            "recommended_jobs": analysis.get("job_recommendations", [])
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Resume analysis failed: {str(e)}"
        )

    finally:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)