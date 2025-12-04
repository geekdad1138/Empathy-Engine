# core/emotion.py
from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"

class EmotionalCore:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)

    def embed(self, text: str):
        return self.model.encode([text])[0]

    def rough_affect(self, text: str):
        """
        Lightweight heuristic example:
        - compute polarity via simple sentiment proxy (embedding dot to small seeds)
        This is a stub: replace with trained regressors later.
        """
        emb = self.embed(text)
        # toy seeds (not real) for demonstration
        seed_positive = np.ones_like(emb) * 0.1
        seed_negative = -seed_positive
        valence = float(np.dot(emb, seed_positive) - np.dot(emb, seed_negative))
        # normalize
        valence = max(-1.0, min(1.0, valence / (np.linalg.norm(emb) + 1e-6)))
        arousal = min(1.0, max(0.0, abs(valence)))
        dominance = 0.5  # placeholder
        return {
            "valence": valence,
            "arousal": arousal,
            "dominance": dominance,
            "confidence": 0.5
        }
