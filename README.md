# TextCompress
This package provides a Python class named TextCompressor for compressing text using various natural language processing techniques, including tokenization and stopword removal, lemmatization, paraphrasing, and summarization.

# Motivation

Working with LLMs for Embeddings, I found much of the raw documents/pages I was passing into the context of my prompts generally contained a lot unneccesary text that didn't contribute to the overal meaning of the document/page. This increased the number of tokens being used in the context, which in turn increased the size of the embeddings. I wanted to find a way to reduce the size of the embeddings without losing the meaning of the document/page. This package is very basic first attempt.

# Installation
To install the text_compression package:

Clone the repository:

```bash
git clone https://github.com/FsuLauncherComp/text-compress.git
```

Install the text_compression package:

```bash
pip install .
```

Afeter installation, you will need to download the following NLTK data:

- punkt
- stopwords
- wordnet

As well as the following spacy model:

- en_core_web_sm

This can be done by executing the run() from post_install.py:

```bash
from text_compress.post_install import run

run()
```

# Usage

Import the TextCompressor class:

```python
from text_compression import TextCompressor
```

Create an instance of the TextCompressor class with the input text:

```python
text = "This is an example of text compression using a callable class. Users can choose specific techniques to implement or use all techniques."

compressor = TextCompressor(text)
```

Call the compress() method with a list of techniques to apply:

```python
compressed_text = compressor.compress(techniques=['remove_stopwords_and_tokenize','generate_paraphrase','generate_summary'])
print(compressed_text)
```

If no techniques are specified, all available techniques are applied by default:

```python
compressed_text = compressor.compress()
print(compressed_text)
```

## Available techniques:

- **remove_stopwords_and_tokenize**: Tokenize the text and remove stopwords.

- **apply_lemmatization**: Lemmatize the text.

- **generate_paraphrase**: Paraphrase the text using TextBlob.

- **generate_summary**: Summarize the text using the LexRank algorithm from the sumy library.