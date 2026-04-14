"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    user_profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "calm",
            "energy": 0.2
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.85
        },

        # Edge cases 👇
        "Conflicting Mood": {
            "genre": "pop",
            "mood": "sad",
            "energy": 0.9
        },
        "No Preference": {
            "genre": "",
            "mood": "",
            "energy": 0.5
        }
    }

    for profile_name, prefs in user_profiles.items():
        print(f"\n=== {profile_name} ===")
        
        recs = recommend_songs(prefs, songs, k=5)

        for i, (song, score, explanation) in enumerate(recs, start=1):
            print(f"\n{i}. {song['title']} by {song['artist']}")
            print(f"   Score : {score:.2f}")
            print(f"   Why   : {explanation}")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop Recommendations")
    print("=" * 40)
    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{i}. {song['title']} by {song['artist']}")
        print(f"   Score : {score:.2f}")
        print(f"   Why   : {explanation}")
    print()


if __name__ == "__main__":
    main()
