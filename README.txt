🎧 AI-Powered Mood-Based Music Recommendation
A Python application that recommends Spotify songs based on the user's current mood. It uses NLTK's VADER sentiment analysis to detect mood from text input and fetches songs from Spotify playlists aligned with different emotional states.

🚀 Features
🔍 Mood Detection using natural language input.

🎵 Spotify API Integration to fetch real-time music recommendations.

😊 Supports moods: happy, sad, relaxed (add angry if you enhance mood detection).

💻 Lightweight Command-Line Interface.

🧠 Built with the help of AI tools like ChatGPT and Blackbox AI.

🛠️ Setup Instructions
1. Prerequisites
Python 3.6 or higher.

Spotify Developer Account to obtain Client ID and Client Secret.

Internet connection (for Spotify API and downloading NLTK data).

2. Clone the Repository

git clone <your-github-repo-url>
cd <your-repo-directory>

3. Install Required Packages

pip install spotipy nltk
4. Configure Spotify Credentials
You need to set your Spotify credentials as environment variables.

On Windows (Command Prompt or PowerShell):

set SPOTIPY_CLIENT_ID=your_spotify_client_id
set SPOTIPY_CLIENT_SECRET=your_spotify_client_secret

On macOS/Linux (Terminal):

export SPOTIPY_CLIENT_ID=your_spotify_client_id
export SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
💡 Tip: You can also store credentials in a .env file using python-dotenv for development, but avoid committing this file.

5. Download NLTK VADER Lexicon
This happens automatically the first time, but you can also do it manually:

python

import nltk
nltk.download('vader_lexicon')
▶️ Usage
Run the main application:

python main.py
You will be prompted:

sql

How are you feeling today?
Type in a sentence describing your mood, for example:

rust

I'm feeling super excited and energized today!
The app will analyze your mood and print a list of recommended Spotify songs.

📁 Project Structure
mood-music-recommender/
├── src/
│   └── mood_music_recommender/
│       ├── __init__.py
│       ├── main.py
│       ├── mood_detection.py
│       ├── music_recommendation.py
│       ├── spotify_auth.py
│       └── config.py
├── .gitignore
├── requirements.txt
├── setup.py
├── LICENSE
├── README.md
├── runtime.txt

🎵 Playlist Mapping
Update music_recommendation.py with your own Spotify playlist IDs:

python

mood_playlists = {
    'happy': 'your_playlist_id',
    'sad': 'your_playlist_id',
    'relaxed': 'your_playlist_id',
    'angry': 'your_playlist_id'
}
🔒 Security Notes
Do NOT commit your Client ID and Client Secret to public repositories.

Use .env or environment variables instead of hardcoding credentials in config.py.

📄 License
This project is licensed under the MIT License.
See the LICENSE file for more details.

🤝 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you would like to change.

📬 Contact
For feedback, questions, or collaborations, contact: [Your Email or GitHub Profile]

🙌 Acknowledgements
NLTK — Natural Language Toolkit

Spotipy — Lightweight Python library for the Spotify Web API

AI tools: ChatGPT, Blackbox AI

