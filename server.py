"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, jsonify, session, redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
# Replace this with routes and view functions!


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/movies')
def get_all_movies():
    """
    Get all movies.
    """
    
    all_movie_data = crud.get_movies()

    list_of_movies = []
    for movie in all_movie_data:
        movie_dict = {'title': movie.title,
                      'overview': movie.overview,
                      'release_date': movie.release_date,
                      'poster_path': movie.poster_path,
                      }
        list_of_movies.append(movie_dict)
    return jsonify(list_of_movies)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
