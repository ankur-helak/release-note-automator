from setuptools import setup, find_packages

setup(
    name="release-note-automator",
    version="0.1.0",
    description="Generate and post automated release notes from Azure DevOps using Gemini",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
        "google-generativeai",
        "questionary",
        "wcwidth"
    ],
    entry_points={
        "console_scripts": [
            "rlauto=release_note_automator.cli:main"
        ]
    },
    python_requires=">=3.8",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
