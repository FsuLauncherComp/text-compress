from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="text-compress",
    version="0.1.0",
    author="Rody Zakovich",
    description="A package for compressing text using various techniques",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FsuLauncherComp/text-compress",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "spacy>=3.5.1",
        "sumy>=0.11.0",
        "textblob>=0.17.1",
        "nltk>=3.8.1",
    ],
    entry_points={
        'console_scripts': [
            'text_compress_install = text_compress.post_install:run',
        ],
    },
)
