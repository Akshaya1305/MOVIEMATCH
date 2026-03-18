# 🎬 MovieMatch — Movie Recommendation System

An AI-powered movie recommendation web app built with Python, Flask, and scikit-learn.

## 🚀 Features
- Content-based filtering using TF-IDF and Cosine Similarity
- Recommends 5 similar movies instantly
- Full movie detail page with Director, Cast, Genres, Rating
- OTT platform availability (Netflix, Prime, Hotstar)
- Search history
- Case-insensitive search
- Movie not found error handling
- Clean dark minimalist UI

## 🛠️ Tech Stack
- **Python** — Core programming language
- **scikit-learn** — TF-IDF Vectorization & Cosine Similarity
- **Pandas** — Data loading and preprocessing
- **Flask** — Web framework
- **HTML/CSS/JavaScript** — Frontend

## 📦 Dataset
TMDB 5000 Movies and Credits Dataset from Kaggle.

## ⚙️ How to Run

1. Clone the repository
git clone https://github.com/YOUR_USERNAME/moviematch

2. Install dependencies
pip install flask pandas scikit-learn numpy

3. Download dataset from Kaggle
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
- Place tmdb_5000_movies.csv and rename to movies.csv
- Place tmdb_5000_credits.csv in same folder

4. Run the app
python app.py

5. Open browser
http://127.0.0.1:5000

## 🧠 How It Works
1. Movie metadata is combined into one text field
2. TF-IDF Vectorizer converts text into numerical vectors
3. Cosine Similarity finds the most similar movies
4. Flask serves results on a clean web interface
5. Clicking a movie shows full details from the dataset
```

Press **Ctrl + S** to save!

---

## 📸 Step 3 — Take Screenshots

1. In VS Code left panel — right click → **New Folder** → name it `screenshots`
2. Open your app in browser `http://127.0.0.1:5000`
3. Take 3 screenshots:
   - Home page → Press **Windows + Shift + S** → save as `home.png`
   - Results page (after searching) → save as `results.png`
   - Detail page (after clicking a card) → save as `detail.png`
4. Copy all 3 screenshots into the `screenshots` folder

---

## 🌐 Step 4 — Create GitHub Repository

1. Go to 👉 [https://github.com](https://github.com)
2. Login to your account
3. Click **"+"** button at top right
4. Click **"New repository"**
5. Fill in:
   - **Repository name:** `moviematch`
   - **Description:** `AI powered movie recommendation system`
   - **Visibility:** ✅ Public
   - ❌ Do NOT tick any checkboxes
6. Click **"Create repository"**
7. You'll see a page with your repo URL — **copy the URL** that looks like:
```
https://github.com/YOURUSERNAME/moviematch.git