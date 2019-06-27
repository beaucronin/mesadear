import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mesadear",
    version="0.0.1",
    author="Beau Cronin",
    author_email="beau.cronin@gmail.com",
    description="A delightful Python client for Airtable",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/beaucronin/mesadear",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)