import logging
from transformers import pipeline

logger = logging.getLogger(__name__)

class Generator:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self._pipe = None

    def _load(self):
        if self._pipe is None:
            try:
                self._pipe = pipeline("text-generation", model=self.model_name)
            except Exception:
                logger.warning("Falling back to echo generator")
                self._pipe = None

    def generate(self, prompt: str) -> str:
        self._load()
        if self._pipe:
            result = self._pipe(prompt, max_new_tokens=50)[0]["generated_text"]
            return result[len(prompt):]
        return prompt
