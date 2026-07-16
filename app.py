import streamlit as st
import base64
import random  # Interview probability simulate karne ke liye fallback

# Back-end functions import
from utils import (
    extract_text,
    extract_email,
    extract_phone,
    extract_skills,
    calculate_ats_score,
    suggest_job_roles,
    missing_skills,
    improvement_suggestions
)

# ----------------------------------------
# Streamlit Page Settings & Theme
# ----------------------------------------
st.set_page_config(
    page_title="AI Resume Parser",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------
# Background Styling & CSS Enhancements
# ----------------------------------------
def set_background(image_file):
    try:
        with open(image_file, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()

        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;
            }}
            .section-card {{
                background: rgba(255, 255, 255, 0.05);
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 10px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except:
        pass

set_background("assets/background.png")

# ----------------------------------------
# Sidebar Navigation
# ----------------------------------------
st.sidebar.title("🚀 Career Copilot")
st.sidebar.markdown("---")

app_mode = st.sidebar.radio(
    "Navigation", 
    ["🔍 Deep AI Resume Analyzer", "💼 Job Description Matcher", "📈 Analytics Dashboard", "ℹ️ Project Metadata"]
)

POPULAR_TECH_SKILLS = ["Python", "Java", "SQL", "HTML", "CSS", "JavaScript", "Docker", "AWS", "Git", "C++", "Machine Learning"]

# ----------------------------------------
# Feature 1: Project Metadata Pane
# ----------------------------------------
if app_mode == "ℹ️ Project Metadata":
    st.title("ℹ️ Project Metadata & Architecture")
    st.markdown("""
    ### 🛠️ Core Capabilities Added:
    * **Named Entity Recognition:** Parsing Name, LinkedIn profiles, and GitHub handles.
    * **Section Segmentation:** Extracting Projects, Education blocks, and Certifications.
    * **Predictive Analytics:** Interview Probability index calculation based on comprehensive resume health metrics.
    """)
    st.info("💡 Pro-Tip: Deploy this script on GitHub Pages or Streamlit Community Cloud for a direct portfolio link!")

# ----------------------------------------
# Feature 2: Core Deep Analyzer with 10/10 Features
# ----------------------------------------
elif app_mode == "🔍 Deep AI Resume Analyzer":
    st.title("📄 AI Resume Parser")
    st.write("Extract structural features, contact nodes, code profiles, and predictive interview outcomes.")
    st.divider()

    uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

    if uploaded_file is not None:
        st.success("🎉 Resume Uploaded Successfully!")
        
        if 'resume_text' not in st.session_state or st.session_state.get('file_name') != uploaded_file.name:
            with st.spinner("Executing extraction sequences..."):
                text = extract_text(uploaded_file)
                st.session_state['resume_text'] = text
                st.session_state['file_name'] = uploaded_file.name
                
                # Basic Utils Extraction
                st.session_state['email'] = extract_email(text)
                st.session_state['phone'] = extract_phone(text)
                st.session_state['skills'] = extract_skills(text)
                st.session_state['ats_score'] = calculate_ats_score(st.session_state['skills'])
                st.session_state['roles'] = suggest_job_roles(st.session_state['skills'])
                st.session_state['missing'] = missing_skills(st.session_state['skills'])
                st.session_state['suggestions'] = improvement_suggestions(
                    st.session_state['ats_score'], st.session_state['missing']
                )

                # ==========================================
                # NEW ADDITIONS (9.5 - 10/10 Premium Features)
                # ==========================================
                
                # 1. Name Extraction Fallback
                lines = [l.strip() for l in text.split('\n') if l.strip()]
                st.session_state['candidate_name'] = lines[0] if len(lines) > 0 else "Candidate Profile"

                # 2. LinkedIn & GitHub Links Parsing
                import re
                linkedin_find = re.findall(r'(linkedin\.com/in/[a-zA-Z0-9_-]+)', text.lower())
                github_find = re.findall(r'(github\.com/[a-zA-Z0-9_-]+)', text.lower())
                
                st.session_state['linkedin'] = f"https://{linkedin_find[0]}" if linkedin_find else "Not Detected"
                st.session_state['github'] = f"https://{github_find[0]}" if github_find else "Not Detected"

                # 3. Education, Projects & Certifications Segmentation
                lower_text = text.lower()
                
                st.session_state['has_edu'] = "education" in lower_text or "university" in lower_text or "degree" in lower_text
                st.session_state['has_proj'] = "project" in lower_text or "academic projects" in lower_text
                st.session_state['has_cert'] = "certification" in lower_text or "certificates" in lower_text or "certified" in lower_text

                # 4. Interview Probability Score Logic
                struct_weight = sum([st.session_state['has_edu'], st.session_state['has_proj'], st.session_state['has_cert']]) * 13.3
                prob_calc = int((st.session_state['ats_score'] * 0.6) + struct_weight)
                st.session_state['interview_prob'] = min(prob_calc, 100)

        # Pull states
        resume_text = st.session_state['resume_text']
        skills = st.session_state['skills']
        ats_score = st.session_state['ats_score']
        roles = st.session_state['roles']
        missing = st.session_state['missing']
        suggestions = st.session_state['suggestions']
        
        # New pulling states
        name = st.session_state['candidate_name']
        email = st.session_state['email']
        phone = st.session_state['phone']
        linkedin = st.session_state['linkedin']
        github = st.session_state['github']
        interview_prob = st.session_state['interview_prob']

        # ----------------------------------------
        # High Level Executive Dashboard Metrics
        # ----------------------------------------
        st.subheader("📊 Executive Analysis Dashboard")
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("Overall ATS Score", f"{ats_score}%")
        with m2:
            st.metric("HR Shortlist Probability", f"{interview_prob}%", 
                      delta="Strong Fit" if interview_prob >= 75 else "Needs Polish")
        with m3:
            st.metric("Parsed Technical Skills", len(skills))
        with m4:
            st.metric("Identified Structural Gaps", 3 - sum([st.session_state['has_edu'], st.session_state['has_proj'], st.session_state['has_cert']]))

        st.divider()

        # Tabs Layout
        tab1, tab2, tab3, tab4 = st.tabs(["👤 Profile Core Details", "📂 Resume Structure Verification", "🎯 Market Role Fit", "🛠️ Action Plan & Export"])

        with tab1:
            st.subheader("Candidate Identification Profile")
            col_a, col_b = st.columns(2)
            with col_a:
                st.info(f"👤 **Name:** {name}")
                st.info(f"📧 **Email:** {email if email else 'Not Found'}")
                st.info(f"📞 **Phone:** {phone if phone else 'Not Found'}")
            with col_b:
                if linkedin != "Not Detected":
                    st.markdown(f"🔗 **LinkedIn Profile:** [{linkedin}]({linkedin})")
                else:
                    st.warning("🔗 **LinkedIn Profile:** Not Detected (Add link!)")
                    
                if github != "Not Detected":
                    st.markdown(f"💻 **GitHub Handle:** [{github}]({github})")
                else:
                    st.warning("💻 **GitHub Handle:** Not Detected (Add link!)")

            st.divider()
            st.subheader("Extracted Skill Badges")
            if skills:
                badges_html = "".join([f'<span style="background-color:#1E88E5; color:white; padding:5px 12px; margin:5px; border-radius:15px; display:inline-block; font-weight:bold;">{s}</span>' for s in skills])
                st.markdown(badges_html, unsafe_allow_html=True)
            else:
                st.warning("No domain-specific skills detected.")

        with tab2:
            st.subheader("Structural Section Verification")
            st.write("Verifying if essential recruiter evaluation modules are present in the parsed text layout:")
            
            c1, c2, c3 = st.columns(3)
            with c1:
                if st.session_state['has_edu']:
                    st.success("🎓 **Education Section:** Verified")
                else:
                    st.error("❌ **Education Section:** Missing")
            with c2:
                if st.session_state['has_proj']:
                    st.success("📂 **Projects Section:** Verified")
                else:
                    st.error("❌ **Projects Section:** Missing")
            with c3:
                if st.session_state['has_cert']:
                    st.success("📜 **Certifications Section:** Verified")
                else:
                    st.error("❌ **Certifications Section:** Missing")

        with tab3:
            st.subheader("Predictive Job Application Shortlist Matrix")
            st.write("Calculated Probability to secure a direct screening interview:")
            st.progress(interview_prob / 100)
            
            if interview_prob >= 75:
                st.balloons()
                st.success(f"🚀 **High Shortlist Potential ({interview_prob}%):** Resume features excellent structure and deep semantic alignment.")
            elif interview_prob >= 50:
                st.warning(f"⚠️ **Moderate Shortlist Potential ({interview_prob}%):** Missing crucial links or cross-industry metrics. Check optimization rules.")
            else:
                st.error(f"🚨 **Low Hiring Potential ({interview_prob}%):** High probability of getting screened out by automated ATS layers.")

            st.divider()
            st.subheader("Suggested Domain Mapping Matches")
            for role in roles:
                st.markdown(f"💼 **{role}**")

        with tab4:
            st.subheader("Missing System Requirements")
            if missing:
                missing_badges = "".join([f'<span style="background-color:#E53935; color:white; padding:5px 12px; margin:5px; border-radius:15px; display:inline-block; font-weight:bold;">⚠️ {m}</span>' for m in missing])
                st.markdown(missing_badges, unsafe_allow_html=True)
            else:
                st.success("0 core technical skill discrepancies found.")

            st.divider()
            st.subheader("Directives Checklist")
            for idx, suggest in enumerate(suggestions, 1):
                st.markdown(f"**{idx}.** {suggest}")

            st.divider()
            
            # Master File Export Generation
            report = f"AI RESUME PARSER EVALUATION REPORT\n" \
                     f"==================================\n" \
                     f"Candidate Name: {name}\n" \
                     f"Email Node: {email}\n" \
                     f"LinkedIn: {linkedin}\n" \
                     f"GitHub: {github}\n\n" \
                     f"ATS Rating: {ats_score}/100\n" \
                     f"Interview Conversion Probability: {interview_prob}%\n\n" \
                     f"Skills Profile: {', '.join(skills)}\n"
            
            st.download_button(
                "📥 Export Full Core Audit Document",
                data=report,
                file_name=f"Comprehensive_Audit_{name.replace(' ', '_')}.txt",
                mime="text/plain",
                use_container_width=True
            )

# ----------------------------------------
# Feature 3: Job Description Matcher Tab
# ----------------------------------------
elif app_mode == "💼 Job Description Matcher":
    st.title("💼 Job Description Keyword Matcher")
    st.write("Test structural matching vectors against real job vacancies.")
    st.divider()

    if 'resume_text' not in st.session_state:
        st.warning("⚠️ Access 'Deep AI Resume Analyzer' first to build memory data frames.")
    else:
        col_jd1, col_jd2 = st.columns([1, 1])
        with col_jd1:
            st.subheader("Target Job Specification Frame")
            jd_text = st.text_area("Paste System JD Text Here...", height=250)
        with col_jd2:
            st.subheader("Active Extracted Pipeline")
            st.info(f"Target Name: {st.session_state['candidate_name']}")
            st.info(", ".join(st.session_state['skills']))

        if st.button("Calculate Alignment Vector", type="primary") and jd_text:
            jd_keywords = [skill for skill in POPULAR_TECH_SKILLS if skill.lower() in jd_text.lower()]
            my_skills = st.session_state['skills']
            
            matched_jd = [s for s in my_skills if s.lower() in jd_text.lower()]
            unmatched_jd = [s for s in jd_keywords if s.lower() not in [m.lower() for m in my_skills]]
            
            total_req = len(jd_keywords) if len(jd_keywords) > 0 else 1
            calculated_match = min(int((len(matched_jd) / total_req) * 100), 100)

            st.subheader("🎯 Alignment Report")
            st.metric("Job Match Alignment Indicator", f"{calculated_match}%")
            st.progress(calculated_match / 100)

            col_res1, col_res2 = st.columns(2)
            with col_res1:
                st.success("✅ Matched Job Keywords:")
                for m in matched_jd: st.write(f"✔️ `{m}`")
            with col_res2:
                st.error("❌ Action Items (Missing Core JD Needs):")
                for u in unmatched_jd: st.write(f"❌ `{u}`")

# ----------------------------------------
# Feature 4: Analytics Dashboard (Safe Checkbox / Progress Bars)
# ----------------------------------------
elif app_mode == "📈 Analytics Dashboard":
    st.title("📈 Structural Metric Visualization")
    st.write("Safe density distribution analytics engine.")
    st.divider()

    if 'resume_text' not in st.session_state:
        st.warning("⚠️ Execute analysis first to activate analytical chart modules.")
    else:
        st.subheader("📊 Relative Vector Proximity Analytics")
        my_skills = st.session_state['skills']
        missing_s = st.session_state['missing']
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.markdown("#### ✅ Active Coverage Density")
            for s in my_skills:
                st.write(f"🟢 **{s}**")
                st.progress(1.0)
        with col_c2:
            st.markdown("#### 🔴 Structural Missing Gaps")
            for m in missing_s:
                st.write(f"❌ **{m}**")
                st.progress(0.3)

# ----------------------------------------
# Global Footer Block
# ----------------------------------------
st.divider()
st.caption("Powered by Streamlit Advanced Parsing Subsystems | Pro Feature Configuration Active 2026")