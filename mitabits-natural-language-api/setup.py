import setuptools

from nlx import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    reqs = [line.strip() for line in fh]
setuptools.setup(
    name="nlx",
    version=__version__,
    author="Dimitar Marinov",
    author_email="dimitar@mitabits.com",
    description="Natural Language API (NLX) for Mitabits Insightful text analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=reqs,
    python_requires='>=3.6',
)
