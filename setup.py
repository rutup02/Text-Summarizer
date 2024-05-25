import setuptools

with open("README.md","r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "rutup02"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "rutuprajapati2003@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    Long_description=long_description,
    Long_description_content_type="text/markdown",
    url=f"https://github.com/rutup02/Text-Summarizer.git",
    project_urls={
        "Bug Tracker": f"https://github.com/rutup02/Text-Summarizer.git/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)