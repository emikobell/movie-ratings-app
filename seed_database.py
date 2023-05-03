"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb movie-ratings")
os.system("createdb movie-ratings")

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    format = "%Y-%m-%d"
    formatted_date = datetime.strptime(movie['release_date'], format)

    movies_in_db.append(
        crud.create_movie(title=movie['title'],
                          overview=movie['overview'],
                          release_date=formatted_date,
                          poster_path=movie['poster_path']))

model.db.session.add_all(movies_in_db)
model.db.session.commit()


user_list = []
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(email, password)

    for _ in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)

        rating = crud.create_rating(user, random_movie, score)
        user.ratings.append(rating)

    user_list.append(user)

model.db.session.add_all(user_list)
model.db.session.commit()
