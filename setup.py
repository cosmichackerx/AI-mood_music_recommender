#setup.py

from setuptools import setup, find_packages

setup(
    name="mood_music_recommender",
    version="1.0.0",
    description="AI-powered mood-based music recommendation app using Spotify and NLP",
    author="CosmicHackerX",
    author_email="cosmichackerx@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "spotipy>=2.23.0",
        "nltk>=3.8.1",
        "python-dotenv>=1.0.1"
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "mood-music=mood_music_recommender.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
