# Skill Claim Verification System

## Problem Overview
Many internship candidates mention skills in their resumes that they cannot actually perform in practical tasks. Companies often find it difficult to accurately assess a candidate’s true abilities during the shortlisting stage, as resumes usually contain self-declared skill claims. Since these claims aren’t always supported by clear evidence or context, it becomes challenging for recruiters to determine whether a candidate genuinely possesses the required competencies.

## Problem Statement

The goal of this project is to determine whether a candidate’s claimed skills truly match their actual performance. In many cases, resumes list a variety of skills, tools, and technologies, but it can be difficult to verify whether the candidate has genuinely applied them in real-world situations. Simply mentioning a skill does not necessarily prove efficiency or practical experience.
The system compares the skills mentioned in the resume with the descriptions of tasks the candidate has performed. By using semantic similarity techniques, it analyzes the meaning and context of both to check if the candidate genuinely demonstrates the abilities they claim. This helps ensure more accurate and reliable skill verification.

## Features
- Verifies whether claimed skills match actual task performance
- Uses semantic similarity instead of surface-level keyword matching
- Implemented using Sentence Transformers
- Computes contextual similarity score between resume and task performance
- Threshold-based classification (Accept / Review / Reject)
- Machine learning-based skill validation model
- Reduces dependency on manual shortlisting

## Innovation Feature

This project introduces a smart skill verification system that compares a candidate’s claimed skills with the tasks they have actually performed using semantic understanding techniques.
Instead of simply checking for matching keywords, the system analyzes the meaning and context to see if the candidate truly demonstrates the skills they mention. It uses clear threshold-based rules to classify candidates fairly and consistently.
By focusing on real performance rather than just self-declared claims, the system supports more reliable, transparent, and practical internship selection decisions.


## Tech Stack Used

- Python
- Sentence Transformers
- Scikit-learn
- NumPy
- Streamlit
- Altair 

## How to Run

1. Clone the repository:
   git clone https://github.com/SudheshnaMadduri05/p3_skill_claim_verification.git

2. Navigate to project folder:
   cd p3_skill_claim_verification

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   python src/main.py


## Deployment

Live Application Link: https://p3skillclaimverification-mzje4clva7jsd8qjhqhmal.streamlit.app/


## Demo Video

Watch the full demo here:  
(Add your Google Drive or YouTube link here)



## Author

Sudheshna Madduri  
GitHub: https://github.com/SudheshnaMadduri05  
LinkedIn: https://www.linkedin.com/in/sudheshna-madduri-77702a352?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app




