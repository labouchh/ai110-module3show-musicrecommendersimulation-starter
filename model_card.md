# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name 

Recotune 1.0

## 2. Intended Use  

 This recommender is designed to suggest songs based on what a user likes. It looks at things like genre, mood, energy, and acoustic style to find songs that match their taste. It is made for people who want personalized music suggestions based on their preferences. This is a simpler version of how real music apps recommend songs to users.

## 3. How the Model Works  

The scoring approach is mainly based on mood, genre, and whether they prefer a certain tempo and energy level. It uses a point system where +2 pt is for a genre match, +1 for mood match, the closer the song is to the energy level prefered it gets more points, and for acousticness it gets a point if the user likes it. 

## 4. Data  
## Data Used

The dataset contains 20 songs. Each song includes information such as genre, mood, energy level, tempo, valence, danceability, and acousticness.

The dataset includes different genres such as pop, lofi, rock, hip-hop, EDM, classical, R&B, country, folk, reggae, and more. It also includes different moods such as happy, chill, intense, relaxed, romantic, nostalgic, and energetic.

I added 10 additional songs to the original dataset to make the catalog more diverse.

Some parts of musical taste are still missing from the dataset compared to advanced systems. It does not include information like lyrics, personal memories connected to songs, listening history, favorite artists, or how often a user skips or replays a song. These factors can affect real-world recommendations immensly.

## 5. Strengths  
## Where the System Works Well

The system works well for users with clear preferences, such as a favorite genre or mood. It correctly recommends songs like pop songs for high-energy pop users and lofi songs for chill users. Because there's a clear scoring system, it is able to find matching genre, mood, and energy level. 

## 6. Limitations and Bias

It does not include information like lyrics, personal memories connected to songs, listening history, favorite artists, or how often a user skips or replays a song. These factors can affect real-world recommendations immensly. The model can also favor songs with similar energy levels, even if the genre does not fully match the user's taste.

## 7. Evaluation  

After the 3 user profile tests of intense rock, high energy pop, and chill lofi, I checked whether the recommendations matched each user's genre, mood, and energy preferences. The results were expected and there were no major surprises, everything matches after comparing the different profiles.

## 8. Future Work  

I would build an algorithm that uses history tracking so that I can find accurate recommendations through songs replayed, artists followed/most listened to, or tracking the last songs listened to.
---

## 9. Personal Reflection  

I never expected a song recommender to be built with logic using mathematics, like having points system to relate songs. It's definitely interesting. This project helped me understand that apps like Spotify use much more data like listening history and user behavior to make recommendations more accurate.
