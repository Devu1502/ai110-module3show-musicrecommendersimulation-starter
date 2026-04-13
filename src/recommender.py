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
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(filepath):
    """Load and type-cast songs from a CSV file into a list of dicts."""
    int_fields = {'id'}
    float_fields = {'energy', 'tempo_bpm', 'valence', 'danceability', 'acousticness'}

    songs = []
    with open(filepath, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for field in int_fields:
                row[field] = int(row[field])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a single song against user preferences and return the score with reasons."""
    score = 0.0
    reasons = []

    if song['genre'] == user_prefs['genre']:
        score += 2.0
        reasons.append("Genre match (+2.0)")

    if song['mood'] == user_prefs['mood']:
        score += 1.0
        reasons.append("Mood match (+1.0)")

    energy_score = 1 - abs(song['energy'] - user_prefs['energy'])
    score += energy_score
    reasons.append(f"Energy similarity (+{energy_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs ranked by score for the given user preferences."""
    scored = [
        (song, score, ", ".join(reasons))
        for song in songs
        for score, reasons in (score_song(user_prefs, song),)
    ]
    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]
