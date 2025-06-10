
from spotify_auth import sp  # Import the authenticated Spotify client

def get_recommendations(mood):
    """
    Get music recommendations based on the specified mood.

    Parameters:
    mood (str): The mood for which to get recommendations. 
                Options are 'happy', 'sad', 'angry', 'relaxed'.

    Returns:
    list: A list of track names recommended for the specified mood.
    """
    # Define mood playlists with unique IDs
    mood_playlists = {
        'happy': '2xJyQdJYQASidY6KQpciCE',  # Replace with actual playlist ID for happy mood
        'sad': '2xJyQdJYQASidY6KQpciCE',    # Replace with actual playlist ID for sad mood
        'angry': '2xJyQdJYQASidY6KQpciCE',  # Replace with actual playlist ID for angry mood
        'relaxed': '2xJyQdJYQASidY6KQpciCE' # Replace with actual playlist ID for relaxed mood
    }
    
    # Get the playlist ID based on the mood, default to relaxed
    playlist_id = mood_playlists.get(mood, '2xJyQdJYQASidY6KQpciCE')  # Default to relaxed
    
    try:
        # Fetch the tracks from the playlist
        results = sp.playlist_tracks(playlist_id)
        # Extract track names, ensuring the track exists
        recommendations = [item['track']['name'] for item in results['items'] if item['track'] is not None]
        return recommendations
    except Exception as e:
        print(f"An error occurred while fetching recommendations: {e}")
        return []
