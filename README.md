# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This simulation models a lightweight content-based recommender that suggests songs by comparing a user’s taste profile to song attributes. In the real world, recommendation systems use far richer signals such as listening history, skips, and collaborative behavior, but this version focuses on a simple and interpretable approach: it prioritizes clear features like genre, mood, energy, and acousticness to show how a recommender can score and rank songs.

---

## How The System Works

This version uses a simple rule-based recommender. Each song is described by a small set of attributes, and the system compares them to a user taste profile to score and rank likely matches.

- `Song` features used in this simulation:
  - `id`, `title`, `artist`
  - `genre`
  - `mood`
  - `energy`
  - `tempo_bpm`
  - `valence`
  - `danceability`
  - `acousticness`

- `UserProfile` information used in this simulation:
  - `favorite_genre`
  - `favorite_mood`
  - `target_energy`
  - `likes_acoustic`

### Algorithm Recipe

1. Define a user taste profile with target values for genre, mood, energy, and acoustic preference.
2. Compare each song to the profile using a weighted scoring rule.
3. Give a stronger reward for direct matches on categorical features such as genre and mood.
4. For numerical features, reward songs that are close to the target value rather than simply higher or lower.
5. Combine the feature scores into a total score and rank songs from highest to lowest.

A simple scoring approach is:

- Genre match: 2.0 points
- Mood match: 1.0 point
- Energy closeness: 1.0 point
- Acousticness closeness: 0.7 point
- Valence closeness: 0.5 point
- Danceability closeness: 0.5 point

This makes genre the strongest signal while still allowing mood and audio characteristics to influence the result.

### Expected Biases

This system may over-prioritize genre, which can cause it to miss great songs that match the user’s mood or energy even when they belong to a different genre. It also uses a very small feature set, so it cannot capture deeper preferences such as lyrics, cultural context, or personal history.

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

The following is an example of the recommender output for a sample user profile with genre set to pop, mood set to happy, and energy target near 0.8:

```text
Loaded songs: 18

Top recommendations:

1. Sunrise City
   Score: 5.14
   Reasons:
     - genre match (+2.0)
     - mood match (+1.0)
     - energy close (+0.98)
     - acousticness close (+0.48)
     - valence close (+0.33)
     - danceability close (+0.35)

2. Gym Hero
   Score: 3.93
   Reasons:
     - genre match (+2.0)
     - mood mismatch (intense)
     - energy close (+0.87)
     - acousticness close (+0.39)
     - valence close (+0.36)
     - danceability close (+0.31)

3. Rooftop Lights
   Score: 3.24
   Reasons:
     - genre mismatch (indie pop)
     - mood match (+1.0)
     - energy close (+0.96)
     - acousticness close (+0.59)
     - valence close (+0.34)
     - danceability close (+0.34)

4. Night Drive Loop
   Score: 2.33
   Reasons:
     - genre mismatch (synthwave)
     - mood mismatch (moody)
     - energy close (+0.95)
     - acousticness close (+0.50)
     - valence close (+0.49)
     - danceability close (+0.39)

5. Firelight Parade
   Score: 2.30
   Reasons:
     - genre mismatch (country)
     - mood mismatch (romantic)
     - energy close (+0.83)
     - acousticness close (+0.69)
     - valence close (+0.37)
     - danceability close (+0.41)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Adversarial Profile Results

The following profiles were defined as edge-case prompts meant to stress-test the scoring logic.

### 1. Genre-only gambit

```text
Profile: Genre-only gambit
Description: Uses only a favorite genre to test whether the scorer over-focuses on the categorical match.
Preferences: {'genre': 'pop'}

Top 5 recommendations:
1. Sunrise City
   Score: 3.16
   Reasons:
     - genre match (+2.0)
     - acousticness close (+0.48)
     - valence close (+0.33)
     - danceability close (+0.35)

2. Gym Hero
   Score: 3.06
   Reasons:
     - genre match (+2.0)
     - acousticness close (+0.39)
     - valence close (+0.36)
     - danceability close (+0.31)

3. Firelight Parade
   Score: 1.47
   Reasons:
     - genre mismatch (country)
     - acousticness close (+0.69)
     - valence close (+0.37)
     - danceability close (+0.41)

4. Quiet Harbor
   Score: 1.46
   Reasons:
     - genre mismatch (reggae)
     - acousticness close (+0.64)
     - valence close (+0.41)
     - danceability close (+0.41)

5. Midnight Coding
   Score: 1.46
   Reasons:
     - genre mismatch (lofi)
     - acousticness close (+0.55)
     - valence close (+0.47)
     - danceability close (+0.44)
```

### 2. Acoustic bait

```text
Profile: Acoustic bait
Description: Claims a strong acoustic preference despite an otherwise mismatched mood and genre.
Preferences: {'genre': 'rock', 'mood': 'intense', 'energy': 0.95, 'likes_acoustic': True}

Top 5 recommendations:
1. Storm Runner
   Score: 5.08
   Reasons:
     - genre match (+2.0)
     - mood match (+1.0)
     - energy close (+0.96)
     - acousticness close (+0.21)
     - valence close (+0.49)
     - danceability close (+0.42)

2. Gym Hero
   Score: 2.83
   Reasons:
     - genre mismatch (pop)
     - mood match (+1.0)
     - energy close (+0.98)
     - acousticness close (+0.17)
     - valence close (+0.36)
     - danceability close (+0.31)

3. Golden Hour Echo
   Score: 2.05
   Reasons:
     - genre mismatch (folk)
     - mood mismatch (nostalgic)
     - energy close (+0.60)
     - acousticness close (+0.62)
     - valence close (+0.39)
     - danceability close (+0.45)

4. Focus Flow
   Score: 2.04
   Reasons:
     - genre mismatch (lofi)
     - mood mismatch (focused)
     - energy close (+0.45)
     - acousticness close (+0.69)
     - valence close (+0.46)
     - danceability close (+0.45)

5. Midnight Coding
   Score: 2.02
   Reasons:
     - genre mismatch (lofi)
     - mood mismatch (chill)
     - energy close (+0.47)
     - acousticness close (+0.64)
     - valence close (+0.47)
     - danceability close (+0.44)
```

### 3. Energy extremist

```text
Profile: Energy extremist
Description: Targets a very high energy value and a contradictory mood to probe whether energy dominates the ranking.
Preferences: {'genre': 'lofi', 'mood': 'happy', 'energy': 0.95, 'likes_acoustic': False}

Top 5 recommendations:
1. Midnight Coding
   Score: 3.72
   Reasons:
     - genre match (+2.0)
     - mood mismatch (chill)
     - energy close (+0.47)
     - acousticness close (+0.34)
     - valence close (+0.47)
     - danceability close (+0.44)

2. Focus Flow
   Score: 3.65
   Reasons:
     - genre match (+2.0)
     - mood mismatch (focused)
     - energy close (+0.45)
     - acousticness close (+0.29)
     - valence close (+0.46)
     - danceability close (+0.45)

3. Library Rain
   Score: 3.55
   Reasons:
     - genre match (+2.0)
     - mood mismatch (chill)
     - energy close (+0.40)
     - acousticness close (+0.24)
     - valence close (+0.45)
     - danceability close (+0.46)

4. Sunrise City
   Score: 3.24
   Reasons:
     - genre mismatch (pop)
     - mood match (+1.0)
     - energy close (+0.87)
     - acousticness close (+0.69)
     - valence close (+0.33)
     - danceability close (+0.35)

5. Rooftop Lights
   Score: 3.09
   Reasons:
     - genre mismatch (indie pop)
     - mood match (+1.0)
     - energy close (+0.81)
     - acousticness close (+0.59)
     - valence close (+0.34)
     - danceability close (+0.34)
```

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

My biggest learning moment was realizing how much a simple scoring rule can make a system feel personal. A few hand-written rules about genre, mood, and energy were enough to produce recommendations that looked believable, even though the model was not really understanding taste.

Using AI tools helped me move faster by generating starter code, suggesting profile ideas, and helping me explain the results. I still needed to double-check the outputs, especially when the model produced explanations or ranking ideas that looked plausible but did not always match the actual scoring logic. If I extended this project, I would try adding more features, more diverse songs, and a way to make the recommendations less narrow so they feel less repetitive.



