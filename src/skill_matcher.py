import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from config import MODEL_NAME, SIMILARITY_THRESHOLD


class SkillVerifier:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)

    def similarity_score(self, claimed: str, performed: str) -> float:

        embeddings = self.model.encode([claimed, performed])

        claimed_vec = np.array(embeddings[0]).reshape(1, -1)
        performed_vec = np.array(embeddings[1]).reshape(1, -1)

        similarity = cosine_similarity(claimed_vec, performed_vec)[0][0]
        return float(similarity)

    def verify(self, claimed: str, performed: str) -> dict:
        score = self.similarity_score(claimed, performed)
        return {
            "authentic": score >= SIMILARITY_THRESHOLD,
            "score": round(score, 2)
        }
