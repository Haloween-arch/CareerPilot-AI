import pdfplumber
from docx import Document
import re


def clean_resume_text(text: str):
    """
    Clean and normalize extracted resume text.
    """

    # Fix missing spaces between lowercase and uppercase words
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)

    # Fix words stuck together around punctuation
    text = re.sub(r"([a-zA-Z])([0-9])", r"\1 \2", text)
    text = re.sub(r"([0-9])([a-zA-Z])", r"\1 \2", text)

    # Normalize bullet points
    text = text.replace("•", "\n• ")
    text = text.replace("–", "\n- ")

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Restore line breaks for readability
    text = re.sub(r"(Education|Experience|Projects|Skills|Technical Skills|Certifications|Achievements)", r"\n\n\1", text)

    return text.strip()


def parse_resume(file_path):

    text = ""

    if file_path.endswith(".pdf"):

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

    elif file_path.endswith(".docx"):

        doc = Document(file_path)

        text = "\n".join([p.text for p in doc.paragraphs])

    else:
        raise Exception("Unsupported file format")

    # Clean extracted text
    text = clean_resume_text(text)

    return text