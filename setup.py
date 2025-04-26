from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="dtrocr",
    version="0.1.0",
    author="Latent",
    description="A PyTorch implementation of DTrOCR: Decoder-only Transformer for Optical Character Recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arvindrajan92/DTrOCR",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
)
