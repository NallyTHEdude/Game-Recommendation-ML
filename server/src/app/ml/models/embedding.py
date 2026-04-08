from sentence_transformers import SentenceTransformer
from typing import Final


class EmbeddingModel:
    _model_instance = None
    _initialized = False

    def __new__(cls):
        if cls._model_instance is None:
            cls._model_instance = super().__new__(cls)
        return cls._model_instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self.model_name: Final[str] = "BAAI/bge-base-en-v1.5"
        self.model = SentenceTransformer(self.model_name)

        self._initialized = True

    def encode_passage(self, tags: list[str], genre: list[str], summary: str) -> list[float]:
        tags_text = ", ".join(tags)
        genre_text = ", ".join(genre)

        passage = f"""passage: This game is described as '{summary}'{summary}.\nIt includes tags such as {tags_text}.\nIt belongs to the genres {genre_text}."""
        return self.model.encode(passage.strip(), normalize_embeddings=True)

    def encode_query(self, query: str) -> list[float]:
        query = f"""query: {query}"""
        return self.model.encode(query.strip(), normalize_embeddings=True)

embedding_model = EmbeddingModel()
