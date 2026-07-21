import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs ranked by the user's taste profile."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        scored_songs = []
        for song in self.songs:
            song_dict = {
                "id": song.id,
                "title": song.title,
                "artist": song.artist,
                "genre": song.genre,
                "mood": song.mood,
                "energy": song.energy,
                "tempo_bpm": song.tempo_bpm,
                "valence": song.valence,
                "danceability": song.danceability,
                "acousticness": song.acousticness,
            }
            score, _ = score_song(user_prefs, song_dict)
            scored_songs.append((score, song))

        scored_songs.sort(key=lambda item: item[0], reverse=True)
        return [song for _, song in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song was scored highly for the given user profile."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        song_dict = {
            "id": song.id,
            "title": song.title,
            "artist": song.artist,
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
            "tempo_bpm": song.tempo_bpm,
            "valence": song.valence,
            "danceability": song.danceability,
            "acousticness": song.acousticness,
        }
        _, reasons = score_song(user_prefs, song_dict)
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": int(float(row["tempo_bpm"])),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    genre_pref = user_prefs.get("genre") or user_prefs.get("favorite_genre")
    if genre_pref and song.get("genre") == genre_pref:
        score += 2.0
        reasons.append("genre match (+2.0)")
    elif genre_pref:
        reasons.append(f"genre mismatch ({song.get('genre')})")

    mood_pref = user_prefs.get("mood") or user_prefs.get("favorite_mood")
    if mood_pref and song.get("mood") == mood_pref:
        score += 1.0
        reasons.append("mood match (+1.0)")
    elif mood_pref:
        reasons.append(f"mood mismatch ({song.get('mood')})")

    energy_pref = user_prefs.get("energy")
    if energy_pref is None:
        energy_pref = user_prefs.get("target_energy")
    if energy_pref is not None:
        energy_closeness = max(0.0, 1.0 - abs(float(song.get("energy", 0.0)) - float(energy_pref)))
        score += 1.0 * energy_closeness
        reasons.append(f"energy close (+{1.0 * energy_closeness:.2f})")

    acoustic_target = user_prefs.get("acousticness")
    if acoustic_target is None:
        likes_acoustic = user_prefs.get("likes_acoustic")
        if likes_acoustic is True:
            acoustic_target = 0.8
        elif likes_acoustic is False:
            acoustic_target = 0.2
        else:
            acoustic_target = 0.5

    acoustic_closeness = max(0.0, 1.0 - abs(float(song.get("acousticness", 0.0)) - float(acoustic_target)))
    score += 0.7 * acoustic_closeness
    reasons.append(f"acousticness close (+{0.7 * acoustic_closeness:.2f})")

    valence_target = user_prefs.get("valence", 0.5)
    valence_closeness = max(0.0, 1.0 - abs(float(song.get("valence", 0.0)) - float(valence_target)))
    score += 0.5 * valence_closeness
    reasons.append(f"valence close (+{0.5 * valence_closeness:.2f})")

    dance_target = user_prefs.get("danceability", 0.5)
    dance_closeness = max(0.0, 1.0 - abs(float(song.get("danceability", 0.0)) - float(dance_target)))
    score += 0.5 * dance_closeness
    reasons.append(f"danceability close (+{0.5 * dance_closeness:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    return sorted(scored_songs, key=lambda item: item[1], reverse=True)[:k]
