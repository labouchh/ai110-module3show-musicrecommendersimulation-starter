# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

My recommender system uses song features and user preferences to find songs that are a good match. Each song has features like genre, mood, energy, tempo, and acousticness. The UserProfile stores what type of music the user prefers, including favorite genre, favorite mood, energy level, and whether they like acoustic songs. A point system is used by ranking highest to lowest, where the highest score is the best match.

---

## How The System Works

Explain your design in plain language.

The system gives each song a score based on how well it matches the user's preferences. Genre matches add more points, mood matches add points, and songs with energy levels close to the user's target receive higher scores. The system then ranks all songs by their score and recommends the highest-scoring songs.
Each song would include its own tempo, mood, and genre. It's important to have multiple data types under Song to make a more accurate recommendation. 

Some prompts to answer:

- What features does each `Song` use in your system?
Features like genre, mood, energy, tempo, and acousticness are used for each song evaluation.
- What information does your `UserProfile` store?
Favorite genre, favorite mood, energy level, and whether they like acoustic songs or not (boolean).
- How does your `Recommender` compute a score for each song?
I used a point system where +2 pt is for a genre match, +1 for mood match, the closer the song is to the energy level prefered it gets more points, and for acousticness it gets a point if the user likes it. 
- How do you choose which songs to recommend
The system builts evaluates each song based on the features and then ranks them with the closest song having the highest points.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

Loaded songs: 20

High Energy Pop
------------------------------
Sunrise City - Score: 5.25
Because: Genre match (+2.0); Mood match (+1.0); Energy similarity (+1.84); Acoustic preference (+0.41)

Gym Hero - Score: 4.42
Because: Genre match (+2.0); Energy similarity (+1.94); Acoustic preference (+0.47)

...

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried
## Experiments You Tried

I tested my recommender using three different user profiles: High energy pop, chill lofi, and intense rock.

The high energy pop profile recommended songs like "Sunrise City" and "Gym Hero" because they matched the user's preferred genre, happy mood, and high energy level.

The chill lofi profile recommended songs like "Library Rain" and "Midnight Coding" because they matched the lofi genre, chill mood, and lower energy preference.

The intense rock profile recommended "Storm Runner" as the top result because it matched the rock genre, intense mood, and high energy preference.

I also noticed that energy similarity has a strong effect on recommendations. Some songs from different genres can still rank highly if their energy level is close to the user's preference.It appears to be a hole in Ai's ability to handle human complex thinking. This showed me that adding more features, such as listening history, could make recommendations more accurate.

## Limitations and Risks

Summarize some limitations of your recommender.

The system may recommend songs from different genres if they have similar energy levels. The algorithm does not fully understand musical style like a human listener would.

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



