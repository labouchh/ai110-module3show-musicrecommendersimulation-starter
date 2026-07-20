from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv
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
        scored = []

        for song in self.songs:
            score = 0

            if song.genre == user.favorite_genre:
                score += 2

            if song.mood == user.favorite_mood:
                score += 1

            score += 2 - abs(song.energy - user.target_energy)

            scored.append((song, score))

        scored.sort(key=lambda x: x[1], reverse=True)

        return [song for song, score in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("matching genre")

        if song.mood == user.favorite_mood:
            reasons.append("matching mood")

        if abs(song.energy - user.target_energy) < 0.2:
            reasons.append("similar energy")

        return "Recommended because of " + ", ".join(reasons)
    
def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file into a list of dictionaries.
    Numeric columns are converted from text to numbers so they can be
    used in scoring; everything else stays a string.
    Required by src/main.py
    """
    # Columns that must be numbers, mapped to how they should be converted.
    numeric_fields = {
        "id": int,
        "energy": float,
        "tempo_bpm": float,
        "valence": float,
        "danceability": float,
        "acousticness": float,
    }

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)  # uses the header row for dictionary keys
        for row in reader:
            for field, convert in numeric_fields.items():
                if field in row and row[field] != "":
                    row[field] = convert(row[field])
            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song based on the user's preferences.
    Returns both the numeric score and a list of reasons.
    """
    score = 0.0
    reasons = []

    # Genre match
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append("Genre match (+2.0)")

    # Mood match
    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.0
        reasons.append("Mood match (+1.0)")

    # Energy similarity (closer energy earns more points)
    energy_diff = abs(song["energy"] - user_prefs["target_energy"])
    energy_score = max(0, 2.0 - (energy_diff * 2))
    score += energy_score
    reasons.append(f"Energy similarity (+{energy_score:.2f})")

    # Acoustic preference
    if user_prefs["likes_acoustic"]:
        acoustic_score = song["acousticness"] * 0.5
    else:
        acoustic_score = (1 - song["acousticness"]) * 0.5
    score += acoustic_score
    reasons.append(f"Acoustic preference (+{acoustic_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # SCORING RULE: score every song on its own.
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored.append((song, score, explanation))

    # RANKING RULE: sort by score (highest first), then keep the top k.
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
