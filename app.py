from flask import Flask, render_template, request, jsonify
from recommendation import get_recommendations, get_movie_details

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie_name']
    recommendations = get_recommendations(movie_name)

    if len(recommendations) == 1 and "not found" in recommendations[0].lower():
        return render_template('index.html',
                             movie=movie_name,
                             recommendations=[],
                             error=True)

    return render_template('index.html',
                         movie=movie_name,
                         recommendations=recommendations,
                         error=False)

@app.route('/movie/<movie_title>')
def movie_detail(movie_title):
    details = get_movie_details(movie_title)
    if not details:
        return render_template('detail.html', error=True)
    return render_template('detail.html', movie=details)

if __name__ == '__main__':
    app.run(debug=True)