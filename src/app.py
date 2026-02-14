import streamlit as st
from pathlib import Path
from skill_extractor import load_text
from skill_matcher import SkillVerifier
from config import ACCEPT_THRESHOLD, REVIEW_THRESHOLD


# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Skill Claim Verification System",
    
    layout="centered"
)

st.title("Skill Claim Verification System")
st.markdown(
    """
This system verifies whether a candidate’s **claimed skills**
match their actual **task performance** using semantic similarity.
"""
)

# ----------------------------
# FILE UPLOAD SECTION
# ----------------------------

st.header("Upload Candidate Files")

resume_file = st.file_uploader("Upload Resume (.txt)", type=["txt"])
task_file = st.file_uploader("Upload Task Performance (.txt)", type=["txt"])

# ----------------------------
# VERIFICATION LOGIC
# ----------------------------

if st.button("Verify Skills"):

    if resume_file is None or task_file is None:
        st.warning("⚠️ Please upload both resume and task files.")
    else:
        # Read file contents
        resume_text = resume_file.read().decode("utf-8")
        task_text = task_file.read().decode("utf-8")

        # Initialize verifier
        verifier = SkillVerifier()

        # Compute similarity
        score = verifier.similarity_score(resume_text, task_text)

        # Decision logic
        if score >= ACCEPT_THRESHOLD:
            decision = "ACCEPT"
            color = "green"
        elif score >= REVIEW_THRESHOLD:
            decision = "REVIEW"
            color = "orange"
        else:
            decision = "REJECT"
            color = "red"

        # ----------------------------
        # DISPLAY RESULTS
        # ----------------------------
        st.subheader("Results")

        st.metric("Similarity Score", f"{score:.2f}")

        st.markdown(
            f"<h3 style='color:{color};'>Decision: {decision}</h3>",
            unsafe_allow_html=True
        )

        st.progress(float(score))

        st.success("Verification completed successfully!")
