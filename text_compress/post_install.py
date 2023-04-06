import nltk
import os
import spacy

def run():
    # Add nltk_data to path and set NLTK_DATA environment variable
    nltk.data.path.append(os.path.join(os.getcwd(), "nltk_data"))
    os.environ["NLTK_DATA"] = os.path.join(os.getcwd(), "nltk_data")

    # Initialize the NLTK downloader
    nltk.download('punkt', download_dir='./nltk_data')
    nltk.download('stopwords', download_dir='./nltk_data')
    nltk.download('wordnet', download_dir='./nltk_data')

    # Download the spacy model
    spacy.cli.download('en_core_web_sm')