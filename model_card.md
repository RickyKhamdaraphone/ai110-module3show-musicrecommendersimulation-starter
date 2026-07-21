# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Goal / Task

This recommender suggests songs that fit a user's stated taste. It tries to predict which songs a person may enjoy based on simple music features.

---

## 3. Data Used

The dataset contains 18 songs. Each song has features like genre, mood, energy, danceability, valence, and acousticness. The catalog is small, so it does not cover every style or every type of listener.

---

## 4. Algorithm Summary

The system gives each song a score by comparing it to the user's preferences. Genre and mood are strong signals. Energy, acousticness, valence, and danceability also help the score. Songs with the highest total score are shown first.

---

## 5. Observed Behavior / Biases

The system often favors obvious matches. It can over-focus on genre and mood, which may make the recommendations feel narrow. It may also miss songs from less common genres or artists.

---

## 6. Limitations and Bias

This system can create a filter-bubble effect. A user who likes one style may keep getting very similar songs. It also uses a small set of features, so it cannot understand deeper taste, culture, or personal context.

---

## 7. Evaluation Process

I tested several user profiles, including a genre-only profile, an acoustic-focused profile, and an energy-focused profile. I compared the top results for each profile and checked whether the order made sense. I also looked for surprising shifts when the preferences changed.

---

## 8. Intended Use and Non-Intended Use

This system is best for classroom demos and simple experiments. It is useful for showing how a content-based recommender works. It should not be used for real music platform decisions or for important personal recommendations.

---

## 9. Ideas for Improvement

I would add more songs and more features, such as lyrics or listening history. I would also make the recommendations more diverse so users do not get stuck in one style. I would improve the explanations so they are easier to understand.

---

## 10. Personal Reflection

This project helped me see how recommender systems turn simple data into suggestions. I also learned that small design choices can create bias and limit variety. The system is simple, but it shows how recommendation tools can shape what people discover.

