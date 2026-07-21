"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:  # pragma: no cover - supports running the file directly
    from recommender import load_songs, recommend_songs


def run_profile_demo(songs) -> None:
    profiles = [
        {
            "name": "Genre-only gambit",
            "description": "Uses only a favorite genre to test whether the scorer over-focuses on the categorical match.",
            "prefs": {"genre": "pop"},
        },
        {
            "name": "Acoustic bait",
            "description": "Claims a strong acoustic preference despite an otherwise mismatched mood and genre.",
            "prefs": {"genre": "rock", "mood": "intense", "energy": 0.95, "likes_acoustic": True},
        },
        {
            "name": "Energy extremist",
            "description": "Targets a very high energy value and a contradictory mood to probe whether energy dominates the ranking.",
            "prefs": {"genre": "lofi", "mood": "happy", "energy": 0.95, "likes_acoustic": False},
        },
    ]

    for profile in profiles:
        print(f"Profile: {profile['name']}")
        print(f"Description: {profile['description']}")
        print(f"Preferences: {profile['prefs']}")
        print()

        recommendations = recommend_songs(profile["prefs"], songs, k=5)

        print("Top 5 recommendations:")
        for idx, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{idx}. {song['title']}")
            print(f"   Score: {score:.2f}")
            print("   Reasons:")
            for reason in explanation.split("; "):
                print(f"     - {reason}")
            print()

        print("=" * 60)
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")
    print()
    run_profile_demo(songs)


if __name__ == "__main__":
    main()
