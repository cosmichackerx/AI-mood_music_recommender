
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure the VADER lexicon is downloaded
nltk.download('vader_lexicon', quiet=True)

def detect_mood(text):
    """
    Detect mood from text input using VADER sentiment analysis.

    Parameters:
    text (str): The text input to analyze

    Returns:
    str: Detected mood; one of ['happy', 'sad', 'neutral']
    """
    # Initialize sentiment analyzer
    sia = SentimentIntensityAnalyzer()
    
    # Analyze sentiment
    sentiment = sia.polarity_scores(text)
    
    # Determine mood based on compound sentiment score
    compound = sentiment['compound']
    if compound > 0.05:
        return 'happy'
    elif compound < -0.05:
        return 'sad'
    else:
        return 'relaxed'  # match 'relaxed' mood as per music recommendation
