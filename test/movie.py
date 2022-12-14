# create the form to search movie
from imdb import Cinemagoer
import PyMovieDb
from PyMovieDb import IMDB
import tkinter as tk
import json
import io
import base64
from urllib.request import urlopen
# ia = Cinemagoer()
ia = IMDB()
root = tk.Tk()
root.title("Movie Scraper")
root.geometry("800x800")
root.configure(bg="black")

# create a frame to hold the widgets
frame = tk.Frame(root, bg="black")
frame.pack()

title = tk.Label(frame, text="Movie Scrapper", font=(
    "Times New Roman", 20, "bold"), bg="black", fg="white")
title.grid(row=0, column=0, columnspan=2, pady=10)

# Create a label for the first name
searchMovies = tk.Label(frame, text="Name Of Movie:", font=(
    "Times New Roman", 15, "bold"), bg="black", fg="white")
searchMovies.grid(row=1, column=0, padx=10, pady=10)

# Create an entry box for the first name
searchMoviesEntry = tk.Entry(frame, font=(
    "Times New Roman", 15, "bold"), bg="white", fg="black", width=30)
searchMoviesEntry.grid(row=1, column=1, padx=10, pady=10)
# label.pack()
# Searching movies that have rock in their name


def search():
    print("Searching...")
    userSearchValue = searchMoviesEntry.get()
    # movies = ia.search_movie("rock")
    print(userSearchValue)
    # movies = ia.search_movie(userSearchValue)
    
    movies = ia.get_by_name(userSearchValue)
    
    # print(movies[0])
    result = json.loads(movies)
    movieName = result["name"]
    movieNameLabel = tk.Label(frame, text="Movieee", font=( "Times New Roman", 15, "bold"), bg="black", fg="white")
    movieNameLabel.grid(row=2, column=0, padx=10, pady=10)
    # loop through and display genres
    genres = result["genre"]
    tableRow = 2
    for genre in genres:
        tk.Label(frame, text=genre, font=( "Times New Roman", 15, "bold"), bg="black", fg="white").grid(row=tableRow, column=1, padx=10, pady=10)
        tableRow += 1
        
    searchMoviesEntry.delete(0, tk.END)
    print(result)


    movieNameLabel.destroy()
    # print(movies[0].keys())


searchButton = tk.Button(frame, text="Search", font=(
    "Times New Roman", 15, "bold"), bg="white", fg="black", width=15, command=search)
searchButton.grid(row=6, column=1, columnspan=1, padx=10, pady=20)


root.mainloop()
