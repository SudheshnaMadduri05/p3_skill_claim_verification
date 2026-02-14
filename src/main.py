from pathlib import Path
from src.skill_extractor import load_text
from src.skill_matcher import SkillVerifier
from src.config import ACCEPT_THRESHOLD, REVIEW_THRESHOLD 

print("=== Skill Claim Verification System ===")

DATA_DIR = Path("data/candidates")
verifier = SkillVerifier()

def decision(score: float) -> str:
    if score >= ACCEPT_THRESHOLD:
        return "ACCEPT"
    elif score >= REVIEW_THRESHOLD:
        return "REVIEW"
    else:
        return "REJECT"

def main():
    if not DATA_DIR.exists():
        print("data/candidates folder not found")
        return

    for candidate_dir in sorted(DATA_DIR.iterdir()):
        if not candidate_dir.is_dir():
            continue

        resume_path = candidate_dir / "resume.txt"
        task_path = candidate_dir / "tasks.txt"

        if not resume_path.exists() or not task_path.exists():
            print(f"Skipping {candidate_dir.name} (missing files)")
            continue

        resume_text = load_text(resume_path) # type: ignore
        task_text = load_text(task_path) # type: ignore

        score = verifier.similarity_score(resume_text, task_text) # type: ignore
        result = decision(score)

        print("\n------------------------------")
        print(f"Candidate: {candidate_dir.name}")
        print(f"Similarity Score : {score:.2f}")
        print(f"Decision         : {result}")

if __name__ == "__main__":
    main()
