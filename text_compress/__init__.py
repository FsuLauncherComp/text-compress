import logging
import re
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer
from textblob import TextBlob
from typing import List, Optional


class TextCompressor:
    def __init__(self, text: str, log_level: Optional[int] = None):
        self.text = text
        self.compressed_text: Optional[str] = None
        self.logger = logging.getLogger(__name__)
        if log_level is not None:
            self.logger.setLevel(log_level)
            handler = logging.StreamHandler()
            handler.setLevel(log_level)
            self.logger.addHandler(handler)

    def remove_stopwords_and_tokenize(self) -> None:
        """Tokenize the text and remove stopwords."""
        self.logger.info("Tokenizing and removing stopwords...")
        _text = self.compressed_text or self.text
        self.logger.debug(f"Starting Length: {len(_text)}")
        tokens = word_tokenize(_text)
        stop_words = set(stopwords.words("english"))
        filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
        self.compressed_text = " ".join(filtered_tokens)
        self.compressed_text = re.sub(r"\s*([.,;:!?\-])\s*", r"\1 ", self.compressed_text)
        self.logger.debug(f"Ending Length: {len(self.compressed_text)}")
        self.logger.debug(self.compressed_text)

    def apply_lemmatization(self) -> None:
        """Lemmatize the text."""
        self.logger.info("Lemmatizing...")
        _text = self.compressed_text or self.text
        self.logger.debug(f"Starting Length: {len(_text)}")
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(_text)
        lemmatized_tokens = [token.lemma_ for token in doc]
        self.compressed_text = " ".join(lemmatized_tokens)
        self.logger.debug(f"Ending Length: {len(self.compressed_text)}")
        self.logger.debug(self.compressed_text)

    def generate_paraphrase(self) -> None:
        """Paraphrase the text."""
        self.logger.info("Paraphrasing...")
        _text = self.compressed_text or self.text
        self.logger.debug(f"Starting Length: {len(_text)}")
        blob = TextBlob(_text)
        self.compressed_text = " ".join([str(s) for s in blob.sentences])
        self.logger.debug(f"Ending Length: {len(self.compressed_text)}")
        self.logger.debug(self.compressed_text)

    def generate_summary(self, ratio: float = 0.8) -> None:
        """Summarize the text using LexRank algorithm."""
        self.logger.info("Summarizing...")
        _text = self.compressed_text or self.text
        self.logger.debug(f"Starting Length: {len(_text)}")
        parser = PlaintextParser.from_string(_text, Tokenizer("english"))
        summarizer = LexRankSummarizer()
        num_sentences = max(1, int(len(parser.document.sentences) * ratio))
        summary = summarizer(parser.document, num_sentences)
        self.compressed_text = " ".join([str(sentence) for sentence in summary])
        self.logger.debug(f"Ending Length: {len(self.compressed_text)}")
        self.logger.debug(self.compressed_text)

    def compress(self, techniques: Optional[List[str]] = None) -> str:
        """Compress the text using specified techniques."""
        self.text = self.text.replace('\n', ' ')

        if techniques is None:
            techniques = ['remove_stopwords_and_tokenize', 'generate_paraphrase', 'generate_summary', 'apply_lemmatization']

        for technique in techniques:
            compression_method = getattr(self, technique)
            compression_method()
            self.logger.info("\n")

        return self.compressed_text