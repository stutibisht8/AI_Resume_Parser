# AI Resume Parser

AI Resume Parser is a Python and Streamlit-based application that analyzes resumes and provides useful insights for improving resume quality and job readiness.

The application extracts important information from PDF and DOCX resumes, analyzes technical skills, calculates an ATS score, suggests suitable job roles, identifies missing skills, and provides personalized improvement suggestions.

## Features

- Upload resumes in PDF and DOCX formats
- Extract candidate name, email, phone number, LinkedIn, and GitHub profiles
- Detect technical skills from resumes
- Calculate ATS compatibility score
- Suggest suitable job roles
- Identify missing technical skills
- Verify Education, Projects, and Certifications sections
- Estimate interview shortlist probability
- Match resume skills with job descriptions
- View resume analytics through a dashboard
- Export a resume analysis report

## Technologies Used

- Python
- Streamlit
- Regular Expressions
- PDF and DOCX Text Extraction
- HTML and CSS
- Git and GitHub

## Project Structure

```text
AI_Resume_Parser/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
│
└── assets/
    └── background.png
```

## Installation
Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## How It Works

1. Upload a resume in PDF or DOCX format.
2. The application extracts and analyzes the resume content.
3. Technical skills and contact information are detected.
4. An ATS score and interview probability are calculated.
5. Suitable job roles, missing skills, and improvement suggestions are provided.
6. Users can compare their resume with a job description.

## Future Enhancements

- AI-powered resume summarization
- Advanced NLP-based resume analysis
- GPT-based resume feedback
- Multi-language resume support
- Resume comparison with multiple job descriptions

## Author
**Stuti Bisht**
GitHub: https://github.com/stutibisht8
