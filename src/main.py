"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs
def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")
    user_profiles = [ 
        {
            "name": "High Energy Pop",
            "preferences": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.9,
            "likes_acoustic": False
            }
        },
        {
            "name": "Chill Lofi",
            "preferences": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.4,
            "likes_acoustic": True
            }
        },
        {
            "name": "Deep Intense Rock",
            "preferences": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.95,
            "likes_acoustic": False
            }
        }
    ]

    for profile in user_profiles:
        print("\n" + profile["name"])
        print("-" * 30)

        recommendations = recommend_songs(
        profile["preferences"],
        songs,
        k=5
        )

        for rec in recommendations:
            song, score, explanation = rec

            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()
if __name__ == "__main__":
    main()