
    
from mood_detection import detect_mood
from music_recommendation import get_recommendations

def main():
    user_input = input("How are you feeling today? ")
    try:
        mood = detect_mood(user_input)
        recommendations = get_recommendations(mood)
        if not recommendations:
            print("Sorry, no recommendations available for your mood right now.")
            return

        print(f"Based on your mood ({mood}), we recommend the following songs:")
        for song in recommendations:
            print(f"- {song}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
