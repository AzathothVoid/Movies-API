from fastapi import FastAPI
import mysql.connector

app = FastAPI()
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="groupproject")
mycursor = mydb.cursor()


@app.get("/movies")
def get_movies():
    sql = "SELECT * FROM movies"
    mycursor.execute(sql)
    movies = mycursor.fetchall()
    return movies


@app.get("/movie/{movie_id}")
def get_movie(movie_id: int):
    sql = "SELECT * FROM movies WHERE id = %s"
    val = (movie_id,)
    mycursor.execute(sql, val)
    movie = mycursor.fetchall()
    return movie


@app.delete("/movie/{movie_id}")
def delete_movie(movie_id: int):
    sql = "DELETE FROM movies WHERE id = %s"
    val = (movie_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    return ("Succesfully Removed")


@app.post("/create_movie")
def create_movie(movie: dict):
    sql = "INSERT INTO movies (Title, Year, Description) VALUES (%s,%s,%s)"
    val = (movie["Title"], movie["Year"], movie["Description"])
    mycursor.execute(sql, val)
    mydb.commit()
    return movie


@app.post("/update_movie")
def update_movie(movie: dict):
    sql = "UPDATE movies SET Title = %s, Year = %s, Description = %s WHERE id = %s"
    val = (movie['Title'], movie['Year'], movie['Description'], movie['id'])
    mycursor.execute(sql, val)
    mydb.commit()
    return movie





