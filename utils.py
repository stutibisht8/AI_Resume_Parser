import pdfplumber
import docx
import re
# -----------------------------------------
# PDF TEXT EXTRACTION
# -----------------------------------------
def extract_pdf(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except:
        return ""
    return text
# -----------------------------------------
# DOCX TEXT EXTRACTION
# -----------------------------------------
def extract_docx(file):
    text = ""
    try:
        document = docx.Document(file)
        for para in document.paragraphs:
            text += para.text + "\n"
    except:
        return ""
    return text
# -----------------------------------------
# MAIN FUNCTION
# -----------------------------------------
def extract_text(uploaded_file):
    filename = uploaded_file.name.lower()
    if filename.endswith(".pdf"):
        return extract_pdf(uploaded_file)
    elif filename.endswith(".docx"):
        return extract_docx(uploaded_file)
    return ""
# -----------------------------------------
# EMAIL DETECTION
# -----------------------------------------
def extract_email(text):
    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )
    if emails:
        return emails[0]
    return "Not Found"
# -----------------------------------------
# PHONE NUMBER DETECTION
# -----------------------------------------
def extract_phone(text):
    phones = re.findall(
        r"\+?\d[\d\s\-]{8,15}\d",
        text
    )
    if phones:
        return phones[0]
    return "Not Found"
# -----------------------------------------
# SKILLS DETECTION
# -----------------------------------------
SKILLS = [
    "Python",
    "Java",
    "C++",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Science",
    "Power BI",
    "Excel",
    "Git",
    "GitHub",
    "Docker",
    "AWS",
    "Streamlit",
    "Flask",
    "Django",
    "HTML",
    "CSS",
    "JavaScript",
    "Pandas",
    "NumPy",
    "TensorFlow",
    "PyTorch",
    "Tableau",
    "MongoDB",
    "MySQL"
]
def extract_skills(text):
    found_skills = []
    text = text.lower()
    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)
    return found_skills
# -----------------------------------------
# ATS SCORE
# -----------------------------------------
def calculate_ats_score(skills):
    score = 0
    # Skills Score
    score += min(len(skills)*5,50)
    # Bonus Points
    if len(skills) >= 8:
        score += 20
    elif len(skills) >= 5:
        score += 15
    elif len(skills) >= 3:
        score += 10
    # Base Score
    score += 30
    if score > 100:
        score = 100
    return score
# -----------------------------------------
# MISSING SKILLS
# ---------------------------------------
def missing_skills(found_skills):
    missing = []
    for skill in SKILLS:
        if skill not in found_skills:
            missing.append(skill)
    return missing[:10]
# -----------------------------------------
# JOB ROLE RECOMMENDATION
# -----------------------------------------
def suggest_job_roles(skills):
    roles = []
    if "Python" in skills:
        roles.append(
            "Python Developer"
        )
    if "Machine Learning" in skills:
        roles.append(
            "Machine Learning Engineer"
        )
    if "Artificial Intelligence" in skills:
        roles.append(
            "AI Engineer"
        )
    if "SQL" in skills:
        roles.append(
            "Data Analyst"
        )
    if "Power BI" in skills:
        roles.append(
            "Business Intelligence Analyst"
        )
    if "Streamlit" in skills:
        roles.append(
            "AI Application Developer"
        )
    if len(roles) == 0:
        roles.append(
            "Software Developer"
        )
    return roles
# -----------------------------------------
# RESUME IMPROVEMENT
# -----------------------------------------
def improvement_suggestions(
        ats_score,
        missing
):
    suggestions = []
    if ats_score < 70:
        suggestions.append(
            "Improve your ATS score by adding more technical skills."
        )
    if len(missing) > 5:
        suggestions.append(
            "Include relevant industry skills in your resume."
        )
    suggestions.append(
        "Add your GitHub profile link."
    )
    suggestions.append(
        "Mention internships and projects clearly."
    )
    suggestions.append(
        "Use proper section headings."
    )
    suggestions.append(
        "Keep your resume limited to one or two pages."
    )
    return suggestions