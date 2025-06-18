from setuptools import setup, find_packages

setup(
    name="release-note-automator",
    version="0.1.0",
    description="Generate, summarize, format, and post release notes from Azure DevOps repos using Gemini",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ankur Helak",
    author_email="ankurhelak@gmail.com",
    url="https://github.com/ankurhelak/release-note-automator",  # update this if hosted elsewhere
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "python-dotenv",
        "questionary",
        "google-generativeai",
        "wcwidth"
    ],
    entry_points={
        "console_scripts": [
            "rlauto=release_note_automator.cli:main"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.7"
)
